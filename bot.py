from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '8084707418:AAG4qZ8GizdIU6gniIp00Hdutfw0Klab1-w'  # <-- вставь сюда свой токен

FAQ = {
    "время работы": "Мы открыты каждый день с 9:00 до 20:00.",
    "доставка": "Доставка по Денверу — $5. Бесплатно при заказе от $50.",
    "адрес": "Наш магазин находится в центре Денвера: 123 Flower St."
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

    await update.message.reply_text("Спасибо! Мы приняли ваш заказ 💐\nСкоро свяжемся с вами для уточнения.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
