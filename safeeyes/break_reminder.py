import time
from plyer import notification


class BreakReminder:
    def __init__(self):
        self.break_interval = 20 * 60
        self.running = True

    def notify(self):
        notification.notify(
            title="Safe Eyes",
            message="Look away for 20 seconds 👀",
            timeout=10
        )

    def start(self):
        print("Safe Eyes started.")

        reminder = 1

        try:
            while self.running:
                time.sleep(self.break_interval)

                print(f"Break reminder #{reminder}")

                self.notify()

                reminder += 1

        except KeyboardInterrupt:
            print("Stopping Safe Eyes...")