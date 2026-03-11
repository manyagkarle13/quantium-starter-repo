import pandas as pd

# load all csv files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# combine them
df = pd.concat([df1, df2, df3])

# keep only pink morsels
df = df[df["product"] == "pink morsel"]

# remove $ symbol from price
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# calculate sales
df["sales"] = df["price"] * df["quantity"]

# keep required columns
df = df[["sales", "date", "region"]]

# save final file
df.to_csv("processed_sales.csv", index=False)

print("Data processing complete!")