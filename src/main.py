
#%%
import logging
import hashlib
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)


API_TOKEN = 'col cazzo che ti do il token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# %%

msg = {'uno' : 'questa cosa la scrivo perchè hai cliccato uno ',
             'due' : 'questa cosa la scrivo perchè hai cliccato due ',
             'tre' : 'questa cosa la scrivo perchè hai cliccato tre ',}


btns = [KeyboardButton(btn) for btn in msg.keys()]


tastiera_custom = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tastiera_custom.add(btns[0]).add(btns[1]).add(btns[2])


## this function is called when the user send /start or /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("ciao amico scegli un numero da 1 a 3", reply_markup=tastiera_custom)




@dp.message_handler()
async def echo(message: types.Message):
    try:
        await message.reply(msg[message.text])
    except:
        await message.reply("non ho capito cosa vuoi dire")



#%%
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
# %%



# %%
