
import os
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import openpyxl

from core.abstract_component import AbstractComponent

class ExcelDataExtractorInputDict(BaseModel):
    input_workbook: str

class ExcelDataExtractorOutputDict(BaseModel):
    results: dict

class ExcelDataExtractor(AbstractComponent):
    def __init__(self):
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["api_key"]
        )

    def transform(self, args: ExcelDataExtractorInputDict) -> ExcelDataExtractorOutputDict:
        
        # Step 1: Read the input Excel workbook
        workbook = openpyxl.load_workbook(args.input_workbook)

        # Step 2 & 3: Connect to the Excel API or other data source using the provided api_key and analyze the data
        # (Replace this step with the code for your actual data source and processing logic)

        processed_data = {}
        for sheet in workbook:
            sheet_data = []
            for row in sheet.rows:
                row_data = [cell.value for cell in row]
                processed_data(sheet.title) = row_data

        # Step 4: Return the results in a structured format (dictionary)
        output = ExcelDataExtractorOutputDict(results=processed_data)
        return output

load_dotenv()
excel_data_extractor_app = FastAPI()

@excel_data_extractor_app.post("/transform/")
async def transform(args: ExcelDataExtractorInputDict) -> ExcelDataExtractorOutputDict:
    excel_data_extractor = ExcelDataExtractor()
    return excel_data_extractor.transform(args)
