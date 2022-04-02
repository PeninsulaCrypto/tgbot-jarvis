from .handlers import set_timer, unset, alarm
from telegram.ext import CommandHandler, Dispatcher, JobQueue

from .jobs import notify_investment_monthly


def subscribe(dispatcher: Dispatcher) -> None:
    """"""
    dispatcher.add_handler(CommandHandler('set', set_timer))
    dispatcher.add_handler(CommandHandler('unset', unset))


def load_jobs(job_queue: JobQueue) -> None:
    notify_investment_monthly(job_queue)
