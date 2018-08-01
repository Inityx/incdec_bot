from telegram.ext import BaseFilter

class IncDecFilter(BaseFilter):
    def filter(self, message):
        return any(action in message.text for action in ['--', '++', '—'])
