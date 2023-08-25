import plotly.express as px
import numpy as np

# plotting

def interactive_plot(df):

    fig = px.line()

    for i in df.columns[1:]: # Why 1 not 0 ? beacuse I put 'Date' in x axis

        fig.add_scatter(x = df['Date'] , y = df[i] , name = i)

    fig.update_layout(width = 450 , margin = dict(l=20 , r=20 , t=50 , b=20) ,
                      legend = dict(orientation = 'h' , yanchor = 'bottom'  , y = 1.02, xanchor = 'right' , x = 1 , ))

    return fig

# function to normalize prices based on the initial price

def normalize(df):

    normalize = df.copy()
    for i in df.columns[1:]:

        normalize[i] = df[i] / df[i][0] # suppose TSLA col, it's each price divided to it's 1st value

    return normalize

# function to calclate daily return

def daily_return(df):

    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1 , len(df)):

            df_daily_return[i][j] = ((df[i][j] - df[i][j-1])/ df[i][j-1]) * 100

        df_daily_return[i][0] = 0
    return df_daily_return

# function to calculate beta

def calculate_beta(stocks_daily_return , stock):

    rm = stocks_daily_return['sp500'].mean()*251

    b , a = np.polyfit(stocks_daily_return['sp500'] , stocks_daily_return[stock] , 1)

    return b , a




