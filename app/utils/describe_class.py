from typing import Any, Dict, List, Type, Union, get_args, get_origin
from pydantic import BaseModel
from pydantic.fields import FieldInfo

#Consider adding constraint mapping as well. This looks possible but need to sort through all the typing implications.
#My previous thought was using a FieldContraints class as a custom extension of Field for use when defining the model. This has some promise.

def describe_class(cls: Type[BaseModel]) -> str:
    def describe_fields(fields: Dict[str, FieldInfo], indent: str = "") -> str:
        description: List[str] = []
        for name, field in fields.items():
            annotation = field.annotation
            if annotation is not None:
                field_type: str = describe_type(annotation)
                if hasattr(annotation, '__fields__'):
                    nested_description: str = describe_fields(annotation.__fields__, indent + "  ")
                    description.append(f"{indent}{name}: {field_type}\n{nested_description}")
                else:
                    description.append(f"{indent}{name}: {field_type}")
            else:
                description.append(f"{indent}{name}: Unknown Type")
        return "\n".join(description)

    def describe_type(annotation: Any) -> str:
        origin = get_origin(annotation)
        args = get_args(annotation)
        
        if origin is None:
            if hasattr(annotation, '__fields__'):
                # Recursively describe the nested model
                nested_description: str = describe_fields(annotation.__fields__, indent="  ")
                return f"{annotation.__name__}\n{nested_description}"
            return annotation.__name__
        elif origin is list:
            return f"List[{describe_type(args[0])}]"
        elif origin is dict:
            return f"Dict[{describe_type(args[0])}, {describe_type(args[1])}]"
        elif origin is Union and type(None) in args:  # Handle Optional[X]
            non_none_type = next(arg for arg in args if arg is not type(None))
            return f"Optional[{describe_type(non_none_type)}]"
        else:
            return str(annotation)

    return describe_fields(cls.model_fields)



