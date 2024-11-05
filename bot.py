import telebot
import time
import psutil
import speedtest
import platform

bot = telebot.TeleBot("BoT_TOKEN")

@bot.message_handler(commands=['speed'])
def measure_speed(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "تم البدء بقياس السرعة ✅", parse_mode="Markdown")
    time.sleep(0.5)

    start_time = time.time()
    for i in range(11):
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg.message_id,
            text=f"*\n♻️ يتم قياس السرعة انتظر قليلاً... {i * 10}%\n*",
            parse_mode="Markdown"
        )
        time.sleep(0.05)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 4)

    if elapsed_time <= 1.5:
        status = "جامدة 💯"
    elif elapsed_time <= 3:
        status = "مش وحشة 🧸"
    else:
        status = "ضعيفة أوي ❌"

    st = speedtest.Speedtest()
    download_speed = round(st.download() / (1024 * 1024), 2)
    upload_speed = round(st.upload() / (1024 * 1024), 2)

    cpu_usage = psutil.cpu_percent(interval=0.5)
    memory_info = psutil.virtual_memory()
    total_memory = round(memory_info.total / (1024 * 1024 * 1024), 2)
    used_memory = round(memory_info.used / (1024 * 1024 * 1024), 2)
    available_memory = round(memory_info.available / (1024 * 1024 * 1024), 2)

    disk_info = psutil.disk_usage('/')
    total_disk = round(disk_info.total / (1024 * 1024 * 1024), 2)
    used_disk = round(disk_info.used / (1024 * 1024 * 1024), 2)
    disk_type = "SSD" if "ssd" in platform.platform().lower() else "HDD"

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=msg.message_id,
        text=(
            f"*✬ نتائج قياس الجهاز:*\n\n"
            f"📊 *سرعة القياس:* {elapsed_time} ثانية\n"
            f"⚙️ *التقييم:* {status}\n\n"
            f"*💻 معلومات النظام:*\n"
            f"🔹 *سرعة التحميل:* {download_speed} Mbps\n"
            f"🔹 *سرعة الرفع:* {upload_speed} Mbps\n"
            f"🔹 *استخدام المعالج:* {cpu_usage}%\n"
            f"🔹 *سعة الذاكرة الكلية:* {total_memory} GB\n"
            f"🔹 *الذاكرة المستخدمة:* {used_memory} GB\n"
            f"🔹 *الذاكرة المتاحة:* {available_memory} GB\n\n"
            f"🔹 *سعة الذاكرة الصلبة:* {total_disk} GB\n"
            f"🔹 *المستخدم من الذاكرة الصلبة:* {used_disk} GB\n"
            f"🔹 *نوع الذاكرة الصلبة:* {disk_type}\n"
        ),
        parse_mode="Markdown"
    )

bot.polling()