import os
from alerts import alerts_dict
from tables import daily_report
from alerts import test1
from alerts import sub_alerts_dict
import pandas as pd

os.system("cls")

path = "C:\\loaders project\\240320_28195\\Alarm"
numeros = ["04-U74D01F1", "04-RIGHTLADDERDOWN"]
date = "20240317"

dict = alerts_dict(path, numeros, date, True, False)

#print(test1(path))

#print(dict)

sub_alerts_dict(path, numeros, date, True, True)

#print(daily_report(date, dict))



