import pandas as pd
from datetime import datetime, timedelta

def filter_customers(df):
    # Calculate the date 6 months ago from today
    six_months_ago = datetime.now() - timedelta(days=6*30)
    
    # Filter purchases made in the last 6 months
    recent_purchases = df[df['purchase_date'] >= six_months_ago]
    print("recent_purchasesr : ",recent_purchases)
    print("\n")
    # Count purchases per customer
    purchase_counts = recent_purchases['customer_id'].value_counts()
    print("purchase_counts:",purchase_counts)
    print("\n")
    # Filter customers with more than 5 purchases
    frequent_customers = purchase_counts[purchase_counts > 5].index
    
    return df[df['customer_id'].isin(frequent_customers)]

# Example usage
data = {
    'customer_id': [1, 2, 1, 3, 2, 1, 4, 1, 2, 3, 1, 2, 1],
    'purchase_date': pd.to_datetime([
        '2025-03-01', '2024-11-15', '2024-12-20', '2024-12-25', '2025-01-10',
        '2025-01-15', '2025-02-01', '2025-02-10', '2025-02-15', '2025-03-01',
        '2025-03-15', '2025-03-20', '2025-04-01'
    ])
}
df = pd.DataFrame(data)
filtered_customers = filter_customers(df)
print(filtered_customers)
