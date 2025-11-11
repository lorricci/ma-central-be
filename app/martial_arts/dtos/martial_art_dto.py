from pydantic import BaseModel

class MartialArtDto(BaseModel):
    id: str
    name: str
    focus: str
    description: str
    imageUrl: str