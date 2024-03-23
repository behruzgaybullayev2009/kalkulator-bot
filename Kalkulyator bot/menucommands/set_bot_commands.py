from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Yordam"),
        BotCommand(command="/about", description="calculyator haqida ma'lumot"),
        BotCommand(command="/admin", description="foydalanuvchilar soni va reklama yunborish button"),
        BotCommand(command="/calc", description="Calculyatorni ishga tushiradi"),
        BotCommand(command="/admins", description="adminlar bilan bog'lanish")


    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())