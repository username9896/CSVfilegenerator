import pandas as pd
import random


def randomvalue ():
    for i in range(1, 500):
        randomdatas = [random.uniform(-0, 40) for _ in range(500)]
        Ledvalue = [1 if data < 15 else 0 for data in randomdatas]
        dateandtime = pd.date_range(start='2003-07-23', periods=500, freq='T')
        storedata = {'DateAndTime': dateandtime, 'Data': randomdatas, 'Status': Ledvalue}
        return storedata

values = pd.DataFrame(randomvalue())
values.to_csv("C:/Users/vicky/OneDrive/Desktop/New folder/courses.csv", index=False)
