from .. import loader, utils
import requests
from random import choice as morgenchoicer
import io
def register(cb):
    cb(MorgenMod())
class MorgenMod(loader.Module):
    strings = {'name': 'Morgen Mood'}
    async def morgcmd(self, event):
        """Рандомизатор треков моргена.\n\nчтобы глянуть список треков в бд пропишите .morg list\n\nчтобы вывести определенный трек пропишите .morg <айди трека>"""
        donttouch = ''
        inter = 0
        try:
            data = requests.get('https://github.com/ChildMandwa/Modules/raw/main/morgenlol.json').json()
        except:
            return await event.edit("<b>база либо недоступна, либо обновляется.</b>")
        if utils.get_args_raw(event):
            args = utils.get_args_raw(event)
            if args.isdigit():
                args = int(args) - 1
                if args == 16:
                    await event.edit("этот трек можно выбить только рандомом. откисай.")
                    return
                try:
                    morgenlive = data['morgens'][int(args)]['morgenmood']
                except:
                    await event.edit("<b>трека под таким айди нет. долбоеб. пропиши в качестве аргумента слово</b> <code>list</code>")
                    return
            elif args == "list":
                for i in data['morgens']:
                    inter += 1
                    more = i["morgenmood"]
                    donttouch += f"{inter}) {more['name']} \n"
                await event.edit(donttouch)
                return
            else:
                await event.edit("это не число. клоун. чтобы выбрать трек по номеру укажи айди трека.")
                return
        else:
            morgenlive = morgenchoicer(data['morgens'])['morgenmood']
        await event.edit("<b>щас морген придет. жди.</b>")
        try:
            req = requests.get(morgenlive["link"])
        except:
            return await event.edit("<b>данный трек еще не был залит в базу данных.</b>\n\nожидай уебище")
        morgen = io.BytesIO(req.content)
        morgen.name = morgenlive["name"] + ".mp3"
        morgen.seek(0)
        await event.edit("<b>морген реально крутой.</b>")
        await event.client.send_file(event.to_id, morgen)
        await event.delete()



    

