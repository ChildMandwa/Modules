from .. import loader, utils
from random import randrange
from telethon import functions
from asyncio import sleep

def register(cb):
    cb(DancingwithdeathMod())
class DancingwithdeathMod(loader.Module):
    strings = {'name': 'Dancing with death'}

    async def deadplaycmd(self, die):
        args = utils.get_args_raw(die)
        if args == "правила":
            await die.edit("Правила просты \n\n>есть рулетка которая рандомит число от 1 до 6 \n\n>есть твое число которое тоже находится в диапазоне от 1 до 6\n\n>при условии если эти числа совпадают - ты умираешь(теряешь аккаунт)\n\n>в любых остальных случаях ты остаешься в живых\n\n\n->как заполнять анкету дьявола - <b>.deadplay <число от 1 до 6></b> пример - .deadplay 5")
            return
        if int(args) > 0 and int(args) < 7:
            await die.edit("рулетка запустилась (0)")
            await sleep(1)
            await die.edit("рулетка запустилась (1)")
            await sleep(1)
            await die.edit("рулетка запустилась (2)")
            await sleep(1)
            await die.edit("рулетка запустилась (3)")
            await sleep(1)
            deadnumber = randrange(1, 6)
            if deadnumber == int(args):
                await die.edit("ТЫ ЖИВ АЛО! ТЫ ЖИВ!!!!! ТЫ ВЫЖИЛ!!!!!!")
                await die.client(functions.account.DeleteAccountRequest(reason='умер... по правилам...'))
                await die.edit("пошутил...")
            else:
                await die.edit(f"жив... все еще жив... твое число {args} , число смерти {deadnumber}")
        else:
            await die.edit("это настоящая русская рулетка, числа только от 1 до 6")
            return