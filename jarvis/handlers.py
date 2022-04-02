# -*- coding: utf-8 -*-
"""handlers

Descriptions...
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from jarvis.utils.menu import build_menu
from jarvis.constants import MENU_CMD_LIST_JOBS
from jarvis.utils.conversation import say


def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""
    button_list = [
        InlineKeyboardButton("List all jobs", callback_data=MENU_CMD_LIST_JOBS),
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    context.bot.send_message(update.message.chat_id, say("At your service"), reply_markup=reply_markup)


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(say('There is nothing here. I need time to evolve'))


def list_all_jobs(update: Update, context: CallbackContext):
    jobs = context.job_queue.jobs()
    text = say("Found all active jobs")
    for job in jobs:
        text += "\n - name: {}".format(job.name)
    context.bot.send_message(update.callback_query.message.chat.id, text)
