
import os
import openpyxl
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import yaml

from core.abstract_component import AbstractComponent


class FormulaAnalyzerInputDict(BaseModel):
    input_workbook: bytes


class FormulaAnalyzerOutputDict(BaseModel):
    formula_report: str


class FormulaAnalyzer(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.report_format: Optional[str] = yaml_data["parameters"]["report_format"]
        self.output = ""

    def transform(
        self, args: FormulaAnalyzerInputDict
    ) -> FormulaAnalyzerOutputDict:
        with open("tmp_workbook.xlsx", "wb") as f:
            f.write(args.input_workbook)

        wb = openpyxl.load_workbook("tmp_workbook.xlsx")
        
        formula_report = ""

        # Iterate through each worksheet and cell
        for sheet in wb:
            for row in sheet.iter_rows():
                for cell in row:

                    # Identify and extract formulas
                    if cell.data_type == "f":
                        formula = cell.value

                        # Analyze and break down the formula
                        analyzed_formula = ""  # Placeholder for analyzed formula information
                        
                        # Identify issues or optimization opportunities
                        issues_and_suggestions = ""  # Placeholder for issues and suggestions

                        # Generate report entry
                        entry = (
                            f"Cell: {cell.coordinate}, "
                            f"Formula: {formula}, "
                            f"Analyzed Formula: {analyzed_formula}, "
                            f"Issues and Suggestions: {issues_and_suggestions}\n"
                        )

                        # Append entry to the formula report
                        formula_report += entry
        
        # Convert the report to the specified output format
        if self.report_format == "pdf":
            # Placeholder for converting report into a pdf format
            formula_report = f"PDF: {formula_report}"
        elif self.report_format == "txt":
            # Placeholder for converting report into a txt format
            formula_report = f"TXT: {formula_report}"

        # Return the generated report as output
        out = FormulaAnalyzerOutputDict(formula_report=formula_report)

        return out


load_dotenv()
formula_analyzer_app = FastAPI()


@formula_analyzer_app.post("/transform/")
async def transform(
    args: FormulaAnalyzerInputDict,
) -> FormulaAnalyzerOutputDict:
    formula_analyzer = FormulaAnalyzer()
    return formula_analyzer.transform(args)
