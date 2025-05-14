# Calgary Crime Forecast  
**Data Analytics Project**

## 🧭 Goal  
Predict crime occurrences in Calgary using machine learning and historical crime data.  
The objective was to identify **seasonal** and **geographic patterns** to help local authorities make informed decisions for **resource allocation** and **crime prevention strategies**.

## 🛠️ Key Technologies and Tools

- **Programming:** Python (Pandas, NumPy)  
- **Data Visualization:** Power BI, Matplotlib, Seaborn  
- **Development Environment:** Visual Studio Code, Jupyter Notebook, GitHub

## 📌 Project Highlights

- Collected and prepared historical crime data from Calgary’s open data portal.
- Performed exploratory data analysis to examine:
  - Distribution of crime types over time.
  - Patterns in specific sectors and communities.
- Created an interactive dashboard in Power BI featuring:
  - **Bar and line charts** showing monthly and yearly crime trends.
  - **Filters** to explore data by crime type, community, year, and month.
  - **Custom visuals** to support stakeholder decision-making.
- Built machine learning models in Python to forecast crime trends using time-series analysis.
- Shared the project through GitHub and Power BI Service for broader accessibility.

## 📊 Key Insights

- 🔁 **Seasonality:** Crime rates were higher during spring and summer, and lower during colder months.
- 📍 **High-Crime Areas:** Communities such as **Downtown Commercial Core** and **Beltline** showed consistently high crime rates.
- 🔮 **Forecasting:** The model successfully identified expected crime increases during holidays and weekends.

## 📸 Dashboard Snapshot

![Calgary Crime Dashboard](./dashboard_snapshot.png) 

## 🚀 Next Steps

- Add external variables (e.g. weather, events, demographics) to enrich predictive power.
- Automate dashboard updates and model retraining using new data.
- Share insights with public safety officials for operational planning.

## 📈 Forecasting Methodology

To predict monthly crime occurrences for 2024, a time series forecasting model was developed using Python and the **ARIMA** algorithm:

### 🔧 Steps Followed

1. **Data Preparation**
   - Created a `Date` column combining `Year` and `Month`.
   - Removed the last month of data to avoid partial/incomplete records.
   - Aggregated monthly crime counts to create a clean time series.

2. **Train-Test Split**
   - Data was split into:
     - **Training Set:** up to December 2023
     - **Testing Set:** from January 2024 onward

3. **Model Building**
   - Used the ARIMA model with configuration:
     ```
     order=(0, 2, 1)
     seasonal_order=(1, 1, 1, 12)
     ```
   - Model diagnostics were generated to evaluate residuals.

4. **Forecasting**
   - Forecasted crime counts for the 12 months of 2024.
   - Rounded and compared predicted vs. actual values.
   - Calculated both the absolute and percentage differences.

5. **Visualization**
   - Created a custom line plot with:
     - Training data
     - Actual values (2024)
     - Forecasted values
   - Styled using a light gray background and clean borders to enhance readability.

### 📉 Forecast Output

| Month | Forecast | Actual | Difference | Difference % |
|-------|----------|--------|------------|---------------|
| Jan   | 2341     | 2402   | -61        | -3%           |
| Feb   | ...      | ...    | ...        | ...           |

*A full table is available in the Jupyter notebook.*

---

This methodology helped evaluate the feasibility of crime forecasting in Calgary and supported a data-driven approach to public safety planning.


