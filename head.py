import os
from alerts import alerts_dict
from tables import daily_report
from alerts import test1
from alerts import sub_alerts_dict


os.system("cls")

path = "C:\\loaders project\\240320_28195\\Alarm"
alerts = [
    "04-RIGHTLADDERDOWN",
    "04-U74D01F1",
    "04-WaitBrake_Warn_Cwd",
    "04-Fault_Reset_Activated",
    "04-U74D01F1",
    "04-L05X01T",
    "04-U70X16B",
    "04-L52C01A",
    "04-LIMITS",
]
date = "20240318"

dict = alerts_dict(path, alerts, date, True, False)

print(test1(path, date))

# print(dict)

# sub_alerts_dict(path, alerts, date, True, True)

# print(daily_report(date, dict))


# "20240315" = 2531
# "20240316" = 3971
# "20240317" = 5410
# "20240318" = 6850