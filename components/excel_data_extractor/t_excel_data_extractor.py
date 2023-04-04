
# test_excel_data_extractor.py

import pytest
import openpyxl
from pydantic import BaseModel
from fastapi.testclient import TestClient

from .excel_data_extractor import ExcelDataExtractor, ExcelDataExtractorInputDict, ExcelDataExtractorOutputDict, excel_data_extractor_app

client = TestClient(excel_data_extractor_app)

@pytest.fixture
def sample_workbook():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Sample Sheet"
    sheet.append(["ID", "Name", "Age"])
    sheet.append([1, "John Doe", 30])
    sheet.append([2, "Jane Doe", 25])
    workbook.save("sample_workbook.xlsx")

@pytest.mark.parametrize("input_data,expected_output", [
    (
        ExcelDataExtractorInputDict(input_workbook="sample_workbook.xlsx"),
        ExcelDataExtractorOutputDict(results={"Sample Sheet": [["ID", "Name", "Age"], [1, "John Doe", 30], [2, "Jane Doe", 25]]}),
    )
])
def test_excel_data_extractor(sample_workbook, input_data, expected_output):
    excel_data_extractor = ExcelDataExtractor()
    output = excel_data_extractor.transform(input_data)
    assert output == expected_output

@pytest.mark.parametrize("input_data,expected_output", [
    (
        {"input_workbook": "sample_workbook.xlsx"},
        {"results": {"Sample Sheet": [["ID", "Name", "Age"], [1, "John Doe", 30], [2, "Jane Doe", 25]]}},
    )
])  
def test_excel_data_extractor_app(sample_workbook, input_data, expected_output):
    response = client.post("/transform/", json=input_data)
    assert response.status_code == 200
    assert response.json() == expected_output
