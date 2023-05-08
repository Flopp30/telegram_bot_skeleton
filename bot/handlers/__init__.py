"""
Register handlers
"""
from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import CommandStart, Command

from bot.handlers.help import help_command, help_func
from bot.handlers.start import start
from bot.middleware import RegisterCheck
from bot.text_for_messages import BOT_COMMANDS_INFO

__all__ = [
    "BOT_COMMANDS_INFO",
    "register_user_commands",
]


def register_user_commands(router: Router) -> None:
    """
    Register user commands
    :param router:
    :return:
    """

    # middleware
    router.message.middleware(RegisterCheck())
    router.callback_query.middleware(RegisterCheck())
    # start
    router.message.register(start, CommandStart())

    # help
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_func, F.text.capitalize() == "Помощь")
