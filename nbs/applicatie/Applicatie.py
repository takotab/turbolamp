import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        error_bad_lines=False,
    )
    data = data.drop(columns=["Lat", "Long"])
    data = data.melt(id_vars=["Province/State", "Country/Region"])
    data = pd.DataFrame(data.groupby(["Country/Region", "variable"]).sum())
    data = data.reset_index()
    data["variable"] = pd.to_datetime(data["variable"])

    data = data.rename(columns={"Country/Region": "country", "variable": "datum"})
    current_land = st.sidebar.selectbox("Which country?", sorted(set(data.country)))
    data.index = data.datum
    data_Country = data[data["country"] == current_land]
    data_Country = data_Country[data_Country.index > pd.Timestamp(2020, 3, 1)]

    
    f, ax = plt.subplots(figsize=(10, 10))
    data_Country.value.plot(ax=ax)
    # for land in current_land:
    # data[data.country == st.sidebar.selectbox(str(i)+" Which country do you want to compare it against?", sorted(set(data.country)))].value.plot(ax=ax, label="Second_Country")
    #   data[data.country == land].value.plot(ax=ax, label=land, logy=True)
    for i in range(4):
        new_country = st.sidebar.selectbox(
            f"which other counrty{i}?", sorted(set(data.country))
        )
        new_country

    f.legend()
    st.title("Corona Kaart")
    st.pyplot(f)
    lst_countrys = st.multiselect(
        "which countries do you want in the total deaths?",
        sorted(set(data.country)),
    )
    # st.write(data)
    st.write(data[data.country.isin(lst_countrys)].groupby('country').sum())


if __name__ == "__main__":
    main()
