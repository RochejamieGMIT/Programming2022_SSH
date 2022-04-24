import pandas as pd
import numpy as np
import plotly.graph_objs as go
import pandas_profiling as pp
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
import plotly.tools as tls
import plotly.express as px
import numpy as np

filename = "iris_csv.csv"

df = pd.read_csv(filename)

IrisSetosaGroup = df[df["class"].isin(['Iris-setosa'])] # seperating each species to their own group
IrisVersicolorGroup = df[df["class"].isin(['Iris-versicolor'])]
IrisVirginicaGroup = df[df["class"].isin(['Iris-virginica'])]


SumIS = IrisSetosaGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
)
SumIVC= IrisVersicolorGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
)
SumIV = IrisVirginicaGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
)

with open('summary.txt', 'a') as f:
    f.write("The summary for the Iris-setosa Species is as follows: \n")
    dfAsString = SumIS.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-versicolor Species is as follows: \n")
    dfAsString = SumIVC.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-virginica Species is as follows: \n")
    dfAsString = SumIV.to_string(header=True, index=True)
    f.write(dfAsString)
f.close()


dist = IrisSetosaGroup['sepallength'].value_counts()
trace = go.Pie(values=(np.array(dist)),labels=dist.index)
#layout = go.Layout(title='Each class')
#data = [trace]
#fig = go.Figure(trace,layout)
#fig.update_traces(marker=dict(line=dict(width=2)))
#fig.show()

#report = pp.ProfileReport(df)
#report.to_file('profile_report.html') # To preview data had to create a .html file as vs code could not open it

fig, ax = plt.subplots()
df.hist(column='sepallength',ax=ax,bins = 5,by = 'class');
plt.suptitle("Histogram of Sepal lenght by class")
fig.savefig('sepallengthHist.png')

fig, ax = plt.subplots()
df.hist(column='sepalwidth',ax=ax,by = 'class', bins = 5,);
plt.suptitle("Histogram of sepal width by class")
fig.savefig('sepalwidthHist.png')

fig, ax = plt.subplots()
df.hist(column='petallength',ax=ax, bins = 5,by = 'class');
plt.suptitle("Histogram of petal length by class")
fig.savefig('petallengthHist.png')


fig, ax = plt.subplots()
df.hist(column='petalwidth',ax=ax,bins = 5,by = 'class');
plt.suptitle("Histogram of petal width by class")
fig.savefig('petalwidthHist.png')

fig, ax1 = plt.subplots()
df.plot.scatter(x='sepallength',
                     y='sepalwidth')
plt.title("Scatter: Sepal length and width")
fig.savefig('scatter.png')
plt.show()


