
import os
from typing import Optional

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class Workbook(BaseModel):
    content: str


class Summary(BaseModel):
    text: str
    visual_aids: list


class WorkbookSummaryGeneratorInputDict(BaseModel):
    input_workbook: Workbook
    nlp_algorithm: Optional[str] = "bert"
    summary_length: Optional[int] = 300
    visualization_type: Optional[str] = "bar_chart"


class WorkbookSummaryGeneratorOutputDict(BaseModel):
    summary: Summary


class WorkbookSummaryGenerator(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

    def transform(
        self, args: WorkbookSummaryGeneratorInputDict
    ) -> WorkbookSummaryGeneratorOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Load input_workbook and parameters
        input_workbook = args.input_workbook
        nlp_algorithm = args.nlp_algorithm
        summary_length = args.summary_length
        visualization_type = args.visualization_type

        # Extract textual and numerical data from the input_workbook
        # Process textual data using the specified NLP algorithm (e.g., bert)
        # Identify key insights and relevant information

        # Generate summary based on the extracted insights and summary_length parameter
        text_summary = "Some generated summary based on the input workbook and parameters."

        # Create visual aids (e.g., graphs, charts) based on the specified visualization_type parameter
        visual_aids = []

        # Combine summary and visual aids into a comprehensive output
        summary = Summary(text=text_summary, visual_aids=visual_aids)

        # Return the generated summary
        return WorkbookSummaryGeneratorOutputDict(summary=summary)


load_dotenv()
workbook_summary_gen_app = FastAPI()


@workbook_summary_gen_app.post("/transform/")
async def transform(
    args: WorkbookSummaryGeneratorInputDict,
) -> WorkbookSummaryGeneratorOutputDict:
    workbook_summary_gen = WorkbookSummaryGenerator()
    return workbook_summary_gen.transform(args)

