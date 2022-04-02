# -*- coding: utf-8 -*-
"""jobs

Descriptions...
"""
from datetime import datetime, time

from telegram.ext import CallbackContext, JobQueue

from jarvis.constants import tz_shanghai, TG_CHAT_ID_PENIN_CORE


def notify_investment_monthly(job_queue: JobQueue):
    def notification(context: CallbackContext) -> None:
        job = context.job
        dt = tz_shanghai.localize(datetime.now())
        text = "Sir, it's time to invest cryptocurrencies! New month starts, LFG! ({dt})".format(
            dt=dt.strftime('%Y/%m/%d'))
        context.bot.send_message(job.context.chat_id, text=text)

    chat_id = TG_CHAT_ID_PENIN_CORE
    timing = time(hour=9, minute=0, tzinfo=tz_shanghai)
    job_queue.run_monthly(notification, day=1,
                          when=timing,
                          context=dict(chat_id=chat_id),
                          name=notify_investment_monthly.__name__)
