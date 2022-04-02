import logging

from telegram import Update
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, CallbackQueryHandler

from jarvis import timer_event
from jarvis.constants import MENU_CMD_LIST_JOBS
from jarvis.handlers import start, help, list_all_jobs
from jarvis.utils.conversation import say
from jarvis.utils.menu import build_menu

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('jarvis')


def callback_query_handler(update: Update, context: CallbackContext) -> None:
    command: str = update.callback_query.data
    if command == MENU_CMD_LIST_JOBS:
        list_all_jobs(update, context)


def main(app_config: dict):
    """Run the bot"""
    updater = Updater(token=app_config.get('TOKEN'))
    dispatcher: Dispatcher = updater.dispatcher

    # register event handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))
    timer_event.subscribe(dispatcher)

    # load jobs
    timer_event.load_jobs(updater.job_queue)

    print(updater.job_queue.jobs())

    logger.info(msg='Jarvis started successfully')
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
    logger.info(msg='Jarvis is shut down')
