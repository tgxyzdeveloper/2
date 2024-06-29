import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24491383"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "78e18eba669cc519ffd7a3c89f9ed32a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://cogat14114:cogat14114@cluster0.amcrvsn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
