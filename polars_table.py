import polars as pl

AlarmsDFpath = "AlarmsDF.parquet"

AlarmsDF = pl.read_parquet(AlarmsDFpath)

print(AlarmsDF)
