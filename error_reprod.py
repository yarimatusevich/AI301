import pandas as pd

# df1 has string index
df1 = pd.DataFrame(
    {"A": [1, 2, 3]},
    index=["1", "2", "3"]   # strings
)

# df2 has integer index (same "values", different type)
df2 = pd.DataFrame(
    {"A": [100, 200, 300]},
    index=[1, 2, 3]         # ints
)

print("BEFORE:")
print(df1)

df1.update(df2)

print("\nAFTER:")
print(df1)
