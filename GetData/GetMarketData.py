
import pandas as pd
import yfinance as yf
import datetime
import matplotlib as plt
import matplotlib.dates as mdates



import pandas_datareader as pdr


#Data viz
import plotly.graph_objs as go

Symbols = ['AAPL']


def YfinanceData(Symbols):
    # Interval required 5 minutes
    start = datetime.datetime(2021, 12, 1)
    for Symbol in Symbols:
        Yfinance_DataFrame = yf.download(tickers=Symbol, interval='1d', start= start)
        Yfinance_DataFrame['Symbol'] = Symbol

    return Yfinance_DataFrame


def YFinanceDataReader(Symbols):
    df = pdr.DataReader("AAPL",
                        start='2010-12-1',
                        end='2022-05-14',
                        data_source='yahoo')

    df.index = mdates.date2num(df.index)
    data = df.reset_index().values  # Convert dataframe into 2-D list

    plt.style.use('ggplot')

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18.5, 7.0)

    ### Subplot 1 - Semi-logarithmic ###
    plt.subplot(121)
    plt.grid(True, which="both")

    # Linear X axis, Logarithmic Y axis
    plt.semilogy(df.index, df['Close'], 'r')
    plt.ylim([10, 500])

    plt.xlabel("Date")
    plt.title('Semi-logarithmic scale')
    fig.autofmt_xdate()

    ### Subplot 2 - Arithmetic ###
    plt.subplot(122)

    plt.plot(df.index, df['Close'], 'b')

    plt.xlabel("Date")
    plt.title('Arithmetic scale')
    fig.autofmt_xdate()

    # show plot
    plt.show()