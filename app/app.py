import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
    current_lands = st.multiselect("Which country?", sorted(set(data.country)))

    st.write(data[data.country.isin(current_lands)])

    data.index = data.datum
    f, ax = plt.subplots(figsize=(10, 10))
    for land in current_lands:
        data[data.country == land].value.plot(ax=ax, label=land, logy=True)
    # data[data.country == "Algeria"].value.plot(ax=ax, label="Algeria")

    for i in range(4):
        new_land = st.sidebar.selectbox(
            f"Which other country {i}?", sorted(set(data.country))
        )
        data[data.country == new_land].value.plot(ax=ax, label=new_land, logy=True)

    f.legend()
    st.pyplot(f)


if __name__ == "__main__":
    main()
