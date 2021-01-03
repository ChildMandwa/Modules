import telethon
#from telethon.client import get_input_chat_photo
from .. import loader, utils
from telethon.sync import TelegramClient
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from datetime import datetime
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest


def register(cb):
    cb(SkolkoMod())

class SkolkoMod(loader.Module):
    """Согласен"""
    strings = {'name': 'Сколько раз блять тебе обьяснять'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def chatinfocmd(self, event):
        await event.edit("<b>Загрузка информации...</b>")
        photo = event.client.get_input_peer(event.to_id)
        #chat = await get_chatinfo(chatinfo)
        #caption = await fetch_info(chat, chatinfo)
        #try:
        await event.client.send_file(event.to_id, photo)
        #except Exception:


#def chatphoto(event):
    #photo = event.client.get_input_channel(get_input_peer(event.to_id))
    # photos = telethon.utils.get_input_peer(chat)
    # send_photos = await event.client.download_media(photos[1])
    # await event.client.send_file(event.chat_id, send_photos)
   # return photo
