import polars as pl
import matplotlib.pyplot as plt
import datetime
def loadDf(path):
    df = pl.read_csv(path)
    return df


def describeData(df):
    return df.describe()

## helper function to plot
def plot(x, y, ylabel, title):
    x = [i for i in x]
    y = [i for i in y]
    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.ylabel(ylabel)
    plt.xticks( rotation=25 )
    plt.title(title if title is not None else "")
    plt.show()
    plt.savefig(f"./{title}_plot.png")

if __name__=='__main__':
    df = loadDf("./taker_buy_sell_volume.csv")
    df['datetime']=df['timestamp'].apply(lambda x:datetime.datetime.fromtimestamp(x//1000))

    plot(x=df["datetime"], y=df["buy_vol"], ylabel="BTC",title="buy_vol")

    plot(x=df["datetime"], y=df["sell_vol"], ylabel="BTC",title="sell_vol")

    plot(x=df["datetime"], y=df["buy_sell_ratio"], ylabel="Ratio",title = "buy_sell_ratio")