# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START documentai_batch_process_document]
import re
import json
from google.cloud import documentai_v1beta3 as documentai
from google.cloud import storage

# TODO(developer): Uncomment these variables before running the sample.
# project_id= 'YOUR_PROJECT_ID'
# location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID' # Create processor in Cloud Console
# input_uri = "YOUR_INPUT_URI"
# gcs_output_bucket_uri = "YOUR_OUTPUT_BUCKET_URI"
# gcs_output_uri_prefix = "YOUR_OUTPUT_URI_PREFIX"


def batch_process_documents(
        project_id,
        location,
        processor_id,
        gcs_input_uri,
        gcs_output_uri,
        gcs_output_uri_prefix):

    client = documentai.DocumentProcessorServiceClient()

    destination_uri = f'{gcs_output_uri}/{gcs_output_uri_prefix}/'

    # mime_type can be application/pdf, image/tiff,
    # and image/gif, or application/json
    input_config = documentai.types.document_processor_service.BatchProcessRequest.BatchInputConfig(
        gcs_source=gcs_input_uri, mime_type='application/pdf')

    # where to write results
    output_config = documentai.types.document_processor_service.BatchProcessRequest.BatchOutputConfig(
        gcs_destination=destination_uri
    )

    # Location can be 'us' or 'eu'
    name = f'projects/{project_id}/locations/{location}/processors/{processor_id}'
    request = documentai.types.document_processor_service.BatchProcessRequest(
        name=name,
        input_configs=[input_config],
        output_config=output_config,)

    operation = client.batch_process_documents(request)

    # Wait for the operation to finish
    operation.result()

    # Results are written to GCS. Use a regex to find
    # output files
    match = re.match(r'gs://([^/]+)/(.+)', destination_uri)
    output_bucket = match.group(1)
    prefix = match.group(2)

    storage_client = storage.client.Client()
    bucket = storage_client.get_bucket(output_bucket)
    blob_list = list(bucket.list_blobs(prefix=prefix))
    print('Output files:')

    def get_text(doc_element):
        """Document AI identifies form fields by their offsets
        in document text. This function converts offsets
        to text snippets.
        """
        response = ''
        # If a text segment spans several lines, it will
        # be stored in different text segments.
        for segment in doc_element['textAnchor']['textSegments']:
            start_index = int(segment['startIndex']) if 'startIndex' in doc_element['textAnchor'] else 0
            end_index = int(segment['endIndex'])
            response += document['text'][start_index:end_index]
        return response

    for i, blob in enumerate(blob_list):
        json_string = blob.download_as_bytes()
        document = json.loads(json_string)

        print(f'Fetched file {i + 1}')

        for page in document['pages']:
            for form_field in page['formFields']:
                field_name = get_text(form_field['fieldName'])
                field_value = get_text(form_field['fieldValue'])
                print('Extracted key value pair:')
                print(f'\t{field_name}, {field_value}')
            for paragraph in document['pages']:
                paragraph_text = get_text(paragraph['layout'])
                print(f'Paragraph text:\n{paragraph_text}')

# [END documentai_batch_process_document]
