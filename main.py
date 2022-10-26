import rumps
from datetime import datetime, date

class BeerApp(rumps.App):
    def __init__(self):
        super(BeerApp, self).__init__("Ølsalg")

    @rumps.timer(1)
    def update(self, _):
        today_ = date.today()
        today_str = today_.strftime("%A")
        h = 20
        if today_str == "Saturday":
            h = 18
        elif today_str == "Sunday":
            h = 0

        deadline = datetime(year=today_.year, month=today_.month, day=today_.day, hour=h, minute=00)
        time_left = deadline - datetime.now()
        self.menu.clear()
        if time_left.total_seconds() < 0:
            self.title = "Stengt"
            self.menu = ["Ølsalget er stengt."]
        else:
            self.title = str(time_left).split(".")[0]
            self.menu = ["Ølsalget stenger om:", str(self.title)]

        if (time_left.total_seconds() == 60*30):
            rumps.notification(title="Kjøp øl!", subtitle="Ølsalget stenger om 30 min", message='')

if __name__ == "__main__":
    app = BeerApp().run()
