



import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from db import BankDB

TOKEN = "8514097375:AAFLiAmieOC7tOyqpVdDTVZGKJfZUqlAcK8"

bot = Bot(token=TOKEN)
dp = Dispatcher()
db = BankDB()


@dp.message(Command("start"))
async def start(message: types.Message):
    if not db.get_user(message.from_user.id):
        db.register(message.from_user.id, message.from_user.username)
        await message.answer("Вас зареєстровано в банку")
    else:
        await message.answer("Вітаємо з поверненням")


@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "/balance – баланс\n"
        "/deposit – інформація про депозит\n"
        "/deposit <сума> – поповнити депозит\n"
        "/withdraw – зняти депозит\n"
        "/transfer <id> <сума> – переказ користувачу"
    )


@dp.message(Command("balance"))
async def balance(message: types.Message):
    await message.answer(f"Баланс: {db.get_balance(message.from_user.id)}")


@dp.message(Command("deposit"))
async def deposit(message: types.Message):
    args = message.text.split()

    if len(args) == 1:
        await message.answer(db.get_deposit_status(message.from_user.id))
        return

    if len(args) == 2:
        try:
            amount = float(args[1])
            if amount <= 0:
                raise ValueError
        except ValueError:
            await message.answer("Сума має бути додатнім числом")
            return

        await message.answer(db.add_to_deposit(message.from_user.id, amount))
        return

    await message.answer("Формат: /deposit або /deposit <сума>")


@dp.message(Command("withdraw"))
async def withdraw(message: types.Message):
    await message.answer(db.withdraw_deposit(message.from_user.id))


@dp.message(Command("transfer"))
async def transfer(message: types.Message):
    args = message.text.split()

    if len(args) != 3:
        await message.answer("Формат: /transfer <id> <сума>")
        return

    try:
        to_id = int(args[1])
        amount = float(args[2])
        if amount <= 0:
            raise ValueError
    except ValueError:
        await message.answer("Некоректні дані")
        return

    await message.answer(
        db.transfer_to_user(message.from_user.id, to_id, amount)
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


