import polars as pl
import matplotlib.pyplot as plt
import numpy as np
def loadDf(path):
    df = pl.read_csv(path)
    return df


def describeData(df):
    return df.describe()

## helper function to plot
def plot(x, y, ylabel, title):
    x = [i for i in x]
    y = [i for i in y]
    fig = plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.ylabel(ylabel)
    plt.xticks( rotation=25 )
    plt.title(title if title is not None else "")
    plt.show()
    plt.savefig(f"./{title}_plot.png")
