
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class ExcelInputModel(BaseModel):
    file: bytes


class WordOutputModel(BaseModel):
    file: bytes


class ExcelSummarizer(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ExcelInputModel, callbacks: typing.Any
    ) -> WordOutputModel:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        # Extract the relevant outputs from the results_dict for your workflow
        # and perform any required post-processing or data manipulation.
        word_output = results_dict['your_key'].word_output

        out = WordOutputModel(
            file=word_output
        )
        return out

load_dotenv()
excel_summarizer_app = FastAPI()

@excel_summarizer_app.post("/transform/")
async def transform(
    args: ExcelInputModel,
) -> WordOutputModel:
    excel_summarizer = ExcelSummarizer()
    return await excel_summarizer.transform(args, callbacks=None)

