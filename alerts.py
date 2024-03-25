import os
from pathlib import Path

folder_path = "C:\\Users\\USER\\Downloads\\240320_28195.zip\\240320_28195\\Alarm"

search_string_list = ["04"]

alerts_list = []

report_test_path = "C:\\Users\\USER\\Documents\\GitHub\\Coding-Loaders-Project\\Alarm\\20240314_171213_563_000_28195_Alarm.pgd"


def report_sorting(report_path: str, date_sorting: str):
    with open(report_path, "r") as report:
        file_name = Path(report_path).stem
        yyyymmdd = file_name[0:8]
        hhmmss = file_name[9:15]
        if yyyymmdd == date_sorting and (80000 <= int(hhmmss) <= 235959):
            return 1
        elif (yyyymmdd[0:6] + (int(yyyymmdd[7:8]) + 1)) == date_sorting and (0 <= int(hhmmss) <= 7000):
            return 1


def get_rid_of_space(string):
    return string[: string.find("          ")]


def alerts(folder_path):
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                with open(os.path.join(folder_path, file_name), "r") as file:
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
    for i in alerts_list:
        return i
