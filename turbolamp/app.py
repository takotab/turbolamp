import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns


def main():
    st.title("Covid app")
    data = pd.read_csv(
        "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        error_bad_lines=False,
    )
    data = data.drop(columns=["Lat", "Long"])
    data = data.melt(id_vars=["Province/State", "Country/Region"])
    data = pd.DataFrame(data.groupby(["Country/Region", "variable"]).sum())
    data = data.reset_index()
    data["variable"] = pd.to_datetime(data["variable"])
    data = data.rename(columns={"Country/Region": "land"})

    f, ax = plt.subplots(figsize=(30, 15))
    data.index = data["variable"]

    c_land = st.multiselect(
        "Choose a country", sorted(list(set(data.land))), default="Netherlands"
    )
    for c in c_land:
        data[data.land == c].value.plot(ax=ax, label=c)

    # ax.xticks(rotation=70)
    st.pyplot(f)


if __name__ == "__main__":
    main()
