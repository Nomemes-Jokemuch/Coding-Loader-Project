import os
from pathlib import Path
import datetime
 
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

def test1(folder_path):
    files = os.listdir(folder_path)
    for index, file_name in enumerate(files):
        file_dict = {}
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as file:
            file_dict[file_name] = index
        print(file_dict)
        file_dict.clear()

def report_sorting_II(report_path: str, date_sorting: str):
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

def number_alert_sort(dictionary):
    values = {key: value for key, value in dictionary.items()}
    sorted_types = sorted(values.keys(), key=lambda x: int(x.split()[-1]))
    values_list = [values[key] for key in sorted_types]
    return values_list

def alerts_dict(
    folder_path, search_string_list, date_sorting, sort_date=True, file_names=False
):
    alert_dict = {}
    file_list = []
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r") as file:
            if (
                report_sorting(os.path.abspath(file.name), date_sorting) == 0
                and sort_date
            ):
                continue
            file_content = file.read()
            for string in file_content.splitlines():
                string = string[: string.find("  OPC")]
                for search_string in search_string_list:
                    if search_string in string:
                        if string in alert_dict:
                            alert_dict[string] += 1
                            if file_names:
                                file_list.append(file_name)
                        else:
                            alert_dict[string] = 1
                            if file_names:
                                file_list.append(file_name)
    print('\n'.join(file_list))
    return alert_dict


def sub_alerts_dict(
    folder_path, search_string_list, date_sorting, sort_date=True, file_names=False
):
    alert_dict = {"name": "0"}
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r") as file:
            if (    
                report_sorting(os.path.abspath(file.name), date_sorting) == 0
                and sort_date
            ):
                continue
            file_content = file.read()
            for string in file_content.splitlines():
                string = string[: string.find("  OPC")]
                for search_string in search_string_list:
                    if search_string in string:
                        if string in alert_dict:
                            alert_dict[string] += 1
                            if file_names:
                                alert_dict["name"] = file_name
                        else:
                            alert_dict[string] = 1
                            if file_names:
                                alert_dict["name"] = file_name
            if alert_dict["name"] != "0":
                print(alert_dict)
                alert_dict = {"name": "0"}
    return 
