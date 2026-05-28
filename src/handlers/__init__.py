from aiogram import Router
from handlers.start import start_router

def get_handlers_router() -> Router:
    main_router = Router()

    main_router.include_routers(
        start_router
    )

    return main_router