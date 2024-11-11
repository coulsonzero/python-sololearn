# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

def plt_series():
    s = pd.Series([18, 42, 9, 32, 81, 64, 3])
    s.plot(kind="bar")
    plt.show()
    plt.savefig("plot.png")
    

def plt_dataframe():
    data = {
        "sport": ["Soccer", "Tennis", "Soccer", "Hockey"],
        "players": [5, 4, 8, 20]
    }
    df = pd.DataFrame(data)
    df.groupby("sport")["players"].sum().plot(kind="pie")
    plt.show()

def plt_pandas():
    df = pd.read_csv("ca-covid.csv")
    df.drop("state", axis=1, inplace=True)

    df["date"] = pd.to_datetime(df['date'], format="%d.%m.%y")
    df["month"] = df["date"].dt.month
    df.set_index("date", inplace=True)

    # one
    # df[df["month"] == 12]["cases"].plot()
    # plt.show()
    # plt.savefig("plot.png")

    # two
    # df[df["month"] == 12][["cases", "deaths"]].plot()
    # plt.show()

    # bar
    # (df.groupby("month")["cases"].sum().plot(kind="bar"))
    # plt.show()

    # df = df.groupby("month")[["cases", "deaths"]].sum()
    # df.plot(kind="bar", stacked=True)
    # plt.show()

    # pie
    # df.groupby("month")["cases"].sum().plot(kind="pie")
    # plt.show()

    # line
    # df = df[df["month"] == 6]
    # df[["cases", "deaths"]].plot(kind="line", legend=True)
    # plt.xlabel("Days in June")
    # plt.ylabel("Number")
    plt.suptitle("Covid-19 in June")
    # plt.show()

    # box
    # df[df["month"] == 6]["cases"].plot(kind="box")
    # plt.show()

    # hist
    # df[df["month"] == 6]["cases"].plot(kind="hist")
    # plt.show()

    # area
    # df[df["month"] == 6][["cases", "deaths"]].plot(kind="area", stacked=False)
    # plt.show()

    # scatter
    # df[df["month"] == 6][["cases", "deaths"]].plot(kind="scatter", x="cases", y="deaths")
    # plt.show()


if __name__ == '__main__':
    plt_dataframe()


