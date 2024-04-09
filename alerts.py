import os
from pathlib import Path
import datetime

def print_alert_list(folder_path, search_string_list, date_sorting, sort_date=True, file_names=False):
    if file_names:
        for i in alert_list(folder_path, search_string_list, date_sorting, sort_date, file_names):
            for j in i[2]:
                print(j)
        print(len(i[2]))
    else:
        for i in alert_list(folder_path, search_string_list, date_sorting, sort_date, file_names):
            print(i[0], i[1])

def report_sorting(report_path: str, date_sorting: str):
    file_name = Path(report_path).stem
    left_border = datetime.datetime(int(date_sorting[0:4]), int(date_sorting[4:6]), int(date_sorting[6:8]), 8)
    right_border = datetime.datetime(int(date_sorting[0:4]), int(date_sorting[4:6]), int(date_sorting[6:8]) + 1, 7, 59, 59)
    date = datetime.datetime(int(file_name[0:4]), int(file_name[4:6]), int(file_name[6:8]), int(file_name[9:11]), int(file_name[11:13]), int(file_name[13:15]))

    if left_border <= date <= right_border:
        return 1
    return 0

def alert_list(folder_path, search_string_list, date_sorting, sort_date=True, file_names=False):
    alerts_list = []

    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r") as file:
            if (
                report_sorting(os.path.abspath(file.name), date_sorting) == 0
                and sort_date
            ):
                continue
            file_content = file.read()
            for string in file_content.splitlines():
                string = string[: string.find("          ")]
                for search_string in search_string_list:
                    if search_string in string:
                        if string in [i[0] for i in alerts_list]:
                            for alert in alerts_list: #оптимизировать
                                if string == alert[0]:
                                    alert[1] += 1
                                    if file_names:
                                        alert[2].append(file_name)
                                    
                        elif file_names:
                            alerts_list.append([string, 1, [file_name]])
                        else:
                            alerts_list.append([string, 1])

    return alerts_list


