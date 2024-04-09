from alerts import alert_list, print_alert_list
import os

path_1 = "C:\\Users\\egor1\\Documents\\loaders_data\\Alarm"
path_2 = "C:\\Users\\USER\\Desktop\\240320_28195\\Alarm"

numeros = ["04-U74D01F1"]
date = "20240317"

os.system("cls")

print_alert_list(path_2, numeros, date, True, False)
