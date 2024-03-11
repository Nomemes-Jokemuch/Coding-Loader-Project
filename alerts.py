import os

def get_rid_of_space(string):
    return string[:string.find('          ')]

folder_path = 'C:\\Users\\egor1\\Downloads\\Report 21.12.23_4\\28195\\28195\\Alarm\\2023-12-21'

search_string_list = [
    '__AlarmValue,04-WaitBrake_Warn_Cwd  3',
    '__AlarmValue,04-WaitBrake_Warn_Hst  5',
    '__AlarmValue,04-WaitBrake_Warn_Hst  3'
]

alerts_list = []

if os.path.exists(folder_path):
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            with open(os.path.join(folder_path, file_name), 'r') as file:
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
    print(i)

