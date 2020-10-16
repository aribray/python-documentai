# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from uuid import uuid4
import pytest
import os
from google.cloud import storage

from samples.snippets import batch_process_documents_sample_v1beta3

project_id = 'python-docs-samples-tests'
location = 'us'
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
processor_id = '90484cfdedb024f6'
gcs_input_uri = 'gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri = 'gs://document-ai-python'
gcs_output_uri_prefix = uuid4()


@pytest.fixture(scope="module")
def test_bucket():
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_output_uri)
    yield bucket

    try:
        blobs = list(bucket.list_blobs())
        for blob in blobs:
            blob.delete()
    except Exception:
        pass


def test_batch_process_documents(capsys, test_bucket):
    batch_process_documents_sample_v1beta3.batch_process_documents(project_id=project_id, location=location, processor_id=processor_id, gcs_input_uri=gcs_input_uri, gcs_output_uri=gcs_output_uri, gcs_output_uri_prefix=gcs_output_uri_prefix)
    out, _ = capsys.readouterr()

    assert "Extracted" in out
    assert "Paragraph" in out