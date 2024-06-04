import polars as pl
import re
import os
from polars_table import AlarmsDF,AlarmsDFpath,AlarmsMergeDFpath


path = "C:\\loaders project\\240320_28195\\Alarm"
path_file1 = "C:\\loaders project\\240320_28195\\Alarm\\20240316_015754_173_000_28195_Alarm.pgd"
path_file2 = "C:\\loaders project\\240320_28195\\Alarm\\20240319_152144_935_000_28195_Alarm.pgd"

temp_cvs = "convert_files\\pgd_to_cvs_convert.cvs"
temp_parquet = "convert_files\\cvs_to_parquet_convert.parquet"

def string_refactoring(input_string : str): 
    input_string = re.sub(r"^__AlarmValue,", "", input_string)
    input_string = re.sub(r"(\S+)\s+(\d+)", r"\1,\2", input_string, count=1)
    input_string = re.sub(r"(\d+)\s+OPC\s+(SIMPLE|CONDITION)\s+EVENT", r"\1,OPC \2 EVENT", input_string)
    input_string = re.sub(r"(OPC (?:SIMPLE|CONDITION) EVENT)\s+\"*(\d*)\"*", r'\1,"\2"', input_string)
    input_string = re.sub(r"(\"\d*\"*)(\s+)(\d{2}-\d{2}-\d{4})", r"\1,\3", input_string)
    input_string = re.sub(r"(\d{2}-\d{2}-\d{4})\s+(\d{2}:\d{2}:\d{2}\.\d+)", r"\1,\2", input_string)
    output_string = re.sub(r"(\d{4}),(\d{2}:\d{2}:\d{2}\.\d+)\s+(\d+).+", r"\1,\2,\3", input_string)
    return output_string

def pgd_to_cvs_parquet(path : str):
    new_lines = []
    with open (path, "r") as file1:
        lines = file1.readlines()
        while lines:
            new_lines.append(string_refactoring(lines.pop(0)))
    new_lines.append((new_lines.pop())[:-1])
    open(temp_cvs, "r+").close()
    with open (temp_cvs, "w") as file2:
        columms = "Alarm,AlarmType,Event,EventType,Date,Time,TimeNumber\n"
        file2.write(columms)
        while new_lines:
            file2.write(new_lines.pop(0))
    open(temp_parquet, "r+").close()
    pl.scan_csv(temp_cvs).sink_parquet(
    temp_parquet,
    compression="zstd",
    row_group_size=100_000)

def refactoring_temp_parquet(parquet):
    df = pl.read_parquet(parquet)
    out1 = df.select(
        pl.col("Date") + " " + pl.col("Time"),
    )
    out1 = out1.select(
        pl.col("Date").str.to_datetime("%d-%m-%Y %T%.3f"),
    )
    out = df.with_columns(out1["Date"])
    out = out.select(
        pl.col("Alarm"),
        pl.col("AlarmType").cast(pl.String),
        pl.col("Event"),
        pl.col("EventType"),
        pl.col("Date").alias("DateTime"),
        pl.col("TimeNumber").cast(pl.String),
    )
    return out

def mergeParquets(folder_path):
    global AlarmsDF
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r") as file:
            pgd_to_cvs_parquet(os.path.abspath(file.name))
            try:
                AlarmsDF = AlarmsDF.vstack(refactoring_temp_parquet(temp_parquet))
                AlarmsDF.write_parquet(AlarmsMergeDFpath) #Как-то нужно ускорить
            except:
                with open("error.txt", "w") as err:
                    err.write(file.name+"\n")
                    print(file.name)
    print("End")


mergeParquets(path)

#pgd_to_cvs_parquet(path_file2)

#AlarmsDF = AlarmsDF.vstack(refactoring_temp_parquet(temp_parquet))

#print(AlarmsDF)