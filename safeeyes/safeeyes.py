"""
Windows-compatible Safe Eyes bootstrap
Temporary replacement for Linux GTK implementation
"""

import time
import threading


class SafeEyes:
    def __init__(self, locale=None):
        self.locale = locale
        self.running = True

    def run(self, argv):
        print("\n=================================")
        print(" Safe Eyes Windows Prototype ")
        print("=================================\n")

        print("Safe Eyes is now running on Windows prototype mode.")
        print("This is NOT full functionality yet.")
        print()

        print("Features currently simulated:")
        print("- Break timer")
        print("- Console notifications")
        print("- Background loop")
        print()

        thread = threading.Thread(target=self.break_loop)
        thread.daemon = True
        thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.quit()

    def break_loop(self):
        counter = 0

        while self.running:
            time.sleep(10)
            counter += 1

            print(f"\n[Safe Eyes] Reminder #{counter}")
            print("Look away from the screen for 20 seconds.")
            print("Blink your eyes.")
            print()

    def quit(self):
        print("\nClosing Safe Eyes...")
        self.running = False