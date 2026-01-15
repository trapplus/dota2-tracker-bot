from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

commands_router: Router = Router()

@commands_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello! {message.from_user.full_name}")


@commands_router.message(Command("profile"))
async def command_profile_handler(message: Message) -> None:
    """
    Handler for '/profile <query>' command
    """
    args = message.text.split()[1:] if message.text is not None else None
        
    if not args:
        await message.answer("❌ Использование: /profile 'profile_id'")
        return

    profile_id = args[0]

    if not profile_id.isdigit():
        await message.answer("❌ Profile ID должен быть числом")
        return

    await message.answer(f"🔍 Ищу матч {profile_id}...")


@commands_router.message(Command("match"))
async def command_match_handler(message: Message) -> None:
    """
    Handler for '/match <query>' command
    """

    args = message.text.split()[1:] if message.text is not None else None

    if not args:
        await message.answer("❌ Использование: /match 'match_id'")
        return

    match_id = args[0]

    if not match_id.isdigit():
        await message.answer("❌ Match ID должен быть числом")
        return

    await message.answer(f"🔍 Ищу матч {match_id}...")
