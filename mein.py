from alerts import alert_list, print_alert_list
import os

path = "C:\\Users\\egor1\\Documents\\loaders_data\\Alarm"
numeros = ["04-RIGHTLADDERDOWN  3"]
date = "20240315"

os.system('cls')

print_alert_list(path, numeros, date, True, False)



