
import pytest
from pydantic import ValidationError
from core.workbook_summary_generator import (
    WorkbookSummaryGenerator,
    WorkbookSummaryGeneratorInputDict,
    WorkbookSummaryGeneratorOutputDict,
    Workbook,
    Summary,
)

# Mocked data for test cases
test_data = [
    # Test case 1: Basic input
    {
        "input": WorkbookSummaryGeneratorInputDict(
            input_workbook=Workbook(content="Sample workbook content"),
            nlp_algorithm="bert",
            summary_length=300,
            visualization_type="bar_chart",
        ),
        "output": WorkbookSummaryGeneratorOutputDict(
            summary=Summary(
                text="Some generated summary based on the input workbook and parameters.",
                visual_aids=[],
            )
        ),
    },
    # Test case 2: Different input workbook
    {
        "input": WorkbookSummaryGeneratorInputDict(
            input_workbook=Workbook(content="Different workbook content"),
            nlp_algorithm="bert",
            summary_length=300,
            visualization_type="bar_chart",
        ),
        "output": WorkbookSummaryGeneratorOutputDict(
            summary=Summary(
                text="Some generated summary based on the input workbook and parameters.",
                visual_aids=[],
            )
        ),
    },
]

@pytest.mark.parametrize("test_input, expected_output", test_data)
def test_workbook_summary_generator_transform(test_input, expected_output):
    
    # Create a WorkbookSummaryGenerator instance and call the transform method with the test input data
    workbook_summary_gen = WorkbookSummaryGenerator()
    result = workbook_summary_gen.transform(test_input)

    # Assert that the output matches the expected output
    assert result == expected_output

def test_invalid_input():

    # Test the case when the input is an invalid instance of WorkbookSummaryGeneratorInputDict
    with pytest.raises(ValidationError):
        invalid_input = WorkbookSummaryGeneratorInputDict(
            input_workbook="Invalid workbook content",  # input_workbook should be an instance of Workbook
            nlp_algorithm="bert",
            summary_length=300,
            visualization_type="bar_chart",
        )
