import time
import threading
from plyer import notification


class SafeEyes:
    def __init__(self):
        self.running = True
        self.reminder_count = 0

        # Timing settings
        self.work_interval = 20
        self.break_message = (
            "Look away from the screen for 20 seconds.\n"
            "Blink your eyes."
        )

    def show_notification(self):
        notification.notify(
            title="Safe Eyes Reminder",
            message=self.break_message,
            timeout=5
        )

    def reminder_loop(self):
        while self.running:
            time.sleep(self.work_interval)

            self.reminder_count += 1

            print(f"\n[Safe Eyes] Reminder #{self.reminder_count}")

            self.show_notification()

    def run(self):
        print("=" * 32)
        print(" Safe Eyes Windows Prototype ")
        print("=" * 32)

        print("\nWindows notifications enabled.")
        print("Press CTRL + C to stop.\n")

        reminder_thread = threading.Thread(
            target=self.reminder_loop
        )

        reminder_thread.daemon = True
        reminder_thread.start()

        try:
            while self.running:
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nClosing Safe Eyes...")
            self.running = False