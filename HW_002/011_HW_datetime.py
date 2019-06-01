from datetime import datetime, timedelta
dt_now = datetime.now()
delta = timedelta(days = 1)
#delta_m = timedelta(months = 1)
print(dt_now)
print(dt_now - delta)
#print(dt_now - delta_m)