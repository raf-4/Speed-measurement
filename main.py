import time
import psutil
import speedtest
import platform

def measure_speed():
    print("تم البدء بقياس السرعة ✅")
    time.sleep(0.5)

    start_time = time.time()
    for i in range(11):
        print(f"♻️ يتم قياس السرعة انتظر قليلاً... {i * 10}%")
        time.sleep(0.05)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 4)

    if elapsed_time <= 1.5:
        status = "جامدة 💯"
    elif elapsed_time <= 3:
        status = "مش وحشة 🧸"
    else:
        status = "ضعيفة أوي ❌"

    try:
        st = speedtest.Speedtest()
        download_speed = round(st.download() / (1024 * 1024), 2)
        upload_speed = round(st.upload() / (1024 * 1024), 2)
        internet_info = f"🔹 سرعة التحميل: {download_speed} Mbps\n🔹 سرعة الرفع: {upload_speed} Mbps\n"
    except:
        internet_info = "🔹 لم أستطع قياس سرعة التحميل والرفع\n"

    try:
        cpu_usage = psutil.cpu_percent(interval=0.5)
        cpu_info = f"🔹 استخدام المعالج: {cpu_usage}%\n"
    except:
        cpu_info = "🔹 لم أستطع الوصول إلى معلومات المعالج\n"

    try:
        memory_info = psutil.virtual_memory()
        total_memory = round(memory_info.total / (1024 * 1024 * 1024), 2)
        used_memory = round(memory_info.used / (1024 * 1024 * 1024), 2)
        available_memory = round(memory_info.available / (1024 * 1024 * 1024), 2)
        memory_details = (
            f"🔹 سعة الذاكرة الكلية: {total_memory} GB\n"
            f"🔹 الذاكرة المستخدمة: {used_memory} GB\n"
            f"🔹 الذاكرة المتاحة: {available_memory} GB\n"
        )
    except:
        memory_details = "🔹 لم أستطع الوصول إلى معلومات الذاكرة\n"

    try:
        disk_info = psutil.disk_usage('/')
        total_disk = round(disk_info.total / (1024 * 1024 * 1024), 2)
        used_disk = round(disk_info.used / (1024 * 1024 * 1024), 2)
        disk_type = "SSD" if "ssd" in platform.platform().lower() else "HDD"
        disk_details = (
            f"🔹 سعة الذاكرة الصلبة: {total_disk} GB\n"
            f"🔹 المستخدم من الذاكرة الصلبة: {used_disk} GB\n"
            f"🔹 نوع الذاكرة الصلبة: {disk_type}\n"
        )
    except:
        disk_details = "🔹 لم أستطع الوصول إلى معلومات الذاكرة الصلبة\n"

    print("\n✬ نتائج قياس الجهاز:\n")
    print(f"📊 سرعة القياس: {elapsed_time} ثانية")
    print(f"⚙️ التقييم: {status}\n")
    print("💻 معلومات النظام:")
    print(internet_info)
    print(cpu_info)
    print(memory_details)
    print(disk_details)

measure_speed()