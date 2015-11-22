import datetime
dt = datetime.datetime.strptime(input().strip(), "%I:%M:%S%p")
print(dt.strftime("%H:%M:%S"))
