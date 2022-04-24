import pandas as pd
import numpy as np


filename = "iris_csv.csv"

df = pd.read_csv(filename)
listofCols = ['sepallength', 'sepalwidth']
print(df[listofCols].head(2))


IrisSetosaGroup = df[df["class"].isin(['Iris-setosa'])] # seperating each species to their own group
IrisVersicolorGroup = df[df["class"].isin(['Iris-versicolor'])]
IrisVirginicaGroup = df[df["class"].isin(['Iris-virginica'])]


print(IrisVirginicaGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
))
#print(IrisSetosaGroup)
#print(IrisVersicolorGroup)
#print(IrisVirginicaGroup)
print(IrisVirginicaGroup[listofCols].head(2))
