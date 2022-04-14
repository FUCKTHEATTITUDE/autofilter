import logging
import pickle
from os import execl, path, remove
from sys import executable
from pyrogram import Client , filters
from telethon.events import NewMessage

from info import OWNER

logger = logging.getLogger(__name__)

if path.exists('restart.pickle'):
    with open('restart.pickle', 'rb') as status:
        chat, msg_id = pickle.load(status)
    bot.loop.run_until_complete(bot.edit_message(
        chat, msg_id, "Restarted Successfully!"))
    remove('restart.pickle')


@Client.on_message(NewMessage & filters.command('restart') & filters.user(OWNER))
async def restart(event):
    restart_message = await event.reply("Restarting, Please wait!")
    with open('restart.pickle', 'wb') as status:
        pickle.dump([event.chat_id, restart_message.id], status)
    logger.info('Restarting Rashmika')
    execl(executable, executable,  "start.sh")
