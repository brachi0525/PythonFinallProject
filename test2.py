import datetime
class commit:
    def __init__(self,message):
        self.message=message
        self.code=hash(message)
        self.date=datetime.date
    def __str__(self):
        return f"message:{self.message} code:{self.code} date:{self.date}"