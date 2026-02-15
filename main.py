import telebot
import requests
import os

# ضع التوكن الجديد هنا
API_TOKEN = '8463740745:AAEywm4g4XHrOXOR7mSqrsN2WFduL6Sog6Q'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي رابط تيك توك لتحميله بدون علامة مائية بجودة HD. 📥")

@bot.message_handler(func=lambda message: 'tiktok.com' in message.text)
def handle_tiktok(message):
    url = message.text
    msg = bot.reply_to(message, "⏳ جاري جلب الفيديو... انتظر لحظة")
    
    try:
        # استخدام API TikWM القوي
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        
        if response.get('code') == 0:
            video_url = response['data']['play']
            # إرسال الفيديو مباشرة
            bot.send_video(message.chat.id, video_url, caption="✅ تم التحميل بنجاح @ALzaabisa_bot")
            bot.delete_message(message.chat.id, msg.message_id)
        else:
            bot.edit_message_text("❌ فشل التحميل، تأكد أن الرابط صحيح والحساب عام.", message.chat.id, msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"⚠️ حدث خطأ تقني، حاول لاحقاً.", message.chat.id, msg.message_id)

print("البوت شغال الآن على Koyeb...")
bot.infinity_polling()
