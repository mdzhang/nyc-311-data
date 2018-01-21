import json
import pandas as pd

dfs = pd.read_csv(
    './data/311_Service_Requests_from_2011.csv', header=0, nrows=100)

dfs_limited = dfs[[
    'Unique Key',
    'Complaint Type',
    'Descriptor',
    'Incident Zip',
    'City',
]]

rename = lambda x: x.lower().replace(' ', '_')

dfs_renamed = dfs_limited.rename(rename, axis='columns')

dfs_dict = dfs_renamed.to_dict(orient='records')

for df in dfs_dict:
    print(json.dumps({'index': {}}))
    print(json.dumps(df))
