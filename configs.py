
from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "6478248479:AAGE_WN9bNrtEo9TPiVpkDfvpkVp5EJSNiM")
    FSUB = getenv("FSUB", "TheFunkyGroup")
    CHID = int(getenv("CHID", "-1001596583384"))
    SUDO = list(map(int, getenv("SUDO", "6643862052").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://lostzoro567:luCu7z2IQyIoZ1kR@cluster0.hkq0krw.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
