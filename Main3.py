import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    CoffeeDrank=[]
    HrsSleeping=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            CoffeeDrank.append(float(row["Coffee"]))
            HrsSleeping.append(float(row["sleep"]))
    return{"x":CoffeeDrank,"y":HrsSleeping}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between the coffee drank and the amount people slept are => ",correlation[0,1])

def setup():
    data_path="data4.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()

        