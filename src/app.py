import logging
from dotenv import load_dotenv, dotenv_values
from timer_event import enable_timer_event_updater

load_dotenv()
app_config = dotenv_values(".env")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('jarvis')


def main():
    """Run the bot"""
    # create timer event updater
    updater = enable_timer_event_updater(app_config.get('TOKEN'))
    logger.info(msg='Jarvis started successfully')

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
    logger.info(msg='Jarvis is shutted down')


if __name__ == '__main__':
    main()
