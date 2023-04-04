
# FormulaAnalyzer

The FormulaAnalyzer component is designed to analyze all formulas used in the input workbook, generating a detailed report outlining their purpose and function. By doing so, it provides users with a comprehensive understanding of how the workbook functions and calculates its results. The component processes each formula in the workbook and breaks it down to its constituent elements, providing a thorough explanation for each one. Additionally, it highlights potential issues or optimization opportunities within the formulas, helping users to improve their workbooks' overall efficiency and effectiveness.

## Initial generation prompt
description: A component that analyzes all formulas used in the input workbook, generating
  a detailed report on their purpose and function.
name: FormulaAnalyzer


## Transformer breakdown
- Load the input workbook
- Iterate through each worksheet and cell to identify and extract all formulas
- Analyze and break down each formula into its constituent elements
- Identify potential issues or optimization opportunities in the formulas
- Generate a detailed report with explanations of the formulas and their purpose, including any issues or optimization suggestions
- Convert the report to the specified output format
- Return the generated report as output

## Parameters
[{'name': 'report_format', 'default_value': 'pdf', 'description': "The format in which the report should be generated. Allowed values are 'pdf' and 'txt'.", 'type': 'string'}]

        