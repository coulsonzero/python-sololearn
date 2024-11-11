import pandas as pd

"""
df = pd.DataFrame(data)
df = pd.DataFrame(data, index = ["James", "Bob", "Amy", "Dave"])
print(df)
print(df["ages"])
print(df[["ages", "heights"]])
print(df.loc["Bob"])
print(df.iloc[2])
print(df.iloc[:3])
print(df[(df["ages"] > 18) & (df["heights"] > 180)])

# scv
df = pd.read_csv("ca-covid.csv")
df.set_index("date", inplace=True)
df.drop("state", axis=1, inplace=True)  
df["month"] = pd.to_datetime(df["date"], format="%d.%m.%y").dt.month_name()
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df["month"].value_counts())
print(df["cases"].sum())
print(df.groupby("month")["cases"].sum())
"""

def pandas_dataframe():
    data = {
        "ages": [14, 18, 24, 42],
        "heights": [165, 180, 176, 184]
    }

    df = pd.DataFrame(data)
    print(df)
    '''
       ages  heights
    0    14      165
    1    18      180
    2    24      176
    3    42      184
    '''
    df = pd.DataFrame(data, index = ["James", "Bob", "Amy", "Dave"])
    print(df)
    '''
           ages  heights
    James    14      165
    Bob      18      180
    Amy      24      176
    Dave     42      184
    '''


def pandas_index_slice():
    data = {
        "ages": [14, 18, 24, 42],
        "heights": [165, 180, 176, 184]
    }
    df = pd.DataFrame(data, index=["James", "Bob", "Amy", "Dave"])

    print(df["ages"])
    '''
    James    14
    Bob      18
    Amy      24
    Dave     42
    Name: ages, dtype: int64
    '''
    print(df[["ages", "heights"]])
    '''
           ages  heights
    James    14      165
    Bob      18      180
    Amy      24      176
    Dave     42      184
    '''

    print(df.loc["Bob"])
    '''
    ages        18
    heights    180
    Name: Bob, dtype: int64
    '''
    print(df.iloc[2])
    '''
    ages        24
    heights    176
    Name: Amy, dtype: int64
    '''
    print(df.iloc[:3])
    '''
           ages  heights
    James    14      165
    Bob      18      180
    Amy      24      176
    '''

    print(df[(df["ages"] > 18) & (df["heights"] > 180)])
    '''
          ages  heights
    Dave    42      184
    '''


def pandas_csv():
    # df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
    df = pd.read_csv("ca-covid.csv")
    # print(df)
    '''
             date       state  cases  deaths
    0    25.01.20  California      1       0
    1    26.01.20  California      1       0
    2    27.01.20  California      0       0
    3    28.01.20  California      0       0
    4    29.01.20  California      0       0
    ..        ...         ...    ...     ...
    337  27.12.20  California  37555      62
    338  28.12.20  California  41720     246
    339  29.12.20  California  34166     425
    340  30.12.20  California  32386     437
    341  31.12.20  California  32264     574
    '''

    # print(df.head())    # 只显示前5 rows
    '''
           date       state  cases  deaths
    0  25.01.20  California      1       0
    1  26.01.20  California      1       0
    2  27.01.20  California      0       0
    3  28.01.20  California      0       0
    4  29.01.20  California      0       0
    '''

    print(df.info())
    '''
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 342 entries, 0 to 341
    Data columns (total 4 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   date    342 non-null    object
     1   state   342 non-null    object
     2   cases   342 non-null    int64 
     3   deaths  342 non-null    int64 
    dtypes: int64(2), object(2)
    memory usage: 10.8+ KB
    None
    '''

    df.set_index("date", inplace=True)
    print(df.head())
    '''
                   state  cases  deaths
    date                               
    25.01.20  California      1       0
    26.01.20  California      1       0
    27.01.20  California      0       0
    28.01.20  California      0       0
    29.01.20  California      0       0
    '''
    df.drop("state", axis=1, inplace=True)
    df.info()
    '''
    <class 'pandas.core.frame.DataFrame'>
    Index: 342 entries, 25.01.20 to 31.12.20
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   cases   342 non-null    int64
     1   deaths  342 non-null    int64
    dtypes: int64(2)
    memory usage: 8.0+ KB
    '''
    print(df.head())
    '''
              cases  deaths
    date                   
    25.01.20      1       0
    26.01.20      1       0
    27.01.20      0       0
    28.01.20      0       0
    29.01.20      0       0
    '''

def pandas_column():
    df = pd.read_csv("ca-covid.csv")
    df.drop("state", axis=1, inplace=True)
    print(df.head())
    '''
           date  cases  deaths
    0  25.01.20      1       0
    1  26.01.20      1       0
    2  27.01.20      0       0
    3  28.01.20      0       0
    4  29.01.20      0       0
    '''
    df["month"] = pd.to_datetime(df["date"], format="%d.%m.%y").dt.month_name()
    df.set_index("date", inplace=True)
    print(df.head())
    '''
              cases  deaths    month
    date                            
    25.01.20      1       0  January
    26.01.20      1       0  January
    27.01.20      0       0  January
    28.01.20      0       0  January
    29.01.20      0       0  January
    '''
    print(df.describe())
    '''
                  cases      deaths
    count    342.000000  342.000000
    mean    6747.862573   75.921053
    std    10023.201267   76.639861
    min        0.000000   -5.000000
    25%     1352.250000   22.000000
    50%     3462.500000   62.500000
    75%     7637.250000  104.000000
    max    64987.000000  574.000000
    '''
    print(df["month"].value_counts())
    '''
    month
    March        31
    May          31
    July         31
    August       31
    October      31
    December     31
    April        30
    June         30
    September    30
    November     30
    February     29
    January       7
    Name: count, dtype: int64
    '''

    print(df.groupby("month")["cases"].sum())
    '''
    month
    April          41887
    August        210268
    December     1070577
    February          25
    January            3
    July          270120
    June          119039
    March           8555
    May            62644
    November      301944
    October       114123
    September     108584
    Name: cases, dtype: int64
    '''
    print(df["cases"].sum())    # 2307769

def pandas_covid19():
    df = pd.read_csv("ca-covid.csv")
    df.drop("state", axis=1, inplace=True)
    df.set_index("date", inplace=True)

    df["ratio"] = df["deaths"] / df["cases"]
    print(df[df["ratio"] == df["ratio"].max()])
    '''
              cases  deaths     ratio
    date                             
    10.03.20      7       1  0.142857
    '''

if __name__ == '__main__':
    pandas_covid19()