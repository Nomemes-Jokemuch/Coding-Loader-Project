import os
from alerts import alerts_dict
from tables import daily_report
from alerts import test1
from alerts import sub_alerts_dict
import pandas as pd

os.system("cls")

path = "C:\\loaders project\\240320_28195\\Alarm"
alerts = ["04-RIGHTLADDERDOWN", "04-U74D01F1", "04-WaitBrake_Warn_Cwd", 
          "04-Fault_Reset_Activated", "04-U74D01F1", "04-L05X01T", 
          "04-U70X16B", "04-L52C01A","04-LIMITS"]
date = "20240318"

dict = alerts_dict(path, alerts, date, True, False)

#print(test1(path))

#print(dict)

sub_alerts_dict(path, alerts, date, True, True)

#print(daily_report(date, dict))



