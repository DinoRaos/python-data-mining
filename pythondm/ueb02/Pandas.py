import pandas as pd


def better_print(df, str):
    print(str)
    print(df)
    print()


# A1
# 1.1
df = pd.DataFrame(data=[[1, 5, 9, 5],
                        [10, 1, 3, 10],
                        [8, 2, 4, 9]])
better_print(df, 1.1)

# 1.2
df.columns = ["Eigenschaft A", "Eigenschaft B", "Eigenschaft C", "Userbewertung"]
index_abc = ["Produkt A", "Produkt B", "Produkt C"]
df.index = index_abc

better_print(df, "1.2")
better_print(df.dtypes, "1.2")

print("---------------------------------------------------------------------------------------------")

# A2
# 2.1
better_print(df["Eigenschaft B"], "2.1 (1)")
better_print(df.loc["Produkt B"], "2.1 (2)")
better_print(df.loc["Produkt A", "Userbewertung"], "2.1 (3)")
better_print(df[df["Eigenschaft C"] > 3], "2.1 (4)")
better_print(df[df["Userbewertung"] > 5]["Eigenschaft B"], "2.1 (5)")

# 2.2
df.index = range(0, len(df))
better_print(df, "2.2")
better_print(df.head(1), "first")
better_print(df.tail(1), "last")
df.reset_index()

# 2.3
df_one = pd.DataFrame(index=range(0, 4), columns=["X", "Y"])
df_two = pd.DataFrame(index=range(6, 9), columns=["X", "Y"])

# axis {0/’index’, 1/’columns’}, default 0
better_print(df_one, "2.3 row")
print(pd.concat([df_one, df_two], axis=0))

print()
better_print(df_two, "2.3 column")
print(pd.concat([df_one, df_two], axis=1))

print("---------------------------------------------------------------------------------------------")

# A3
# 3.1
df.index = index_abc
for row in range(len(df)):
    better_print(df.iloc[[row]], row)

# 3.2
print()
for col in df.columns:
    better_print(df[col], col)

# 3.3
doubled_df = df.map(lambda row: row * 2)
better_print(doubled_df, "3.3 double df")
print(df)


# 3.4
def classify_number(num):
    if num < 3:
        return "low"
    elif num < 8:
        return "medium"
    else:
        return "high"


str_df = df.map(lambda x: classify_number(x))
better_print(str_df, "3.4 Converted to String")

print("---------------------------------------------------------------------------------------------")

# A4
# 4.1
sales_df = pd.read_csv("Sales_April_2019.csv")
better_print(sales_df.head(10), "4.1 Sales April 2019")

# 4.2
isna_output = sales_df.isna()
better_print(isna_output, "4.2 isna()")
better_print(isna_output.value_counts(), "4.2 value_counts() on isna()")

# 4.3
sales_df_dropna = sales_df.dropna()
better_print(sales_df_dropna.head(), "4.3 dropna()")

# 4.4
better_print(sales_df.head().to_string(), "4.4 NaN Price Each")
sales_df = sales_df.dropna(subset=["Price Each"])
better_print(sales_df.head().to_string(), "Price Each")

print("---------------------------------------------------------------------------------------------")

# A5
# 5.1 (openpyxl)
df_excel = pd.read_excel("Kundendaten.xlsx")
better_print(df_excel.head(), "5.1 Kundendaten")

# 5.2
better_print(df_excel[df_excel["Kundennummer"] == 22], "5.2 Rechnung Kundennummer 22")

# 5.3
better_print(df_excel[df_excel["Umsatz netto"] > 5], "5.3 Umsatz netto > 5")

# 5.4
better_print(df_excel[df_excel["Kundennummer"] == 22].sum(axis=0, numeric_only=True), "5.4 Summe Umsatz")

# 5.5
better_print(df_excel.groupby("Kundennummer").agg({"Umsatz netto": "sum", "Umsatz brutto": "sum"}), "5.5 groupby/agg")
