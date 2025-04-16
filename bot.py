import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

FAQ = {
    "время работы": "Мы открыты каждый день с 10:00 до 18:00.",
    "доставка": "Доставка по Денверу — $25. Бесплатно при заказе от $50.",
    "адрес": "Наш магазин находится в центре Денвера: 1655 Larimer st."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот цветочного магазина 🌸\n\n"
        "Ты можешь спросить меня:\n"
        "- Время работы\n"
        "- Доставка\n"
        "- Адрес\n\n"
        "Или просто напиши заказ (например: \"Хочу букет роз\")"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    for key in FAQ:
        if key in text:
            await update.message.reply_text(FAQ[key])
            return

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )

    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
