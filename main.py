import telebot
import requests
from flask import Flask
from threading import Thread

# سيرفر وهمي صغير لإقناع Koyeb أن البوت "موقع ويب" شغال
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- إعدادات البوت ---
API_TOKEN = '8463740745:AAEywm4g4XHrOXOR7mSqrsN2WFduL6Sog6Q'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت شغال الآن بنجاح على Koyeb 🚀")

@bot.message_handler(func=lambda message: 'tiktok.com' in message.text)
def handle_tiktok(message):
    url = message.text
    try:
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        if response.get('code') == 0:
            video_url = response['data']['play']
            bot.send_video(message.chat.id, video_url, caption="تم التحميل بدون علامة مائية ✅")
    except:
        bot.reply_to(message, "حدث خطأ أثناء جلب الفيديو.")

if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر الوهمي في الخلفية
    bot.infinity_polling()
