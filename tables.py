import pandas as pd

def daily_report(date, report):
    table = pd.DataFrame(
    report,
    index=[date])
    return table