import polars as pl

AlarmsDFpath = "AlarmsDF.parquet"
AlarmsMergeDFpath = "AlarmMergeDF.parquet"

AlarmsDF = pl.read_parquet(AlarmsDFpath)
AlarmsMergeDF = pl.read_parquet(AlarmsMergeDFpath)

#df_first_row = AlarmsDF.head(1)
#df_first_row.write_parquet(AlarmsDFpath)
#df_first_row.write_parquet(AlarmsMergeDFpath)

#print(AlarmsDF)
print(AlarmsMergeDF)
