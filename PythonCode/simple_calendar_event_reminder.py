# simple_calendar_event_reminder.py
from datetime import datetime, timedelta

class Event:
    def __init__(self, name, event_time):
        self.name = name
        self.event_time = event_time

    def __str__(self):
        return f"{self.name} at {self.event_time}"

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def check_reminders(self):
        now = datetime.now()
        for event in self.events:
            if now >= event.event_time - timedelta(minutes=30) and now < event.event_time:
                print(f"Reminder: {event}")

if __name__ == "__main__":
    calendar = Calendar()
    while True:
        action = input("Choose action: add, check, or quit: ").strip().lower()
        if action == 'add':
            name = input("Enter event name: ")
            event_time_str = input("Enter event time (YYYY-MM-DD HH:MM): ")
            event_time = datetime.strptime(event_time_str, "%Y-%m-%d %H:%M")
            event = Event(name, event_time)
            calendar.add_event(event)
        elif action == 'check':
            calendar.check_reminders()
        elif action == 'quit':
            break
