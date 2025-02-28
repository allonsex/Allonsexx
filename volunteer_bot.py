from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [['Темы для волонтерства', 'Список мероприятий'], ['Помощь', 'О боте']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        " Привет! Я бот Волонтер Helper.\n"
        "Выбери одну из вкладок ниже:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text == 'Темы для волонтерства':
        themes_keyboard = [['Экология', 'Помощь животным'], ['Дети', 'Пожилые люди'], ['Назад']]
        reply_markup = ReplyKeyboardMarkup(themes_keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "Выбери тему для волонтерства:",
            reply_markup=reply_markup
        )
    elif text == 'Список мероприятий':
        events_keyboard = [['Мероприятие 1', 'Мероприятие 2'], ['Мероприятие 3', 'Назад']]
        reply_markup = ReplyKeyboardMarkup(events_keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "Выбери мероприятие для подробной информации:",
            reply_markup=reply_markup
        )
    elif text == 'Помощь':
        await update.message.reply_text(
            " Справка по использованию бота:\n\n"
            "/start - Главное меню\n"
            "/help - Помощь\n"
            "/about - О боте\n\n"
            "Выбери вкладку из меню, чтобы начать."
        )
    elif text == 'О боте':
        await update.message.reply_text(
            " Я — бот Волонтер Helper.\n"
            "Моя цель — помочь тебе найти подходящие волонтерские мероприятия "
            "и вдохновить на добрые дела!\n\n"
            "Если у тебя есть вопросы, нажми 'Помощь'."
        )
    elif text in ['Экология', 'Помощь животным', 'Дети', 'Пожилые люди']:
        ideas = {
            'Экология': [
                "1. Организуй субботник в своем районе.",
                "2. Посади дерево или цветы в парке.",
                "3. Проведи лекцию о важности переработки мусора."
            ],
            'Помощь животным': [
                "1. Помоги местному приюту для животных кормом или медикаментами.",
                "2. Стань временным хозяином для бездомного животного.",
                "3. Организуй сбор средств для лечения больных животных."
            ],
            'Дети': [
                "1. Проведи мастер-класс для детей в детском доме.",
                "2. Собери и передай детям книги, игрушки или одежду.",
                "3. Организуй праздник для детей из малообеспеченных семей."
            ],
            'Пожилые люди': [
                "1. Помоги пожилым соседям с покупками или уборкой.",
                "2. Организуй чаепитие в доме престарелых.",
                "3. Научи пожилых людей пользоваться смартфонами и компьютерами."
            ]
        }
        message = f"Отлично! Ты выбрал тему: {text}.\n\nВот три идеи для тебя:\n\n" + "\n".join(ideas[text])
        await update.message.reply_text(message)
    elif text in ['Мероприятие 1', 'Мероприятие 2', 'Мероприятие 3']:
        event_info = {
            'Мероприятие 1': " Субботник в парке\n Москва\n [Подробнее](https://example.com/event1)",
            'Мероприятие 2': " Помощь бездомным животным\n Санкт-Петербург\n [Подробнее](https://example.com/event2)",
            'Мероприятие 3': " Уроки для детей в детском доме\n Екатеринбург\n [Подробнее](https://example.com/event3)"
        }
        await update.message.reply_text(event_info[text], parse_mode="Markdown")
    elif text == 'Назад':
        await start(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выбери вкладку из меню.")

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        " Справка по использованию бота:\n\n"
        "/start - Главное меню\n"
        "/help - Помощь\n"
        "/about - О боте\n\n"
        "Выбери вкладку из меню, чтобы начать."
    )

async def about_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        " Я — бот Волонтер Helper.\n"
        "Моя цель — помочь тебе найти подходящие волонтерские мероприятия "
        "и вдохновить на добрые дела!\n\n"
        "Если у тебя есть вопросы, нажми 'Помощь'."
    )

def main() -> None:
    application = Application.builder().token("7843444109:AAF9YyvzOjMnlLADeyeNRqLo3TJJ3RgfT-w").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()