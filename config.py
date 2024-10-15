import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7673403548:AAEJau7jPtMUewQK21briuobAUv7_euYbFI")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24491383"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "78e18eba669cc519ffd7a3c89f9ed32a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mrrajib536:LoQ9PPjcRRgnQXFj@cluster0.svhwzos.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
