import plotly.express as px
import csv
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
        fig.show()
def getDataSource(data_path):
    MarksInPercentage=[]
    DaysPresent=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))

        
    return{"x":MarksInPercentage,"y":DaysPresent}

def findcorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Co relation between Marks and Days Present: \n=",correlation[0,1])


def setup():
    data_path="data2.csv"
    dataSource=getDataSource(data_path)
    findcorrelation(dataSource)
    plotfigure(data_path)
setup()
