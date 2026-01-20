import pandas as pd

# Load the Excel file
excel_file = r'C:\Users\tpundpal\OneDrive - e2open, LLC\Documents\Python\Input\output.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

csv_file = r'C:\Users\tpundpal\OneDrive - e2open, LLC\Documents\Python\output\result.csv'
df.to_csv(csv_file, sep='~', index=False)