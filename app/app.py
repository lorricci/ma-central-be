from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import martial_arts_api
from app.db.database import close_db_client, init_db
from app.core import config

# --- Gestore del Ciclo di Vita (Lifespan Handler) ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestisce il ciclo di vita dell'applicazione"""
    # [STARTUP LOGIC]
    print("Avvio connessione al db...")
    init_db()
    
    yield # L'applicazione inizia a servire il traffico qui
    
    # [SHUTDOWN LOGIC]
    print("Chiusura del db...")
    close_db_client()

application = FastAPI(title="Martial Arts Central", lifespan=lifespan)

# --- Registrazione del Router ---

# /api/v1/martial_arts
application.include_router(martial_arts_api.router, prefix=config.CONTEXT_PATH)

@application.get("/")
def read_root():
    return {"message": "Benvenuto nell'API delle Arti Marziali"}