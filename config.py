import os
API_ID = int(os.getenv("28257754"))
API_HASH = os.getenv("ed1a012ea309aaf00295a2e4e33d7902")
BOT_TOKEN = os.getenv("5760189520:AAGayg21HUnse4QNuhVdJR3AMDth2dgS3Yo")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("1536628714", "").split()})
