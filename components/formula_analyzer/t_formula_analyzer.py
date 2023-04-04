
# Import necessary libraries for testing
import pytest
import openpyxl
from fastapi.testclient import TestClient
from pydantic import ValidationError
from base64 import b64encode

# Import the Yeager component to be tested
from component_directory.component_name import (
    FormulaAnalyzer,
    FormulaAnalyzerInputDict,
    FormulaAnalyzerOutputDict,
)

# Initialize test client
client = TestClient(formula_analyzer_app)

# Define mocked test cases
test_cases = [
    (
        b64encode(b"Dummy workbook bytes"),
        {"report_format": "pdf"},
        "PDF: Cell: A1, Formula: =SUM(A1:A5), Analyzed Formula: , Issues and Suggestions:\n",
    ),
    (
        b64encode(b"Dummy workbook bytes"),
        {"report_format": "txt"},
        "TXT: Cell: A1, Formula: =SUM(A1:A5), Analyzed Formula: , Issues and Suggestions:\n",
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_workbook, yaml_parameters, expected_formula_report", test_cases)
def test_formula_analyzer(input_workbook, yaml_parameters, expected_formula_report):

    # Mock component configuration (yaml)
    with open("component_directory/component_name/configuration.yml", "w") as config:
        config.write(yaml.dump(yaml_parameters))

    # Instantiate the component and test the transform method
    try:
        input_dict = FormulaAnalyzerInputDict(input_workbook=input_workbook)
        formula_analyzer = FormulaAnalyzer()
        output_dict = formula_analyzer.transform(input_dict)

    # Check for ValidationError exceptions (if applicable)
    except ValidationError as error:
        pytest.fail(f"ValidationError occurred: {error}")

    # Assert that the output matches the expected output
    assert output_dict.formula_report == expected_formula_report

    # Cleanup the mocked configuration file
    os.remove("component_directory/component_name/configuration.yml")
