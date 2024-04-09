import os
from alerts import alerts_dict
from tables import daily_report
import pandas as pd

os.system("cls")

path = "C:\\loaders project\\240320_28195\\Alarm"
numeros = ["04-U74D01F1", "04-L52C01A"]
date = "20240317"

dict = alerts_dict(path, numeros, date, True, False)

print(daily_report(date, dict))

#print(dict.values())
#print(dict.keys())

