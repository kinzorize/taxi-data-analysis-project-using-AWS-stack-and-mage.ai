import pandas as pd

parquet_doc = "/Users/ghost/Downloads/yellow_tripdata_2022-01.parquet"

df = pd.read_parquet(parquet_doc)


df.head()


csv_output = "/Users/ghost/Downloads/yellow_tripdata_2022-01.csv"

df.to_csv(csv_output, index=False)

df.info()
