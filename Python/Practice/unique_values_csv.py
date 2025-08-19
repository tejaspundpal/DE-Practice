import pandas as pd

def extract_unique_values(input_csv, column_name, output_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Extract unique values from the specified column
    unique_values = df[column_name].unique()
    
    # Save the unique values to a new CSV file
    unique_df = pd.DataFrame(unique_values, columns=[column_name])
    unique_df.to_csv(output_csv, index=False)

# Example usage
input_csv = 'input.csv'
column_name = 'your_column_name'
output_csv = 'unique_values.csv'
extract_unique_values(input_csv, column_name, output_csv)
