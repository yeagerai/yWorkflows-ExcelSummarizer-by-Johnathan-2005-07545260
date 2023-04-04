
import pytest
from core.word_document_generator import WordDocumentGenerator, WordDocumentGeneratorInputDict, WordDocumentGeneratorOutputDict
from unittest.mock import MagicMock

# Define test cases with mocked input and expected output data
test_data = [
    (
        WordDocumentGeneratorInputDict(
            workbook=MagicMock(),
            visual_aids=[MagicMock(), MagicMock()],
            format_preferences={"custom_format_key": "custom_format_value"},
        ),
        WordDocumentGeneratorOutputDict(
            word_document=MagicMock()
        ),
    ),
    (
        WordDocumentGeneratorInputDict(
            workbook=MagicMock(),
            visual_aids=[MagicMock()],
            format_preferences=None,
        ),
        WordDocumentGeneratorOutputDict(
            word_document=MagicMock()
        ),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_transform(input_data, expected_output):
    # Instantiate the WordDocumentGenerator component
    word_doc_gen = WordDocumentGenerator()

    # Call the component's transform() method with the mocked input
    result = word_doc_gen.transform(input_data)

    # Assert that the output matches the expected output
    # Note: Since docx.Document() returns a new instance every time, we cannot compare the instances directly
    # Instead, we can compare specific attributes or content of the output document
    assert isinstance(result, WordDocumentGeneratorOutputDict)
    # Add any other applicable assertions to test the content/values of the generated word_document

# Include additional tests for error handling and edge case scenarios, if applicable
def test_transform_with_empty_input():
    word_doc_gen = WordDocumentGenerator()

    with pytest.raises(ValueError):  # Assuming the component raises a ValueError for empty input
        word_doc_gen.transform(WordDocumentGeneratorInputDict(workbook=None, visual_aids=None, format_preferences=None))
