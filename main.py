import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({'371dc01e8dc14ff581b060330c3a8dac': [-1, 0, 2.5],
                   'd25581a263154e49bcbed1a2a53bfa89': ['foo', 'bar', 'baz'],
                   '70a5e270b2ae4d71aae4606fb29be3ca': [True, False, True]})

table = pa.Table.from_pandas(df)
pq.write_table(table, 'my-own.parquet')
