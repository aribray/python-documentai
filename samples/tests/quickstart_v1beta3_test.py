# # Copyright 2020 Google LLC
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
import os

from samples.snippets import quickstart_sample_v1beta3


location = "us"
project_id = '1012616486416'
processor_id = '90484cfdedb024f6'
bucket_name = 'python_docs_samples_test_%s' % uuid4()
gcs_input_uri = 'gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri_prefix = uuid4()
file_name = 'samples/snippets/resources/invoice.pdf'
file_path = os.path.join(os.getcwd(), file_name)


def test_quickstart(capsys):
    quickstart_sample_v1beta3.quickstart(project_id=project_id, location=location, processor_id=processor_id, file_path=file_path)
    out, _ = capsys.readouterr()

    assert "Paragraph" in out
