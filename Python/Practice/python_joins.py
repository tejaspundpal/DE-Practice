# Example 1: Dynamic SQL WHERE clause from dictionary (Finance - Transaction Filtering)
filters = {
    "account_id": "12345",
    "status": "active",
    "amount": "> 1000"
}
where_conditions = [f"{k} = '{v}'" if not v.startswith(">") else f"{k} {v}" for k, v in filters.items()]
query = f"SELECT * FROM transactions WHERE {' AND '.join(where_conditions)}"
print(query)

# Example 2: Generating CSV header from list (Retail - Product Export)
columns = ["product_id", "name", "price", "stock"]
csv_header = ",".join(columns)
print(csv_header)

# Example 3: Creating email recipient string from list (HR - Notification System)
recipients = ["alice@company.com", "bob@company.com", "carol@company.com"]
email_to = ";".join(recipients)
print(email_to)

print("\n")
#example 4
query = "SELECT t.*, a.account_name FROM transactions t JOIN accounts a ON t.account_id = a.account_id"
filters_for_query = [{"account_id": "act12345", "status": "pending"}, {"status": "active"}, {"amount": "> 1000"}]
final_filter_query = []
for filter in filters_for_query:
    for k, v in filter.items():
        if not v.startswith(">"):
            final_filter_query.append(f"{k} = '{v}'")
        else:
            final_filter_query.append(f"{k} {v}")

final_filter_query = [" OR ".join(final_filter_query)]

print(final_filter_query)
print("\n")

final_query = f"{query} WHERE {' AND '.join(final_filter_query)}"
print(f' Final Query : {final_query}')