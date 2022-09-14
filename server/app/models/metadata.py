from pydantic import BaseModel, validator
from typing import List


class _Attribute(BaseModel):
    trait_type: str
    value: str


class Metadata(BaseModel):
    image: str
    external_url: str
    description: str
    name: str
    attributes: List[_Attribute]
    background_color: str

    @validator('background_color')
    def valid_hexadecimal(cls, v):
        v = v.lstrip('#')
        if len(v) != 6:
            raise ValueError('Background color must be a 6 digit hexadecimal')
        return v
