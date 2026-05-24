import schedule
import time
import datetime
import random
import json
import os

print("=" * 50)
print("     🤖 AI AUTOMATION SYSTEM - DAY 14")
print("=" * 50)

# ─── Task 1: Auto Generate Daily Report ───
def generate_daily_report():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""
====================================
    📊 DAILY AI REPORT
    Generated: {now}
====================================

✅ Tasks Completed Today:
   - AI Image Generation (Day 10)
   - Face Detection (Day 11)
   - NLP Analysis (Day 12)
   - Voice Assistant (Day 13)

📈 Progress: 14/21 Days Completed
🎯 Next Task: AI Chatbot Website

💡 AI Tip of the Day:
   Machine Learning models improve
   with more quality training data!

====================================
"""
    filename = f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Report generated: {filename}")
    print(report)

# ─── Task 2: Auto Save Logs ───
def save_log():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{now}] ✅ System running normally\n"
    
    with open("automation_log.txt", 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(f"📝 Log saved: {log_entry.strip()}")

# ─── Task 3: AI Quote Generator ───
def ai_quote():
    quotes = [
        "AI is not about replacing humans, it's about empowering them!",
        "The best way to predict the future is to create it with AI!",
        "Machine Learning: Teaching computers to learn like humans!",
        "Data is the new oil, AI is the new engine!",
        "Every expert was once a beginner — keep learning AI!"
    ]
    quote = random.choice(quotes)
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\n💡 [{now}] AI Quote: {quote}\n")

# ─── Schedule Tasks ───
print("\n🚀 Starting Automation System...")
print("📋 Scheduled Tasks:")
print("   - Daily Report: every 1 minute (demo)")
print("   - Log Saver: every 30 seconds")
print("   - AI Quote: every 2 minutes")
print("\nPress Ctrl+C to stop\n")

schedule.every(1).minutes.do(generate_daily_report)
schedule.every(30).seconds.do(save_log)
schedule.every(2).minutes.do(ai_quote)

# Run immediately once
generate_daily_report()
save_log()
ai_quote()

# Keep running
while True:
    schedule.run_pending()
    time.sleep(1)