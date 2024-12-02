from tradingview_ta import *

bitcoin = TA_Handler(
    symbol="BTCUSD",
    exchange="BITSTAMP",
    screener="crypto",
    interval="1m",
    timeout=None
)
totalgain = 0
def buy(priceTB):
    global price
    print("buy at " + str(priceTB))
    return priceTB

def sell(priceTS, priceTB1):
    global totalgain
    gain = (priceTS - priceTB1) / priceTB
    totalgain = totalgain + gain
    print("sell at " + str(priceTS) + " with " + str(gain) + "% gain this is "+ totalgain +"% total gain.")


while True:
    trade = False
    price = bitcoin.get_indicators()['close']
    rsi = bitcoin.get_indicators()['RSI']
    sma = bitcoin.get_indicators()['SMA20']
    print(sma < price)
    if trade == False :
        if rsi < 41 and sma < price:
            trade = True
            price = bitcoin.get_indicators()['close']
            rsi = bitcoin.get_indicators()['RSI']
            priceTB = buy(price)
            while trade:
                price = bitcoin.get_indicators()['close']
                rsi = bitcoin.get_indicators()['RSI']
                sma = bitcoin.get_indicators()['SMA20']
                if rsi > 59 and sma > price:
                    sell(price, priceTB)
                    trade = False
