from kite_trade import *




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("IDEA"))

def get_daily_ohlc_data(symbol):
    function_name = 'TIME_SERIES_DAILY'    
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(symbol,API_KEY)
    r = requests.get(base_url)
    data = r.json()["Time Series (Daily)"]
    return data

