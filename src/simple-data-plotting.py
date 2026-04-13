import pandas as pd
import matplotlib.pyplot as plt

data_file = "src/notebooks/section_1/sales_predictors.csv"

df = pd.read_csv(data_file)

print("First DF")
print(df.head())
print(f"\n")

# clone a dataframe
print("Cloned DF")
df_new = df.iloc[:]
print(df_new)

# Plotting Sales X TV
tv_column = df["TV"]
sales_column = df["Sales"]

plt.scatter(tv_column, sales_column)
plt.xlabel("TV Budget")
plt.ylabel("Sales")
plt.title("Sales x TV")
