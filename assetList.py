from settings import *



# Get S&P 500 constituents from Wikipedia
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_table = pd.read_html(sp500_url)
sp500_df = sp500_table[0]


# Calculate Years Active and Active Flag
sp500_df['Date added'] = pd.to_datetime(sp500_df['Date added'], errors='coerce') #Convert Date added to "year"
current_year = datetime.now().year
sp500_df['Years Active'] = current_year - pd.to_datetime(sp500_df['Date added']).dt.year
sp500_df['Active Flag'] = sp500_df['Years Active'] >= 8


# Extract the ticker symbols from the DataFrame
sp500_symbols = sp500_df['Symbol'].tolist()


# Print the DataFrame containing the S&P 500 constituents
print_break('Data Table')
print(sp500_df)



#ACQUIRE OPEN, CLOSE, HIGH, LOW, DATA