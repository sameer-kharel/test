import pandas as pd

def combine_files(csv1, csv2, output_file):
    # Read CSV files into pandas DataFrames
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    # Merge DataFrames on the first column
    merged_df = pd.merge(df1, df2, on=df1.columns[0])

    # Concatenate lines and drop the duplicate column from CSV2 Assuming that the first column in CSV1 is the key for merging
    # and the first column in CSV2 is not needed after merging
    merged_df['Result'] = merged_df[df2.columns[1]].astype(str) + merged_df[df2.columns[2]].astype(str)
    merged_df = merged_df.drop(columns=[df2.columns[1]])

    # Write the result to the result file
    # The 'Result' column contains the concatenated lines
    # The 'index=False' parameter avoids writing row indices to the CSV
    merged_df.to_csv(output_file, index=False)

# path of the files 
csv1_path = '1.csv'
csv2_path = '2.csv'
output_path = 'result.csv'

combine_files(csv1_path, csv2_path, output_path)
