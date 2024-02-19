from kite_trade import *




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

enctoken = "4MrFxrhhBKQha78Ke7pPlVH+4vyCgmBPzs1yk5wiaIzXcIq4KYfekIp+bg6jRD5wL/CkFUFRoeQyzoHRPdVALvmXrLbHCur68qAidoAht+w6UCSRxfmThg=="
kite = KiteApp(enctoken=enctoken)


# Modify order
kite.modify_order(variety=kite.VARIETY_REGULAR,
                  order_id="order_id",
                  parent_order_id=None,
                  quantity=5,
                  price=2600,
                  order_type=kite.ORDER_TYPE_LIMIT,
                  trigger_price=2650,
                  validity=kite.VALIDITY_DAY,
                  disclosed_quantity=5)

print(order)
