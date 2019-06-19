import datetime

class MessageUser():
    user_details = []
    messages = []
    base_message = """ Hi {name}!

Thank you for the purchase on {date}.
We hope ypu are excited about usig it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team RUNA
"""

    def add_user(self, name, amount):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        self.user_details.append(detail)
    
    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                new_amount = "%.2f" %(detail["amount"])
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name = name,
                    date = date,
                    total = new_amount
                )
                self.messages.append(new_msg)
            return self.messages
        return []