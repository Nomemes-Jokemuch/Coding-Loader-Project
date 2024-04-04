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
    d_time = datetime.timedelta(days=1)
    DateSorting = datetime.date.fromisoformat(date_sorting)
    file_name = Path(report_path).stem
    yyyymmdd = datetime.date.fromisoformat(file_name[0:8])
    hhmmss = file_name[9:15]
    if yyyymmdd == DateSorting and (80000 <= int(hhmmss) <= 235959):
        return 1
    elif (yyyymmdd - d_time) == DateSorting and (0 <= int(hhmmss) <= 75959):
        return 1
    else:
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
                            for alert in alerts_list:
                                if string == alert[0]:
                                    alert[1] += 1
                                    if file_names:
                                        alert[2].append(file_name)
                                    
                        elif file_names:
                            alerts_list.append([string, 1, [file_name]])
                        else:
                            alerts_list.append([string, 1])

    return alerts_list


