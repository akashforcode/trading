import tkinter as tk
from kite_trade import *
 


def func(kite):
    print(kite.margins())
    print(kite.ltp("NSE:TRIDENT"))






import time
for i in range(1):
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NSE,
                              tradingsymbol="TRIDENT",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=1,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
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
button_buy = tk.Button(frame_2, text='Buy', command=lambda: func("See this worked!"))
button_buy.pack(side=tk.LEFT)
button_sell = tk.Button(frame_2, text='Sell')
button_sell.pack(side=tk.RIGHT)
 
window_main.mainloop()
