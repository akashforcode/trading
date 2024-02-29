from tkinter import*

currentsum=0
from tkinter import *
from tkinter import messagebox
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
##########BANKNIFTY2430646600CE

import time
def buy_option():
    for i in range(1):
        print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NSE,
                              tradingsymbol=e2.get(),
                              #tradingsymbol="BANKNIFTY2430646600CE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=e1.get(),
                              #quantity=15*e1.get(),
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


def sell_option():
    for i in range(1):
        print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=e2.get(),
                              #tradingsymbol="BANKNIFTY2430646600CE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=e1.get(),
                              #quantity=15*e1.get(),
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=600.00,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)



#buy_option(1)
#sell_option(1)
def addition():
   global currentsum # New
   currentsum+=float(e1.get()) # Fix
   #e1.insert(INSERT,str(currentsum))
   l2['text'] = str(currentsum) # Change

def subtraction():
   global currentsum # New
   currentsum=currentsum-float(e1.get())
   #e1.insert(INSERT,str(currentsum))
   l2['text'] = str(currentsum) # Change

def reset():
   global currentsum # New
   currentsum=0
   #e1.insert(INSERT,str(currentsum))
   l2['text'] = str(currentsum) # Change
window=Tk()
window.title("Nifty50")
window.geometry("350x150")



l1=Label(window,text="Quantity:")
l1.grid(row=0, column=0)
#l2=Label(window,text=str(currentsum))
l2=Label(window)
l2.grid(row=0,column=1)
l3=Label(window,text="Strike_Price")
l3.grid(row=3, column=0)


e1=Entry(window)
e1.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=4,column=0)


b1=Button(window,text="BUY++",command=buy_option)
b2=Button(window,text="SELL--",command=sell_option)
b3=Button(window,text="RESET",command=reset)
b1.grid(row=5,column=0)
b2.grid(row=5,column=1)
b3.grid(row=5,column=2)

window.mainloop()