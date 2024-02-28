from kite_trade import *
import tkinter as tk
from kite_trade import *
 




f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NFO:FINNIFTY24FEB20800CE"))

import time


def buy_option():
    for i in range(1):
        order = kite.place_order(variety=kite.VARIETY_AMO,
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



window_main = tk.Tk(className='Tkinter - TutorialKart')
window_main.geometry("400x200")
 
frame_1 = tk.Frame(window_main, bg='#c4ffd2', width=200, height=50)
frame_1.pack()
frame_1.pack_propagate(0)
 
frame_2 = tk.Frame(window_main, bg='#ffffff', width=200, height=50)
frame_2.pack()
frame_2.pack_propagate(0)
 
#in frame_1
label_1 = tk.Label(frame_1, text='Stocks')

label_1.pack(side=tk.LEFT)
sell = tk.Entry(frame_1)
sell.pack(side=tk.RIGHT)

 
#in frame_2
button_buy = tk.Button(frame_2, text='Buy', command=lambda: buy_option())
button_buy.pack(side=tk.LEFT)
button_sell = tk.Button(frame_2, text='Sell')
button_sell.pack(side=tk.RIGHT)
 
window_main.mainloop()




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

