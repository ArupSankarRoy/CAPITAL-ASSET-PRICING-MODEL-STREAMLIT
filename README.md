# CAPM Data Visualization and Calculation

![project-2](https://github.com/ArupSankarRoy/CAPITAL-ASSET-PRICING-MODEL-STREAMLIT/assets/115450599/38cc5bdb-a27d-4ec5-b905-b62fe0506295)

This Streamlit app is designed to help you explore the Capital Asset Pricing Model (CAPM) by visualizing stock prices, calculating beta values, and estimating returns.

## Overview

The app allows you to:

1. Select up to 4 stocks of your choice.
2. Choose the number of years for historical data.
3. View a dataframe displaying the selected stock prices and S&P 500 data.
4. Visualize stock prices over time and after normalization.
5. Calculate and display the beta values for each selected stock.
6. Estimate returns using the CAPM formula.

## Usage

1. **Stock Selection:**
   - Use the multiselect dropdown to choose up to 4 stocks from options like TSLA, AAPL, AMZN, and more.
   
2. **Data Range:**
   - Input the number of years you want to consider for historical data.

3. **Data Visualization:**
   - Explore the dataframes showing stock prices, normalized prices, beta values, and estimated returns.
   - Visualize stock prices using interactive charts.

4. **Understanding Results:**
   - The app calculates beta values, representing the stocks' sensitivity to market movements.
   - Estimated returns are computed using the CAPM formula.

## Instructions for Running Locally

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/ArupSankarRoy/CAPITAL-ASSET-PRICING-MODEL-STREAMLIT.git
   cd capm-app
   ```

2. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to view and interact with the app.

## Note

- Ensure that you have Python installed on your machine.
- The app uses Streamlit, pandas, yfinance, and other libraries. Install any additional dependencies as needed.


