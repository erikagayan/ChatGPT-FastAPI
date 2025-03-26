from aiogram import Router
from tg_bot.handlers.start import router as start_router
from tg_bot.handlers.gpt import router as gpt_router
from tg_bot.handlers.anthropic import router as anthropic_router
from tg_bot.handlers.model_interaction import router as model_interaction_router

router = Router()

router.include_router(start_router)
router.include_router(gpt_router)
router.include_router(anthropic_router)
router.include_router(model_interaction_router)

__all__ = ["router"]
