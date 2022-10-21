from base64 import b16decode
from datetime import date, datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL,'de_DE')
#a
now = datetime.now()
print(now.strftime("%A, %d.%m.%Y"))

#b
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
seconds = (now - midnight).seconds
print(seconds)

#c
d0 = date(2002, 11, 21)
d1 = date(2022, 10, 21)
delta = d1 - d0
print(delta.days)