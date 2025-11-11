from app.martial_arts.dtos.martial_art_dto import MartialArtDto
from app.martial_arts.models.martial_art import MartialArt, PyObjectId
from app.utils.mapper import AbstractMapper


class MartialArtMapper(AbstractMapper[MartialArt, MartialArtDto]):
    def map_entity_to_dto(self, entity: MartialArt) -> MartialArtDto:
        return None if entity is None else MartialArtDto(
            id=str(entity.id), 
            name=entity.name, 
            focus=entity.focus, 
            description=entity.description, 
            imageUrl=entity.imageUrl
        )

    def map_dto_to_entity(self, dto: MartialArtDto) -> MartialArt: 
        return None if dto is None else MartialArt(
            _id=PyObjectId(dto.id) if dto.id else None, 
            name=dto.name, 
            focus=dto.focus, 
            description=dto.description, 
            imageUrl=dto.imageUrl
        )