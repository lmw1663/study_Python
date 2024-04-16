import pandas as pd

# Read the CSV file from the URL (using the GitHub raw version link)
url = "https://raw.githubusercontent.com/WillKoehrsen/automated-feature-engineering/master/walk_through/data/loans.csv"

# Read the CSV file into a DataFrame
loans = pd.read_csv(url)
clients = pd.read_csv("https://raw.githubusercontent.com/WillKoehrsen/automated-feature-engineering/master/walk_through/data/clients.csv")

# Group loans by client id and calculate sum of loans

total_loan_amount = loans.groupby('client_id')['loan_amount'].agg('sum')
total_loan_amount = pd.DataFrame(total_loan_amount)
# Rename the columns
total_loan_amount.columns = ['total_loan_amuont']

# Merge with the clients dataframe
stats = clients.merge(total_loan_amount, left_on='client_id', right_index=True, how='left')
print(loans.head(10))
print(clients.head(10))
# Display the first 10 rows
print(stats.head(10))

