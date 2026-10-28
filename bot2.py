import telebot
from telebot import types

TOKEN = "8822971823:AAHR9Ky5KcC_5uBF-HX2tMcQuwEfD6vioQg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("🟡 Pro Obuna")
    button2 = types.KeyboardButton("ℹ️ Bot haqida")
    button3 = types.KeyboardButton("📞 Bog'lanish")
    keyboard.add(button1)
    keyboard.add(button2, button3)
    
    bot.send_message(
        message.chat.id, 
        f"Assalomu alaykum, {message.from_user.first_name}!\nBotimizga xush kelibsiz!", 
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "🟡 Pro Obuna":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("1️⃣ 1 oylik obuna"))
        keyboard.add(types.KeyboardButton("3️⃣ 3 oylik obuna"))
        keyboard.add(types.KeyboardButton("1️⃣ 1 yillik obuna"))
        keyboard.add(types.KeyboardButton("⬅️ Orqaga"))
        
        bot.send_message(
            message.chat.id, 
            "Quyidagi obuna turlaridan birini tanlang:\n\n"
            "1 oylik obuna - 100 000 so'm\n"
            "3 oylik obuna - 300 000 so'm\n"
            "1 yillik obuna - 1 200 000 so'm", 
            reply_markup=keyboard
        )

    elif message.text == "1️⃣ 1 oylik obuna":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("✅ To'lov qildim"))
        keyboard.add(types.KeyboardButton("⬅️ Orqaga"))

        bot.send_message(
            message.chat.id, 
            "Siz 1 oylik obuna (12 000 so'm) ni tanladingiz.\n\n"
            "💳 Karta raqam: 2321 8373 2334 2322\n"
            "👤 Karta egasi: Normo'minov Eldor\n\n"
            "⚠️ To'lovni amalga oshirgach, to'lov cheki (skrinshot) rasmini adminga (t.me/eldor_python_2026_bot) yuboring va pastdagi '✅ To'lov qildim' tugmasini bosing!",
            reply_markup=keyboard
        )

    elif message.text == "3️⃣ 3 oylik obuna":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("✅ To'lov qildim"))
        keyboard.add(types.KeyboardButton("⬅️ Orqaga"))

        bot.send_message(
            message.chat.id, 
            "Siz 3 oylik obuna (32 000 so'm) ni tanladingiz.\n\n"
            "💳 Karta raqam: 2321 8373 2334 2322\n"
            "👤 Karta egasi: Normo'minov Eldor\n\n"
            "⚠️ To'lovni amalga oshirgach, to'lov cheki (skrinshot) rasmini adminga (t.me/eldor_python_2026_bot) yuboring va pastdagi '✅ To'lov qildim' tugmasini bosing!",
            reply_markup=keyboard
        )

    elif message.text == "1️⃣ 1 yillik obuna":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("✅ To'lov qildim"))
        keyboard.add(types.KeyboardButton("⬅️ Orqaga"))

        bot.send_message(
            message.chat.id, 
            "Siz 1 yillik obuna (200 000 so'm) ni tanladingiz.\n\n"
            "💳 Karta raqam: 2321 8373 2334 2322\n"
            "👤 Karta egasi: Normo'minov Eldor\n\n"
            "⚠️ To'lovni amalga oshirgach, to'lov cheki (skrinshot) rasmini adminga (t.me/eldor_python_2026_bot) yuboring va pastdagi '✅ To'lov qildim' tugmasini bosing!",
            reply_markup=keyboard
        )

    elif message.text == "✅ To'lov qildim":
        bot.send_message(
            message.chat.id, 
            "⚠️ To'lovni amalga oshirganingiz uchun rahmat!\n\n"
            "Chekingiz admin tomonidan tekshirilgach, obunangiz tez orada faollashtiriladi."
        )

    elif message.text == "ℹ️ Bot haqida":
        bot.reply_to(message, "Bu bot orqali siz Pro obunalarni xarid qilishingiz mumkin.")

    elif message.text == "📞 Bog'lanish":
        bot.reply_to(message, "Admin bilan bog'lanish: t.me/eldor_python_2026_bot")

    elif message.text == "⬅️ Orqaga":
        start(message)

    else:
        bot.reply_to(message, message.text)

print("Bot ishga tushdi....")
bot.infinity_polling()