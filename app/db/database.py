from pymongo import MongoClient
from pymongo.database import Database
from app.core import config

# Variabili globali per client e database
client: MongoClient = None
db: Database = None

# Inizializza la connessione
def init_db():
    """Inizializza il DB"""
    global client, db
    
    # Se il client è già inizializzato, non eseguire
    if client is not None:
        return 

    try:
        client = MongoClient(config.MONGODB_URI)
        db = client.get_database(config.MONGODB_NAME)

        # Verifica ping per assicurarsi che il server sia raggiungibile
        client.admin.command('ping') 
        print(f"Connessione a MongoDB ({config.MONGODB_NAME}) stabilita con successo!")
    except Exception as e:
        print("Error: " + e)

# Recupera il riferimento a DB
def get_database() -> Database:
    """Restituisce l'istanza globale del database."""
    if db is None:
        initialize_db()
    return db

# Chiusura del client
def close_db_client():
    """Chiude il client MongoDB."""
    global client
    if client:
        client.close()
        print("Connessione a MongoDB chiusa.")