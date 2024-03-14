"""awel-list-to-string-operator operator package"""

from typing import List
from dbgpt.core.awel import MapOperator
from dbgpt.core.awel.flow import ViewMetadata, OperatorCategory, IOField, Parameter


class ListToStringOperator(MapOperator[List[str], str]):
    metadata = ViewMetadata(
        label="List to String Operator",
        name="list_to_string_operator",
        category=OperatorCategory.COMMON,
        description="Transform a list to a string.",
        parameters=[
            Parameter.build_from(
                "Delimiter",
                "delimiter",
                str,
                optional=True,
                default="\n\n",
                description="The delimiter to join the list of strings. Default is "
                "'\\n\\n'.",
            )
        ],
        inputs=[
            IOField.build_from(
                "Input value",
                "value",
                str,
                is_list=True,
                description="The input value to be transformed to a string.",
            )
        ],
        outputs=[
            IOField.build_from(
                "Output value",
                "value",
                str,
                description="The output value transformed to a string.",
            )
        ]
    )

    def __init__(self, delimiter: str = "\n\n", **kwargs):
        super().__init__(**kwargs)
        self.delimiter = delimiter

    async def map(self, value: List[str]) -> str:
        return self.delimiter.join(value)
