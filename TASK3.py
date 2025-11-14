import pandas as pd
df = pd.read_csv("train.csv")

total_sal = df['Sales'].sum()
prod_sal = df.groupby('Product Name')['Sales'].sum()
bst_prod = prod_sal.idxmax()
bst_prod_sal= prod_sal.max()

print("----- Sales Report -----")
print(f"Total Sales: {total_sal}")
print(f"Best Selling Product: {bst_prod}")
print(f"Sales of Best Product: {bst_prod_sal:.2f}")