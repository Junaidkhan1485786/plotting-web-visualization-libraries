import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# Add a title
st.markdown("<h1 style='text-align: center; color: blue;'>Stock Price Chart</h1>", unsafe_allow_html=True)

# Get a list of stock symbols
stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

# Add a title for the dropdown
st.sidebar.markdown("<h3>Select a stock</h3>", unsafe_allow_html=True)

# Create a dropdown menu for stock selection
selected_stock = st.sidebar.selectbox('', stocks)

# Retrieve the stock data using Yahoo Finance API
stock_data = yf.download(selected_stock, start='2022-01-01', end='2022-12-31')

# Create a line chart for the stock's closing prices using Plotly
fig = go.Figure(data=go.Scatter(x=stock_data.index, y=stock_data['Close']))
fig.update_layout(title=f'{selected_stock} Stock Price',
                xaxis_title='Date',
                yaxis_title='Close Price')

# Display the chart
st.plotly_chart(fig)
