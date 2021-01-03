from .. import loader, utils
from requests import get
from io import BytesIO
from random import randint, choice
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap

class AmongUsMod(loader.Module):
    strings = {
        "name": "shark"
    }
    async def client_ready(self, client, db):
        self.client = client
    @loader.owner
    async def sharkcmd(self, message):
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not text:
            if not reply:
                
                return
            if not reply.text:
                
                return
            text = reply.raw_text
  
        
        url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
        font = ImageFont.truetype(BytesIO(get(url+"bold.ttf").content), 60)
        shark = Image.open(BytesIO(get(f"https://telegra.ph/file/cc1cdd7961734ab0c4707.png").content))
        text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
        w, h = ImageDraw.Draw(Image.new("RGB", (1,1))).multiline_textsize(text_, font, stroke_width=5)
        text = Image.new("RGBA", (w+30, h+30))
        ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=5, stroke_fill="#000", align="center")
        w = shark.width
        h = shark.height+ text.height+30
        image = Image.new("RGBA", (w, h))
        text.thumbnail((shark.width, 9999))
        image.paste(shark, (0, 0), shark)
        image.paste(text, ((shark.width-text.width)//2, shark.height-10), text)
        image.thumbnail((512, 512))
        output = BytesIO()
        output.name = "shark.webp"
        image.save(output)
        output.seek(0)
        await message.delete()
        await message.client.send_file(message.to_id, output, reply_to=reply)