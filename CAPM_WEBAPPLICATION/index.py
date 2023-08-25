import datetime

# CAPM (CAPITAL ASSET PRICING MODEL):
#
#  CAPM is a model that describes the relationship between the expected return and risk securities.
#  CAPM indicates that the expected return on a security is equal to risk-free return plus a risk premium.
#
#             ri = rf + Bi(rm - rf) where ri = Expected return on a security.
#                                         rf = Risk free rate of return.
#                                         Bi = Beta between the stock and market.
#                                         rm = Expected return on the market.
#                                         (rm - rf) = Risk premium.
#
# RISK FREE ASSET RETURN :
#
#  Investors who are extremely risk averse would prefer to buy the risk free asset to protect their money and earn a
#  low return.If Investors are interested in gaining more return, They have to bear more risk compared to the risk free asset.
#  A risk free asset could be a US govt 10 year Treasury Bill.
#
# MARKET PORTFOLIO RETURN :
#
#  Market portfolio includes all securities in the market. A good representation of the market portfolio in the S&P 500
#  Market postfolio return is the average return of the overall return of the SP500.
#
# BETA :
#
#  It's a measure of the stock's risk reflected by measuring the fluctuation of it's price changes relative to the overall market.
#
#        B = 0 : NO MARKET SENSITIVITY. (this basically relationship between MARKET and STOCK)
#        B < 1 : LOW MARKET SENSITIVITY.(security is Less volatile than the market)
#        B = 1 : NEUTRAL. (increasing of the Market stock is also increase)
#        B > 1 : HIGH MARKET SENSITIVITY.
#        B < 0 : NEGATIVE MARKET SENSITIVITY.


# importing libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import capm_functions

st.set_page_config(page_title = "CAPM" , page_icon = "chart_with_upwards_trend" , layout="wide")

import streamlit as st

# Use Markdown to style the title
st.markdown("<h1 style='text-align: center; color: #ff00ff;'>CAPITAL ASSET PRICING MODEL</h1>", unsafe_allow_html=True)

# getting input from the user

col1 , col2 = st.columns([1 , 1]) # equal width [width , width]

with col1 :

 stocks_list = st.multiselect("Choose 4 stocks" , ["TSLA" , "AAPL" , "NFLX" , "MSFT" , "AMZN" , "GOOGL" , "NVDA" , "MGM" , "WMT" , "NKE"] , ["TSLA" , "AAPL" , "AMZN" , "GOOGL"])

with col2 :

 year = st.number_input("Number of Years" , 1 , 10)

# downloading data from SP500

try:
 end = datetime.date.today()

 start = datetime.date(datetime.date.today().year - year , datetime.date.today().month , datetime.date.today().day)

 sp500 = web.DataReader(['sp500'] , 'fred' , start , end)

 stocks_df = pd.DataFrame()

 for stock in stocks_list:

  data = yf.download(stock , period = f"{year}y")
  stocks_df[f"{stock}"] = data['Close']

 stocks_df.reset_index(inplace=True)
 sp500.reset_index(inplace = True)
 sp500.columns = ['Date' , 'sp500'] # For changing sp500 col name 'DATE' to 'Date'

 stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]') # For merge from datetime64[ns , America/NewYork] to datetime64[ns]
 stocks_df['Date'] = stocks_df['Date'].apply(lambda x : str(x)[:10]) # For split time from date. 1st step convert date-time[Ex: 2022-05-19 12:00:30] to str
                                                                     # Then we only select the 1st 10 digits that is date and lambda func return that .

 stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
 stocks_df = pd.merge(stocks_df , sp500 , on = 'Date' , how = 'inner')

 col1 , col2 = st.columns([1 , 1])

 with col1:
  st.markdown("### Dataframe Head")
  st.dataframe(stocks_df.head() , use_container_width=True)

 with col2:
  st.markdown('### Dataframe Tail')
  st.dataframe(stocks_df.tail(), use_container_width=True)


 col1 , col2 = st.columns([1 , 1])

 with col1:

  st.markdown("### Price of all the stocks")
  st.plotly_chart(capm_functions.interactive_plot(stocks_df))

 with col2:

  st.markdown("### Price of all the stocks(After Normalizing)")
  st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)))

 stocks_daily_return =  capm_functions.daily_return(stocks_df)
 print(stocks_daily_return)

 beta = {}
 alpha = {}

 for i in stocks_daily_return.columns:

  if i != 'Date' and i != 'sp500':
    b , a = capm_functions.calculate_beta(stocks_daily_return , i)

    beta[i] = b
    alpha[i] = a

 print( beta , alpha)

 beta_df = pd.DataFrame(columns=['Stock' , 'Beta Value'])
 beta_df['Stock'] = beta.keys()
 beta_df['Beta Value'] = [str(round(i , 2)) for i in beta.values()]

 with col1:

  st.markdown('### Calculated Beta Value')
  st.dataframe(beta_df , use_container_width=True)

 # For calculating return

 rf = 0

 rm = stocks_daily_return['sp500'].mean()*252 # Market portfolio return

 return_df = pd.DataFrame()

 return_value = []

 for stock , value in beta.items():

  return_value.append(str(round(rf + (value * (rm-rf)) , 2)))

 return_df['Stock'] = stocks_list
 return_df['Return Value'] = return_value

 with col2:

  st.markdown('### Calculated return using CAPM')
  st.dataframe(return_df , use_container_width=True)

except:

 st.write('Please select valid input :(')







