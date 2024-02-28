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

import time
def buy_option():
    for i in range(1):
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NSE,
                              tradingsymbol="TRIDENT",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=1,
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


def sell_option():
    for i in range(1):
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NSE,
                              tradingsymbol="TRIDENT",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=1,
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



#buy_option(1)
#sell_option(1)
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def showMsg():  
    messagebox.showinfo('Message', 'You clicked the Submit button!')

button = Button(tkWindow,
	text = 'buy',
	command = buy_option)  
button.pack()  

button = Button(tkWindow,
	text = 'Sell',
	command = sell_option)  
button.pack()  
  
tkWindow.mainloop()