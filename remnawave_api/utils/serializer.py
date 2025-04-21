from pydantic import BaseModel


def orjson_default(obj):
    if isinstance(obj, BaseModel):
        return obj.model_dump(mode="json", exclude_none=True, by_alias=True)
    return obj
