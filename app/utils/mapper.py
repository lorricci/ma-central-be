from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

# Definizione dei generics
E = TypeVar('E') # Tipo entità
D = TypeVar('D') # Tipo DTO

class AbstractMapper(ABC, Generic[E, D]):

    # --- Metodi astratti - Mapping --- 
    @abstractmethod
    def map_entity_to_dto(self, entity: E) -> D: 
        pass

    @abstractmethod
    def map_dto_to_entity(self, dto: D) -> E: 
        pass

    # --- Metodi Default - Mapping Liste
    def map_entities_to_dtos(self, entities: List[E]) -> List[D]:
        return list(map(self.map_entity_to_dto, entities))
    
    def map_dtos_to_entities(self, dtos: List[D]) -> List[E]:
        return list(map(self.map_dto_to_entity, dtos))