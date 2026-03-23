import schedule
import time
from plyer import notification

def reminder():
    notification.notify(
        title="Daily Reminder",
        message="Time to study Python automation!",
        timeout=10
    )

# Schedule reminders
schedule.every().day.at("19:11").do(reminder)
schedule.every().day.at("15:00").do(reminder)
schedule.every().day.at("21:00").do(reminder)

print("Reminder bot running...")

while True:
    schedule.run_pending()
    time.sleep(1)