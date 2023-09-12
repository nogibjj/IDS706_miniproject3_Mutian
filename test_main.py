from main import *

def test_func():
    df = loadDf("./taker_buy_sell_volume.csv")
    descriptive_df = describeData(df)
    assert isinstance(df, pl.DataFrame)
    #assert 'max' in descriptive_df.index
    #assert df.shape[0]==89
    print(descriptive_df)
    print(df)
    #plotData(df)
test_func()