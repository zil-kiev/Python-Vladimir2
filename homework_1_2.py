import datetime
import time
Data = int(input('Vasha data rojdeniya: '))
now_date=datetime.date.today()
cur_year = now_date.year
print('Vam:',cur_year-Data)
