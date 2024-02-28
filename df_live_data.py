from kite_trade import *
import time
import pandas as pd


# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
ldm=pd.DataFrame(kite.margins())
print(ldm)
while True:
    #print(kite.ltp("NSE:RELIANCE"))
    ldr=pd.DataFrame(kite.ltp("NSE:RELIANCE"))
    print(ldr)
    time.sleep(1)

