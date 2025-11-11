from typing import Collection, List
from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import get_database
from app.martial_arts.dtos.martial_art_dto import MartialArtDto
from app.martial_arts.mappers.martial_art_mapper import MartialArtMapper
from pymongo.database import Database
from app.martial_arts.models.martial_art import MartialArt
from app.core import config

# Creazione del router
router = APIRouter(
    prefix=config.MARTIAL_ARTS_PATH,
    tags=["Martial Arts"]
)

# Iniezione Mapper
martial_art_mapper = MartialArtMapper()

# Get /martial-arts
@router.get(
    "", 
    response_model=List[MartialArtDto], 
    status_code=status.HTTP_200_OK,
    summary="Recupera tutte le arti marziali"
)
async def find_all(db: Database = Depends(get_database)):
    try:
        collection: Collection = db[config.MARTIAL_ARTS_COLL]
        # Recupero dei dati da MongoDB (cursor)
        results = list(collection.find({}))
        # Mapping delle Entities in DTO
        return martial_art_mapper.map_entities_to_dtos([MartialArt(**ma) for ma in results])
    except Exception as e:
        print(f"Errore durante il recupero delle arti marziali: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Errore interno del server."
        )