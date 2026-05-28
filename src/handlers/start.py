from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

start_router = Router()

@start_router.message(CommandStart())
async def start_cmd(message: Message) -> None:
    await message.answer("Welcome to <b>Habit tracker</b> bot\n\n I will try to help you to improve your life", parse_mode="HTML")

