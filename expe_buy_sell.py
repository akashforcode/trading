from kite_trade import *




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NSE:TRIDENT"))

import time
def buy_option(qaunt):
    for i in range(1):
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NSE,
                              tradingsymbol="TRIDENT",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=qaunt,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=43.00,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option(quant):
    for i in range(1):
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NSE,
                              tradingsymbol="TRIDENT",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=quant,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=43.00,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)



buy_option(1)
sell_option(1)




