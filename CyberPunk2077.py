#By CyberClown
from .. import loader, utils
import requests
from PIL import Image, ImageDraw, ImageFont
import io
from textwrap import wrap
def register(cb):
    cb(CyberGenMod())
class CyberGenMod(loader.Module):
    strings = {'name': 'Киберпанк генератор',
               'noargs': 'нет аргументов.'}
    async def cybercmd(self, event):
        """.cyber <текст/реплай на текст>"""
        args = utils.get_args_raw(event)
        reply = await event.get_reply_message()
        if not reply and not args:
            return await event.edit(self.strings('noargs', event))
        if reply:
            txt = reply.text
        else:
            txt = args
        pic = requests.get("https://github.com/SpyderJabro/SpYD3R/raw/master/img/cyberpunk-blank.jpeg")
        pic.raw.decode_content = True
        img = Image.open(io.BytesIO(pic.content)).convert("RGB")
        W, H = img.size
        ufr = requests.get("https://github.com/SpyderJabro/SpYD3R/raw/master/modul/BlenderPro-MediumItalic.ttf")
        f = ufr.content
        t = txt
        t = t.replace("𓃐", "\n")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(io.BytesIO(f), 52, encoding='UTF-8')
        w, h = draw.multiline_textsize(t, font=font)
        imtext = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
        draw = ImageDraw.Draw(imtext)
        draw.multiline_text((0, 0), t, (0, 0, 0), font=font)
        imtext.thumbnail((W, H))
        img.paste(imtext, (W // 15, H // 5), imtext)
        out = io.BytesIO()
        out.name = "ясосУспая.jpg"
        img.save(out)
        out.seek(0)
        await event.client.send_file(event.to_id, out)
        await event.delete()