from kite_trade import *




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("MCX:CRUDEOIL24FEB7500CE"))

order = kite.place_order(variety=kite.VARIETY_AMO,
                         exchange=kite.EXCHANGE_MCX,
                         tradingsymbol="CRUDEOIL24FEB6500CE",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=1,
                         product=kite.PRODUCT_NRML,
                         order_type=kite.ORDER_TYPE_LIMIT,
                         price=105,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeViaPython")

