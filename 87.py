import datetime

now = str(datetime.datetime.now())
print(now.split()[1][:5])
# h = datetime.datetime.now().hour
# m = datetime.datetime.now().minute
# print(f"{h}:{m}")
