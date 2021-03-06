import schedule
from datetime import datetime


def job():
    time = str(datetime.now().time()).split(":")
    if time[0] <= '12':
        for _ in range(int(time[0])):
            print("Ку")
        exit()
    elif time[0] % 12 == 0:
        pm_time = int(time[0]) - 12
        for _ in range(pm_time):
            print("Ку")
        exit()


schedule.every().hour.at(":18").do(job)

while True:
    schedule.run_pending()
