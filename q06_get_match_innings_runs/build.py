# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    df_local = ipl_df[['match_code', 'inning', 'runs']]
    return df_local.groupby(['match_code','inning']).agg(['sum'])


innruns = get_match_innings_runs()
#rint (innruns)
# print type(innruns)
# print innruns.sum()
