from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.users.states import RegState
from aiogram.fsm.context import FSMContext


from app.users.dao import UsersDao

users_router = Router()

@users_router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext) -> None:
    user = await UsersDao.find_one_or_none(tg_id=message.from_user.id)
    if user:
        await message.answer("Wellcome back! I'm habits bot")
        return
    
    await message.answer("Hello I'm habit bot. Whats your name")
    await state.set_state(RegState.username)

@users_router.message(RegState.username)
async def capture_usname(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await state.clear()

    await UsersDao.add(
        tg_id=message.from_user.id,
        username=message.text,
    )
    await message.answer(f"You registered:\n\nusername:{message.text}")
    