from utils import StockAPI
import streamlit as st

# Initialize the web application
st.set_page_config(page_title="Stock Market Project" , layout="wide")

# import stock api client
client = StockAPI()

# add title to web page
st.title("Stock Market Project")

# add author name as subheader
st.subheader("by Rohan Biradar")

# add company as input
company = st.text_input("Company Name :")

# if company name is inputed then 
if company:
    # get the symbol
    search = client.symbol_search(company)
    options = st.selectbox("company symbol",options=search.keys())
    selected = search[options]
    
    #display the name region  and currency
    st.success(f"Name : {selected[0]}")
    st.success(f"Region : {selected[1]}")
    st.success(f"Currency : {selected[2]}")
    
    # create a submit button
    submit = st.button("Submit",type="primary")

    # after pressing the submit button
    if submit:
        df= client.get_daily_prices(options)
        fig = client.plot_candlestick(df)
        st.plotly_chart(fig)
   

