# -*- coding: utf-8 -*-

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

import proto  # type: ignore


from google.cloud.documentai_v1beta3.types import geometry
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore
from google.type import color_pb2 as gt_color  # type: ignore
from google.type import date_pb2 as date  # type: ignore
from google.type import datetime_pb2 as datetime  # type: ignore
from google.type import money_pb2 as money  # type: ignore
from google.type import postal_address_pb2 as postal_address  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3", manifest={"Document",},
)


class Document(proto.Message):
    r"""Document represents the canonical document resource in
    Document Understanding AI.
    It is an interchange format that provides insights into
    documents and allows for collaboration between users and
    Document Understanding AI to iterate and optimize for quality.

    Attributes:
        uri (str):
            Currently supports Google Cloud Storage URI of the form
            ``gs://bucket_name/object_name``. Object versioning is not
            supported. See `Google Cloud Storage Request
            URIs <https://cloud.google.com/storage/docs/reference-uris>`__
            for more info.
        content (bytes):
            Inline document content, represented as a stream of bytes.
            Note: As with all ``bytes`` fields, protobuffers use a pure
            binary representation, whereas JSON representations use
            base64.
        mime_type (str):
            An IANA published MIME type (also referred to
            as media type). For more information, see
            https://www.iana.org/assignments/media-
            types/media-types.xhtml.
        text (str):
            UTF-8 encoded text in reading order from the
            document.
        text_styles (Sequence[~.document.Document.Style]):
            Styles for the
            [Document.text][google.cloud.documentai.v1beta3.Document.text].
        pages (Sequence[~.document.Document.Page]):
            Visual page layout for the
            [Document][google.cloud.documentai.v1beta3.Document].
        entities (Sequence[~.document.Document.Entity]):
            A list of entities detected on
            [Document.text][google.cloud.documentai.v1beta3.Document.text].
            For document shards, entities in this list may cross shard
            boundaries.
        entity_relations (Sequence[~.document.Document.EntityRelation]):
            Relationship among
            [Document.entities][google.cloud.documentai.v1beta3.Document.entities].
        translations (Sequence[~.document.Document.Translation]):
            A list of translations on
            [Document.text][google.cloud.documentai.v1beta3.Document.text].
            For document shards, translations in this list may cross
            shard boundaries.
        text_changes (Sequence[~.document.Document.TextChange]):
            A list of text corrections made to [Document.text]. This is
            usually used for annotating corrections to OCR mistakes.
            Text changes for a given revision may not overlap with each
            other.
        shard_info (~.document.Document.ShardInfo):
            Information about the sharding if this
            document is sharded part of a larger document.
            If the document is not sharded, this message is
            not specified.
        error (~.status.Status):
            Any error that occurred while processing this
            document.
        revisions (Sequence[~.document.Document.Revision]):
            Revision history of this document.
    """

    class ShardInfo(proto.Message):
        r"""For a large document, sharding may be performed to produce
        several document shards. Each document shard contains this field
        to detail which shard it is.

        Attributes:
            shard_index (int):
                The 0-based index of this shard.
            shard_count (int):
                Total number of shards.
            text_offset (int):
                The index of the first character in
                [Document.text][google.cloud.documentai.v1beta3.Document.text]
                in the overall document global text.
        """

        shard_index = proto.Field(proto.INT64, number=1)

        shard_count = proto.Field(proto.INT64, number=2)

        text_offset = proto.Field(proto.INT64, number=3)

    class Style(proto.Message):
        r"""Annotation for common text style attributes. This adheres to
        CSS conventions as much as possible.

        Attributes:
            text_anchor (~.document.Document.TextAnchor):
                Text anchor indexing into the
                [Document.text][google.cloud.documentai.v1beta3.Document.text].
            color (~.gt_color.Color):
                Text color.
            background_color (~.gt_color.Color):
                Text background color.
            font_weight (str):
                Font weight. Possible values are normal, bold, bolder, and
                lighter. https://www.w3schools.com/cssref/pr_font_weight.asp
            text_style (str):
                Text style. Possible values are normal, italic, and oblique.
                https://www.w3schools.com/cssref/pr_font_font-style.asp
            text_decoration (str):
                Text decoration. Follows CSS standard.
                https://www.w3schools.com/cssref/pr_text_text-decoration.asp
            font_size (~.document.Document.Style.FontSize):
                Font size.
        """

        class FontSize(proto.Message):
            r"""Font size with unit.

            Attributes:
                size (float):
                    Font size for the text.
                unit (str):
                    Unit for the font size. Follows CSS naming
                    (in, px, pt, etc.).
            """

            size = proto.Field(proto.FLOAT, number=1)

            unit = proto.Field(proto.STRING, number=2)

        text_anchor = proto.Field(
            proto.MESSAGE, number=1, message="Document.TextAnchor",
        )

        color = proto.Field(proto.MESSAGE, number=2, message=gt_color.Color,)

        background_color = proto.Field(proto.MESSAGE, number=3, message=gt_color.Color,)

        font_weight = proto.Field(proto.STRING, number=4)

        text_style = proto.Field(proto.STRING, number=5)

        text_decoration = proto.Field(proto.STRING, number=6)

        font_size = proto.Field(
            proto.MESSAGE, number=7, message="Document.Style.FontSize",
        )

    class Page(proto.Message):
        r"""A page in a [Document][google.cloud.documentai.v1beta3.Document].

        Attributes:
            page_number (int):
                1-based index for current
                [Page][google.cloud.documentai.v1beta3.Document.Page] in a
                parent [Document][google.cloud.documentai.v1beta3.Document].
                Useful when a page is taken out of a
                [Document][google.cloud.documentai.v1beta3.Document] for
                individual processing.
            image (~.document.Document.Page.Image):
                Rendered image for this page. This image is
                preprocessed to remove any skew, rotation, and
                distortions such that the annotation bounding
                boxes can be upright and axis-aligned.
            transforms (Sequence[~.document.Document.Page.Matrix]):
                Transformation matrices that were applied to the original
                document image to produce
                [Page.image][google.cloud.documentai.v1beta3.Document.Page.image].
            dimension (~.document.Document.Page.Dimension):
                Physical dimension of the page.
            layout (~.document.Document.Page.Layout):
                [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                for the page.
            detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                A list of detected languages together with
                confidence.
            blocks (Sequence[~.document.Document.Page.Block]):
                A list of visually detected text blocks on
                the page. A block has a set of lines (collected
                into paragraphs) that have a common line-spacing
                and orientation.
            paragraphs (Sequence[~.document.Document.Page.Paragraph]):
                A list of visually detected text paragraphs
                on the page. A collection of lines that a human
                would perceive as a paragraph.
            lines (Sequence[~.document.Document.Page.Line]):
                A list of visually detected text lines on the
                page. A collection of tokens that a human would
                perceive as a line.
            tokens (Sequence[~.document.Document.Page.Token]):
                A list of visually detected tokens on the
                page.
            visual_elements (Sequence[~.document.Document.Page.VisualElement]):
                A list of detected non-text visual elements
                e.g. checkbox, signature etc. on the page.
            tables (Sequence[~.document.Document.Page.Table]):
                A list of visually detected tables on the
                page.
            form_fields (Sequence[~.document.Document.Page.FormField]):
                A list of visually detected form fields on
                the page.
        """

        class Dimension(proto.Message):
            r"""Dimension for the page.

            Attributes:
                width (float):
                    Page width.
                height (float):
                    Page height.
                unit (str):
                    Dimension unit.
            """

            width = proto.Field(proto.FLOAT, number=1)

            height = proto.Field(proto.FLOAT, number=2)

            unit = proto.Field(proto.STRING, number=3)

        class Image(proto.Message):
            r"""Rendered image contents for this page.

            Attributes:
                content (bytes):
                    Raw byte content of the image.
                mime_type (str):
                    Encoding mime type for the image.
                width (int):
                    Width of the image in pixels.
                height (int):
                    Height of the image in pixels.
            """

            content = proto.Field(proto.BYTES, number=1)

            mime_type = proto.Field(proto.STRING, number=2)

            width = proto.Field(proto.INT32, number=3)

            height = proto.Field(proto.INT32, number=4)

        class Matrix(proto.Message):
            r"""Representation for transformation matrix, intended to be
            compatible and used with OpenCV format for image manipulation.

            Attributes:
                rows (int):
                    Number of rows in the matrix.
                cols (int):
                    Number of columns in the matrix.
                type_ (int):
                    This encodes information about what data type the matrix
                    uses. For example, 0 (CV_8U) is an unsigned 8-bit image. For
                    the full list of OpenCV primitive data types, please refer
                    to
                    https://docs.opencv.org/4.3.0/d1/d1b/group__core__hal__interface.html
                data (bytes):
                    The matrix data.
            """

            rows = proto.Field(proto.INT32, number=1)

            cols = proto.Field(proto.INT32, number=2)

            type_ = proto.Field(proto.INT32, number=3)

            data = proto.Field(proto.BYTES, number=4)

        class Layout(proto.Message):
            r"""Visual element describing a layout unit on a page.

            Attributes:
                text_anchor (~.document.Document.TextAnchor):
                    Text anchor indexing into the
                    [Document.text][google.cloud.documentai.v1beta3.Document.text].
                confidence (float):
                    Confidence of the current
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    within context of the object this layout is for. e.g.
                    confidence can be for a single token, a table, a visual
                    element, etc. depending on context. Range [0, 1].
                bounding_poly (~.geometry.BoundingPoly):
                    The bounding polygon for the
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout].
                orientation (~.document.Document.Page.Layout.Orientation):
                    Detected orientation for the
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout].
            """

            class Orientation(proto.Enum):
                r"""Detected human reading orientation."""
                ORIENTATION_UNSPECIFIED = 0
                PAGE_UP = 1
                PAGE_RIGHT = 2
                PAGE_DOWN = 3
                PAGE_LEFT = 4

            text_anchor = proto.Field(
                proto.MESSAGE, number=1, message="Document.TextAnchor",
            )

            confidence = proto.Field(proto.FLOAT, number=2)

            bounding_poly = proto.Field(
                proto.MESSAGE, number=3, message=geometry.BoundingPoly,
            )

            orientation = proto.Field(
                proto.ENUM, number=4, enum="Document.Page.Layout.Orientation",
            )

        class Block(proto.Message):
            r"""A block has a set of lines (collected into paragraphs) that
            have a common line-spacing and orientation.

            Attributes:
                layout (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for
                    [Block][google.cloud.documentai.v1beta3.Document.Page.Block].
                detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages together with
                    confidence.
                provenance (~.document.Document.Provenance):
                    The history of this annotation.
            """

            layout = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=2, message="Document.Page.DetectedLanguage",
            )

            provenance = proto.Field(
                proto.MESSAGE, number=3, message="Document.Provenance",
            )

        class Paragraph(proto.Message):
            r"""A collection of lines that a human would perceive as a
            paragraph.

            Attributes:
                layout (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for
                    [Paragraph][google.cloud.documentai.v1beta3.Document.Page.Paragraph].
                detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages together with
                    confidence.
                provenance (~.document.Document.Provenance):
                    The  history of this annotation.
            """

            layout = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=2, message="Document.Page.DetectedLanguage",
            )

            provenance = proto.Field(
                proto.MESSAGE, number=3, message="Document.Provenance",
            )

        class Line(proto.Message):
            r"""A collection of tokens that a human would perceive as a line.
            Does not cross column boundaries, can be horizontal, vertical,
            etc.

            Attributes:
                layout (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for
                    [Line][google.cloud.documentai.v1beta3.Document.Page.Line].
                detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages together with
                    confidence.
                provenance (~.document.Document.Provenance):
                    The  history of this annotation.
            """

            layout = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=2, message="Document.Page.DetectedLanguage",
            )

            provenance = proto.Field(
                proto.MESSAGE, number=3, message="Document.Provenance",
            )

        class Token(proto.Message):
            r"""A detected token.

            Attributes:
                layout (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for
                    [Token][google.cloud.documentai.v1beta3.Document.Page.Token].
                detected_break (~.document.Document.Page.Token.DetectedBreak):
                    Detected break at the end of a
                    [Token][google.cloud.documentai.v1beta3.Document.Page.Token].
                detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages together with
                    confidence.
                provenance (~.document.Document.Provenance):
                    The  history of this annotation.
            """

            class DetectedBreak(proto.Message):
                r"""Detected break at the end of a
                [Token][google.cloud.documentai.v1beta3.Document.Page.Token].

                Attributes:
                    type_ (~.document.Document.Page.Token.DetectedBreak.Type):
                        Detected break type.
                """

                class Type(proto.Enum):
                    r"""Enum to denote the type of break found."""
                    TYPE_UNSPECIFIED = 0
                    SPACE = 1
                    WIDE_SPACE = 2
                    HYPHEN = 3

                type_ = proto.Field(
                    proto.ENUM, number=1, enum="Document.Page.Token.DetectedBreak.Type",
                )

            layout = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            detected_break = proto.Field(
                proto.MESSAGE, number=2, message="Document.Page.Token.DetectedBreak",
            )

            detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=3, message="Document.Page.DetectedLanguage",
            )

            provenance = proto.Field(
                proto.MESSAGE, number=4, message="Document.Provenance",
            )

        class VisualElement(proto.Message):
            r"""Detected non-text visual elements e.g. checkbox, signature
            etc. on the page.

            Attributes:
                layout (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for
                    [VisualElement][google.cloud.documentai.v1beta3.Document.Page.VisualElement].
                type_ (str):
                    Type of the
                    [VisualElement][google.cloud.documentai.v1beta3.Document.Page.VisualElement].
                detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages together with
                    confidence.
            """

            layout = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            type_ = proto.Field(proto.STRING, number=2)

            detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=3, message="Document.Page.DetectedLanguage",
            )

        class Table(proto.Message):
            r"""A table representation similar to HTML table structure.

            Attributes:
                layout (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for
                    [Table][google.cloud.documentai.v1beta3.Document.Page.Table].
                header_rows (Sequence[~.document.Document.Page.Table.TableRow]):
                    Header rows of the table.
                body_rows (Sequence[~.document.Document.Page.Table.TableRow]):
                    Body rows of the table.
                detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages together with
                    confidence.
            """

            class TableRow(proto.Message):
                r"""A row of table cells.

                Attributes:
                    cells (Sequence[~.document.Document.Page.Table.TableCell]):
                        Cells that make up this row.
                """

                cells = proto.RepeatedField(
                    proto.MESSAGE, number=1, message="Document.Page.Table.TableCell",
                )

            class TableCell(proto.Message):
                r"""A cell representation inside the table.

                Attributes:
                    layout (~.document.Document.Page.Layout):
                        [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                        for
                        [TableCell][google.cloud.documentai.v1beta3.Document.Page.Table.TableCell].
                    row_span (int):
                        How many rows this cell spans.
                    col_span (int):
                        How many columns this cell spans.
                    detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                        A list of detected languages together with
                        confidence.
                """

                layout = proto.Field(
                    proto.MESSAGE, number=1, message="Document.Page.Layout",
                )

                row_span = proto.Field(proto.INT32, number=2)

                col_span = proto.Field(proto.INT32, number=3)

                detected_languages = proto.RepeatedField(
                    proto.MESSAGE, number=4, message="Document.Page.DetectedLanguage",
                )

            layout = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            header_rows = proto.RepeatedField(
                proto.MESSAGE, number=2, message="Document.Page.Table.TableRow",
            )

            body_rows = proto.RepeatedField(
                proto.MESSAGE, number=3, message="Document.Page.Table.TableRow",
            )

            detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=4, message="Document.Page.DetectedLanguage",
            )

        class FormField(proto.Message):
            r"""A form field detected on the page.

            Attributes:
                field_name (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for the
                    [FormField][google.cloud.documentai.v1beta3.Document.Page.FormField]
                    name. e.g. ``Address``, ``Email``, ``Grand total``,
                    ``Phone number``, etc.
                field_value (~.document.Document.Page.Layout):
                    [Layout][google.cloud.documentai.v1beta3.Document.Page.Layout]
                    for the
                    [FormField][google.cloud.documentai.v1beta3.Document.Page.FormField]
                    value.
                name_detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages for name
                    together with confidence.
                value_detected_languages (Sequence[~.document.Document.Page.DetectedLanguage]):
                    A list of detected languages for value
                    together with confidence.
                value_type (str):
                    If the value is non-textual, this field represents the type.
                    Current valid values are:

                    -  blank (this indicates the field_value is normal text)
                    -  "unfilled_checkbox"
                    -  "filled_checkbox".
            """

            field_name = proto.Field(
                proto.MESSAGE, number=1, message="Document.Page.Layout",
            )

            field_value = proto.Field(
                proto.MESSAGE, number=2, message="Document.Page.Layout",
            )

            name_detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=3, message="Document.Page.DetectedLanguage",
            )

            value_detected_languages = proto.RepeatedField(
                proto.MESSAGE, number=4, message="Document.Page.DetectedLanguage",
            )

            value_type = proto.Field(proto.STRING, number=5)

        class DetectedLanguage(proto.Message):
            r"""Detected language for a structural component.

            Attributes:
                language_code (str):
                    The BCP-47 language code, such as "en-US" or "sr-Latn". For
                    more information, see
                    http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
                confidence (float):
                    Confidence of detected language. Range [0, 1].
            """

            language_code = proto.Field(proto.STRING, number=1)

            confidence = proto.Field(proto.FLOAT, number=2)

        page_number = proto.Field(proto.INT32, number=1)

        image = proto.Field(proto.MESSAGE, number=13, message="Document.Page.Image",)

        transforms = proto.RepeatedField(
            proto.MESSAGE, number=14, message="Document.Page.Matrix",
        )

        dimension = proto.Field(
            proto.MESSAGE, number=2, message="Document.Page.Dimension",
        )

        layout = proto.Field(proto.MESSAGE, number=3, message="Document.Page.Layout",)

        detected_languages = proto.RepeatedField(
            proto.MESSAGE, number=4, message="Document.Page.DetectedLanguage",
        )

        blocks = proto.RepeatedField(
            proto.MESSAGE, number=5, message="Document.Page.Block",
        )

        paragraphs = proto.RepeatedField(
            proto.MESSAGE, number=6, message="Document.Page.Paragraph",
        )

        lines = proto.RepeatedField(
            proto.MESSAGE, number=7, message="Document.Page.Line",
        )

        tokens = proto.RepeatedField(
            proto.MESSAGE, number=8, message="Document.Page.Token",
        )

        visual_elements = proto.RepeatedField(
            proto.MESSAGE, number=9, message="Document.Page.VisualElement",
        )

        tables = proto.RepeatedField(
            proto.MESSAGE, number=10, message="Document.Page.Table",
        )

        form_fields = proto.RepeatedField(
            proto.MESSAGE, number=11, message="Document.Page.FormField",
        )

    class Entity(proto.Message):
        r"""A phrase in the text that is a known entity type, such as a
        person, an organization, or location.

        Attributes:
            text_anchor (~.document.Document.TextAnchor):
                Provenance of the entity. Text anchor indexing into the
                [Document.text][google.cloud.documentai.v1beta3.Document.text].
            type_ (str):
                Entity type from a schema e.g. ``Address``.
            mention_text (str):
                Text value in the document e.g. ``1600 Amphitheatre Pkwy``.
            mention_id (str):
                Deprecated. Use ``id`` field instead.
            confidence (float):
                Optional. Confidence of detected Schema entity. Range [0,
                1].
            page_anchor (~.document.Document.PageAnchor):
                Optional. Represents the provenance of this
                entity wrt. the location on the page where it
                was found.
            id (str):
                Canonical id. This will be a unique value in
                the entity list for this document.
            normalized_value (~.document.Document.Entity.NormalizedValue):
                Optional. Normalized entity value. Absent if
                the extracted value could not be converted or
                the type (e.g. address) is not supported for
                certain parsers. This field is also only
                populated for certain supported document types.
            properties (Sequence[~.document.Document.Entity]):
                Optional. Entities can be nested to form a
                hierarchical data structure representing the
                content in the document.
            provenance (~.document.Document.Provenance):
                Optional. The history of this annotation.
            redacted (bool):
                Optional. Whether the entity will be redacted
                for de-identification purposes.
        """

        class NormalizedValue(proto.Message):
            r"""Parsed and normalized entity value.

            Attributes:
                money_value (~.money.Money):
                    Money value. See also:
                    https:
                    github.com/googleapis/googleapis/blob/master/google/type/money.proto
                date_value (~.date.Date):
                    Date value. Includes year, month, day. See
                    also:
                    https:
                    github.com/googleapis/googleapis/blob/master/google/type/date.proto
                datetime_value (~.datetime.DateTime):
                    DateTime value. Includes date, time, and
                    timezone. See also:
                    https:
                    github.com/googleapis/googleapis/blob/master/google/type/datetime.proto
                address_value (~.postal_address.PostalAddress):
                    Postal address. See also:

                    https:
                    github.com/googleapis/googleapis/blob/master/google/type/postal_address.proto
                text (str):
                    Required. Normalized entity value stored as a string. This
                    field is populated for supported document type (e.g.
                    Invoice). For some entity types, one of respective
                    'structured_value' fields may also be populated.

                    -  Money/Currency type (``money_value``) is in the ISO 4217
                       text format.
                    -  Date type (``date_value``) is in the ISO 8601 text
                       format.
                    -  Datetime type (``datetime_value``) is in the ISO 8601
                       text format.
            """

            money_value = proto.Field(
                proto.MESSAGE, number=2, oneof="structured_value", message=money.Money,
            )

            date_value = proto.Field(
                proto.MESSAGE, number=3, oneof="structured_value", message=date.Date,
            )

            datetime_value = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="structured_value",
                message=datetime.DateTime,
            )

            address_value = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="structured_value",
                message=postal_address.PostalAddress,
            )

            text = proto.Field(proto.STRING, number=1)

        text_anchor = proto.Field(
            proto.MESSAGE, number=1, message="Document.TextAnchor",
        )

        type_ = proto.Field(proto.STRING, number=2)

        mention_text = proto.Field(proto.STRING, number=3)

        mention_id = proto.Field(proto.STRING, number=4)

        confidence = proto.Field(proto.FLOAT, number=5)

        page_anchor = proto.Field(
            proto.MESSAGE, number=6, message="Document.PageAnchor",
        )

        id = proto.Field(proto.STRING, number=7)

        normalized_value = proto.Field(
            proto.MESSAGE, number=9, message="Document.Entity.NormalizedValue",
        )

        properties = proto.RepeatedField(
            proto.MESSAGE, number=10, message="Document.Entity",
        )

        provenance = proto.Field(
            proto.MESSAGE, number=11, message="Document.Provenance",
        )

        redacted = proto.Field(proto.BOOL, number=12)

    class EntityRelation(proto.Message):
        r"""Relationship between
        [Entities][google.cloud.documentai.v1beta3.Document.Entity].

        Attributes:
            subject_id (str):
                Subject entity id.
            object_id (str):
                Object entity id.
            relation (str):
                Relationship description.
        """

        subject_id = proto.Field(proto.STRING, number=1)

        object_id = proto.Field(proto.STRING, number=2)

        relation = proto.Field(proto.STRING, number=3)

    class Translation(proto.Message):
        r"""A translation of the text segment.

        Attributes:
            text_anchor (~.document.Document.TextAnchor):
                Provenance of the translation. Text anchor indexing into the
                [Document.text][google.cloud.documentai.v1beta3.Document.text].
                There can only be a single ``TextAnchor.text_segments``
                element. If the start and end index of the text segment are
                the same, the text change is inserted before that index.
            language_code (str):
                The BCP-47 language code, such as "en-US" or "sr-Latn". For
                more information, see
                http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
            translated_text (str):
                Text translated into the target language.
            provenance (Sequence[~.document.Document.Provenance]):
                The history of this annotation.
        """

        text_anchor = proto.Field(
            proto.MESSAGE, number=1, message="Document.TextAnchor",
        )

        language_code = proto.Field(proto.STRING, number=2)

        translated_text = proto.Field(proto.STRING, number=3)

        provenance = proto.RepeatedField(
            proto.MESSAGE, number=4, message="Document.Provenance",
        )

    class TextAnchor(proto.Message):
        r"""Text reference indexing into the
        [Document.text][google.cloud.documentai.v1beta3.Document.text].

        Attributes:
            text_segments (Sequence[~.document.Document.TextAnchor.TextSegment]):
                The text segments from the
                [Document.text][google.cloud.documentai.v1beta3.Document.text].
            content (str):
                Contains the content of the text span so that users do not
                have to look it up in the text_segments.
        """

        class TextSegment(proto.Message):
            r"""A text segment in the
            [Document.text][google.cloud.documentai.v1beta3.Document.text]. The
            indices may be out of bounds which indicate that the text extends
            into another document shard for large sharded documents. See
            [ShardInfo.text_offset][google.cloud.documentai.v1beta3.Document.ShardInfo.text_offset]

            Attributes:
                start_index (int):
                    [TextSegment][google.cloud.documentai.v1beta3.Document.TextAnchor.TextSegment]
                    start UTF-8 char index in the
                    [Document.text][google.cloud.documentai.v1beta3.Document.text].
                end_index (int):
                    [TextSegment][google.cloud.documentai.v1beta3.Document.TextAnchor.TextSegment]
                    half open end UTF-8 char index in the
                    [Document.text][google.cloud.documentai.v1beta3.Document.text].
            """

            start_index = proto.Field(proto.INT64, number=1)

            end_index = proto.Field(proto.INT64, number=2)

        text_segments = proto.RepeatedField(
            proto.MESSAGE, number=1, message="Document.TextAnchor.TextSegment",
        )

        content = proto.Field(proto.STRING, number=2)

    class PageAnchor(proto.Message):
        r"""Referencing the visual context of the entity in the
        [Document.pages][google.cloud.documentai.v1beta3.Document.pages].
        Page anchors can be cross-page, consist of multiple bounding
        polygons and optionally reference specific layout element types.

        Attributes:
            page_refs (Sequence[~.document.Document.PageAnchor.PageRef]):
                One or more references to visual page
                elements
        """

        class PageRef(proto.Message):
            r"""Represents a weak reference to a page element within a
            document.

            Attributes:
                page (int):
                    Required. Index into the
                    [Document.pages][google.cloud.documentai.v1beta3.Document.pages]
                    element
                layout_type (~.document.Document.PageAnchor.PageRef.LayoutType):
                    Optional. The type of the layout element that
                    is being referenced if any.
                layout_id (str):
                    Optional. Deprecated. Use
                    [PageRef.bounding_poly][google.cloud.documentai.v1beta3.Document.PageAnchor.PageRef.bounding_poly]
                    instead.
                bounding_poly (~.geometry.BoundingPoly):
                    Optional. Identifies the bounding polygon of
                    a layout element on the page.
            """

            class LayoutType(proto.Enum):
                r"""The type of layout that is being referenced."""
                LAYOUT_TYPE_UNSPECIFIED = 0
                BLOCK = 1
                PARAGRAPH = 2
                LINE = 3
                TOKEN = 4
                VISUAL_ELEMENT = 5
                TABLE = 6
                FORM_FIELD = 7

            page = proto.Field(proto.INT64, number=1)

            layout_type = proto.Field(
                proto.ENUM, number=2, enum="Document.PageAnchor.PageRef.LayoutType",
            )

            layout_id = proto.Field(proto.STRING, number=3)

            bounding_poly = proto.Field(
                proto.MESSAGE, number=4, message=geometry.BoundingPoly,
            )

        page_refs = proto.RepeatedField(
            proto.MESSAGE, number=1, message="Document.PageAnchor.PageRef",
        )

    class Provenance(proto.Message):
        r"""Structure to identify provenance relationships between
        annotations in different revisions.

        Attributes:
            revision (int):
                The index of the revision that produced this
                element.
            id (int):
                The Id of this operation.  Needs to be unique
                within the scope of the revision.
            parents (Sequence[~.document.Document.Provenance.Parent]):
                References to the original elements that are
                replaced.
            type_ (~.document.Document.Provenance.OperationType):
                The type of provenance operation.
        """

        class OperationType(proto.Enum):
            r"""If a processor or agent does an explicit operation on
            existing elements.
            """
            OPERATION_TYPE_UNSPECIFIED = 0
            ADD = 1
            REMOVE = 2
            REPLACE = 3
            EVAL_REQUESTED = 4
            EVAL_APPROVED = 5

        class Parent(proto.Message):
            r"""Structure for referencing parent provenances.  When an
            element replaces one of more other elements parent references
            identify the elements that are replaced.

            Attributes:
                revision (int):
                    The index of the [Document.revisions] identifying the parent
                    revision.
                id (int):
                    The id of the parent provenance.
            """

            revision = proto.Field(proto.INT32, number=1)

            id = proto.Field(proto.INT32, number=2)

        revision = proto.Field(proto.INT32, number=1)

        id = proto.Field(proto.INT32, number=2)

        parents = proto.RepeatedField(
            proto.MESSAGE, number=3, message="Document.Provenance.Parent",
        )

        type_ = proto.Field(
            proto.ENUM, number=4, enum="Document.Provenance.OperationType",
        )

    class Revision(proto.Message):
        r"""Contains past or forward revisions of this document.

        Attributes:
            agent (str):
                If the change was made by a person specify
                the name or id of that person.
            processor (str):
                If the annotation was made by processor
                identify the processor by its resource name.
            id (str):
                Id of the revision.  Unique within the
                context of the document.
            parent (Sequence[int]):
                The revisions that this revision is based on. This can
                include one or more parent (when documents are merged.) This
                field represents the index into the ``revisions`` field.
            create_time (~.timestamp.Timestamp):
                The time that the revision was created.
            human_review (~.document.Document.Revision.HumanReview):
                Human Review information of this revision.
        """

        class HumanReview(proto.Message):
            r"""Human Review information of the document.

            Attributes:
                state (str):
                    Human review state. e.g. ``requested``, ``succeeded``,
                    ``rejected``.
                state_message (str):
                    A message providing more details about the current state of
                    processing. For example, the rejection reason when the state
                    is ``rejected``.
            """

            state = proto.Field(proto.STRING, number=1)

            state_message = proto.Field(proto.STRING, number=2)

        agent = proto.Field(proto.STRING, number=4, oneof="source")

        processor = proto.Field(proto.STRING, number=5, oneof="source")

        id = proto.Field(proto.STRING, number=1)

        parent = proto.RepeatedField(proto.INT32, number=2)

        create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp.Timestamp,)

        human_review = proto.Field(
            proto.MESSAGE, number=6, message="Document.Revision.HumanReview",
        )

    class TextChange(proto.Message):
        r"""This message is used for text changes aka. OCR corrections.

        Attributes:
            text_anchor (~.document.Document.TextAnchor):
                Provenance of the correction. Text anchor indexing into the
                [Document.text][google.cloud.documentai.v1beta3.Document.text].
                There can only be a single ``TextAnchor.text_segments``
                element. If the start and end index of the text segment are
                the same, the text change is inserted before that index.
            changed_text (str):
                The text that replaces the text identified in the
                ``text_anchor``.
            provenance (Sequence[~.document.Document.Provenance]):
                The history of this annotation.
        """

        text_anchor = proto.Field(
            proto.MESSAGE, number=1, message="Document.TextAnchor",
        )

        changed_text = proto.Field(proto.STRING, number=2)

        provenance = proto.RepeatedField(
            proto.MESSAGE, number=3, message="Document.Provenance",
        )

    uri = proto.Field(proto.STRING, number=1, oneof="source")

    content = proto.Field(proto.BYTES, number=2, oneof="source")

    mime_type = proto.Field(proto.STRING, number=3)

    text = proto.Field(proto.STRING, number=4)

    text_styles = proto.RepeatedField(proto.MESSAGE, number=5, message=Style,)

    pages = proto.RepeatedField(proto.MESSAGE, number=6, message=Page,)

    entities = proto.RepeatedField(proto.MESSAGE, number=7, message=Entity,)

    entity_relations = proto.RepeatedField(
        proto.MESSAGE, number=8, message=EntityRelation,
    )

    translations = proto.RepeatedField(proto.MESSAGE, number=12, message=Translation,)

    text_changes = proto.RepeatedField(proto.MESSAGE, number=14, message=TextChange,)

    shard_info = proto.Field(proto.MESSAGE, number=9, message=ShardInfo,)

    error = proto.Field(proto.MESSAGE, number=10, message=status.Status,)

    revisions = proto.RepeatedField(proto.MESSAGE, number=13, message=Revision,)


__all__ = tuple(sorted(__protobuf__.manifest))
