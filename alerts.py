import os
from pathlib import Path
from funcs import get_rid_of_space

path = "Alarm"
numero = ["04"]

def report_sorting(report_path: str, date_sorting: str):
    file_name = Path(report_path).stem
    yyyymmdd = file_name[0:8]
    hhmmss = file_name[9:15]
    if yyyymmdd == date_sorting and (80000 <= int(hhmmss) <= 235959):
        return 1
    elif (yyyymmdd[0:6] + (int(yyyymmdd[7:8]) + 1)) == date_sorting and (0 <= int(hhmmss) <= 7959):
        return 1

def alert_list(folder_path, search_string_list, date_sorting):
    alerts_list = []
    
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r") as file:
            if report_sorting(os.path.abspath(file.name), date_sorting) != 1:
                continue
            file_content = file.read()
            for string in file_content.splitlines():
                string = get_rid_of_space(string)
                for search_string in search_string_list:
                    if search_string in string:
                        if string in [i[0] for i in alerts_list]:
                            for alert in alerts_list:
                                if string == alert[0]:
                                    alert[1] += 1
                        else:
                            alerts_list.append([string, 1])

    return alerts_list

