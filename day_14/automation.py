import schedule
import time
import datetime
import random
import os

print("=" * 50)
print("     AI AUTOMATION SYSTEM - DAY 14")
print("=" * 50)

# Make sure day_14 folder exists
os.makedirs("day_14", exist_ok=True)

def generate_daily_report():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (
        "====================================\n"
        "    DAILY AI REPORT\n"
        f"    Generated: {now}\n"
        "====================================\n\n"
        "Tasks Completed Today:\n"
        "   - AI Image Generation (Day 10)\n"
        "   - Face Detection (Day 11)\n"
        "   - NLP Analysis (Day 12)\n"
        "   - Voice Assistant (Day 13)\n\n"
        "Progress: 14/21 Days Completed\n"
        "Next Task: AI Chatbot Website\n\n"
        "AI Tip of the Day:\n"
        "   Machine Learning models improve\n"
        "   with more quality training data!\n\n"
        "====================================\n"
    )
    filename = f"day_14/report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report generated: {filename}")
    print(report)

def save_log():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{now}] System running normally\n"
    with open("day_14/automation_log.txt", 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(f"Log saved: {log_entry.strip()}")

def ai_quote():
    quotes = [
        "AI is not about replacing humans, it's about empowering them!",
        "The best way to predict the future is to create it with AI!",
        "Machine Learning: Teaching computers to learn like humans!",
        "Data is the new oil, AI is the new engine!",
        "Every expert was once a beginner - keep learning AI!"
    ]
    quote = random.choice(quotes)
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\n[{now}] AI Quote: {quote}\n")

print("\nStarting Automation System...")
print("Scheduled Tasks:")
print("   - Daily Report: every 1 minute")
print("   - Log Saver: every 30 seconds")
print("   - AI Quote: every 2 minutes")
print("\nPress Ctrl+C to stop\n")

schedule.every(1).minutes.do(generate_daily_report)
schedule.every(30).seconds.do(save_log)
schedule.every(2).minutes.do(ai_quote)

generate_daily_report()
save_log()
ai_quote()

while True:
    schedule.run_pending()
    time.sleep(1)