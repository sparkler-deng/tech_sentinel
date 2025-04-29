from notifier.base import NotifierBase

class EmailNotifier(NotifierBase):
    def notify(self, message: str):
        print(f"Sending Email: {message}")
