from tradingview_ta import *
import time

totalgain = 0

bitcoin = TA_Handler(
    symbol="BTCUSD",
    exchange="BITSTAMP",
    screener="crypto",
    interval="1m",
    timeout=None
)

def main():
    global time
    while True:
        trade = False
        price = bitcoin.get_indicators()['close']
        rsi = bitcoin.get_indicators()['RSI']
        sma20 = bitcoin.get_indicators()['SMA20']
        sma50 = bitcoin.get_indicators()['SMA50']
        sma200 = bitcoin.get_indicators()['SMA200']
        if trade == False :
            if sma20 < sma200:
                time.sleep(150)
                exp = time.time()
                while sma200 > price:
                    price = bitcoin.get_indicators()['close']
                    sma20 = bitcoin.get_indicators()['SMA20']
                    sma50 = bitcoin.get_indicators()['SMA50']
                    sma200 = bitcoin.get_indicators()['SMA200']
                    #if exp - time.time() > 1000:
                        #main()
                trade = True
                price = bitcoin.get_indicators()['close']
                rsi = bitcoin.get_indicators()['RSI']
                priceTB = buy(price)
                while trade:
                    time.sleep(100)
                    price = bitcoin.get_indicators()['close']
                    rsi = bitcoin.get_indicators()['RSI']
                    sma20 = bitcoin.get_indicators()['SMA20']
                    sma50 = bitcoin.get_indicators()['SMA50']
                    if sma50 < sma20:
                        time.sleep(100)
                        while trade:
                            sma20 = bitcoin.get_indicators()['SMA20']
                            sma50 = bitcoin.get_indicators()['SMA50']
                            if sma50 > sma20:
                                sell(price, priceTB)
                                trade = False


def buy(priceTB):
    global price
    print("buy at " + str(priceTB))
    return priceTB

def sell(priceTS, priceTB1):
    global totalgain
    priceTS = bitcoin.get_indicators()['close']
    gain = (priceTS - priceTB1) / priceTB1
    totalgain = totalgain + gain
    print("sell at " + str(priceTS) + " with " + str(gain) + "% gain \n"+ str(totalgain) +"% total gain.")
    time.sleep(150)


while True:
    main()