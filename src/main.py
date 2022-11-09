
#%%
import logging
import hashlib
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
print(TOKEN)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# %%

msg = {'INFO GENERALI' : "🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n         INFO GENERALI\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nLunedì 31 Ottobre\nOrario: dalle 10.30 alle 4.30\n\nPrezzo uomo: 20€\nPrezzo donna: 15€\n\nL'ingresso é consentito esclusivamente con iscrizione in lista, e include l'OPEN BAR dalle ore 10.30 alle ore 2.00.\n\nEcc Ecc.. porca merdaaaaaaa",
             'LOCATION' : '🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n             LOCATION\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nNuova Location: NoSpace Club, Via Vergnano 65, Brescia\n\n https://maps.app.goo.gl/34daiXjMFQM5x8aB7 \n\nMolto figo e accogliente, adatto alle famiglie.',
             'MUSICA' : '🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n                MUSICA\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nProgramma della serata:\n\nDalle 10.30 alle 00.00: House/commerciale -> Dj Trilly\nDalle 00.00 alle 2.00: Salsa e bachata -> Dj Gonzales El Gonzo\nDalle 2.00 alle 4.30: Tecno e pasticche -> Dj SeNonTiDroghiFaiSchifo',
             'DRINK OPEN BAR':"🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n        DRINK OPEN BAR\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nDrinks:\n\nAcqua\nAcqua Frizzante\nAqua\nAqua Con Gas",
             'TAVOLI':"🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n                TAVOLI\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nTavoli disponibili:\n\nTavolo1..\n\nTavolo 2\n\nSi dai avete capito non ho sbatta ah no basta copiare e incollare\n\nBASE:\n150 (5 ingressi) —> include 1 bottiglia base + open bar per tutta la durata dell'evento\n300 (10 ingressi) —> include 2 bottiglie base + open bar per tutta la durata dell'evento\n\nPREMIUM:\n200 (5 ingressi) —> include 1 bottiglia premium (belvedere/hendrick's) + open bar per tutta la durata dell'evento\n400 (10 ingressi) —> include 2 bottiglie premium  (belvedere/hendrick's) + open bar per tutta la durata dell'evento\n\nVIP:\n250 (5 ingressi) —> include 1 bottiglia premium (belvedere/hendrick's) e 1 spumante  + open bar per tutta la durata dell'evento\n500 (10 ingressi) —> include 2 bottiglie premium  (belvedere/hendrick's) e 2 spumanti + open bar per tutta la durata dell'evento",
             'ISCRIZIONE IN LISTA':"🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n     ISCRIZIONE IN LISTA\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nSi va bene tutto, però quanto cazzo è bello Dema??!?",
             'CHI SIAMO':"🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n             CHI SIAMO\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\nSisi ma io capisco tutto, però non ho piu sbatta\n\nComunque\n\nDema è proprio un toro ma minchia proprio un torotoro fessssss",}


btns = [KeyboardButton(btn) for btn in msg.keys()]


tastiera_custom = ReplyKeyboardMarkup(resize_keyboard=True)
tastiera_custom.add(*btns)


## this function is called when the user send /start or /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Bella raga!\nQua direi tipo qua potete trovare tutte le info che vi servono per la 'Prossima Festa Trilogy Cazzo'!\nClicca sul bottone per avere tutte le info dettagliate su:\n\nInfo Generali\nLocation \nMusica \nDrink Open Bar \nTavoli \nCome aggiungersi in lista \nChi siamo", reply_markup=tastiera_custom)




@dp.message_handler()
async def echo(message: types.Message):
    try:
        await message.reply(msg[message.text])
    except:
        await message.reply("Non ho capito cosa cazzo vuoi dire brutto minchioneoneone")



#%%
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
# %%



# %%
