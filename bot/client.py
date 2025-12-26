from pyrogram import Client
from config.config import *

def create_client():
    return Client(
        SESSION_NAME,
        api_id=API_ID,
        api_hash=API_HASH,
        workdir="sessions",
        #proxy= {
        #"scheme": "mtproto",
        #"hostname": "xn--digikala-5r45g.pianmusic.ir",
        #"port": 18189,
        #"secret": "eeNEgYdJvXrFGRMCIMJdCQ"
        #}

    )
