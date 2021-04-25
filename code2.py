import plotly.express as px
import csv
import numpy as np

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="sleep in hours",y="Coffee in ml")
        fig.show()
def getDataSource(data_path):
    Coffeeinml=[]
    sleepinhours=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Coffeeinml.append(float(row["Coffee in ml"]))
            sleepinhours.append(float(row["sleep in hours"]))

        
    return{"x":Coffeeinml,"y":sleepinhours}

def findcorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Co relation between coffee in ml and sleep: \n=",correlation[0,1])


def setup():
    data_path="data1.csv"
    dataSource=getDataSource(data_path)
    findcorrelation(dataSource)
    plotfigure(data_path)
setup()
