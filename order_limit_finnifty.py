from kite_trade import *




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NFO:FINNIFTY24FEB20800CE"))

import time
for i in range(1):
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol="FINNIFTY24FEB20800CE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=40,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=0.10,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
    print(order)
