import pandas as pd
import streamlit as st
import duckdb


st.title("Playing with Duckdb")
all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Out", "Nov", "Dec"]

df = pd.read_excel("financial_data.xlsx")

df = duckdb.sql(f"""
   UNPIVOT(
        SELECT Scenario, {','.join(all_months)}
        FROM df
        WHERE Year=2023
        and Account='Sales'
        AND business_unit='Software'
    )
    ON {','.join(all_months)}
    INTO
        NAME month
        VALUE sales
""").df()

st.dataframe(df, use_container_width=True)