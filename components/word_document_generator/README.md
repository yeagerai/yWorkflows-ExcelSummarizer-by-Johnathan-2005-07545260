
# WordDocumentGenerator

A component that generates a formal Word document that summarizes the input workbook, includes the formula analysis report, and contains a table of contents and visual aids, allowing the user to customize the format and structure as needed.

## Initial generation prompt
description: A component that generates a formal Word document that summarizes the
  input workbook, includes the formula analysis report, and contains a table of contents
  and visual aids, allowing the user to customize the format and structure as needed.
name: WordDocumentGenerator


## Transformer breakdown
- Initialize a new Word document
- If format_preferences is not empty, apply the custom format
- Else, apply the default_format
- Generate the workbook summary
- Add the workbook summary to the Word document
- Analyze and generate the formula analysis report
- Add the formula analysis report to the Word document
- Loop through the visual_aids list and add each visual aid to the Word document
- Generate and add the table of contents to the Word document, with a maximum depth level set by toc_max_depth
- Return the Word document

## Parameters
[{'name': 'default_format', 'default_value': 'standard', 'description': 'Default format applied to the Word document if no format_preferences are given.', 'type': 'str'}, {'name': 'toc_max_depth', 'default_value': 3, 'description': 'The maximum depth level for the table of contents.', 'type': 'int'}]

        