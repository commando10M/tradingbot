from tradingview_ta import *
import colorama, time
from colorama import Fore
colorama.init(autoreset=True)

totalgain = 0

bitcoin = TA_Handler(
    symbol="SOLUSD",
    exchange="COINBASE",
    screener="crypto",
    interval="1m",
    timeout=None
)

print(f"{Fore.GREEN}online")

#main functoin
def main():
    global time

    while True:
        trade = False
        price = bitcoin.get_indicators()['close']
        sma20 = bitcoin.get_indicators()['SMA20']
        sma50 = bitcoin.get_indicators()['SMA50']
        sma200 = bitcoin.get_indicators()['SMA200']
        if trade == False :

            #buy algo
            if sma50 < sma20 < price < sma200:
                time.sleep(150)
                while sma200 > price:
                    price = bitcoin.get_indicators()['close']
                    sma200 = bitcoin.get_indicators()['SMA200']
                trade = True
                price = bitcoin.get_indicators()['close']
                priceTB = buy(price)
                time.sleep(100)

                #sell algo
                while trade:
                    price = bitcoin.get_indicators()['close']
                    sma20 = bitcoin.get_indicators()['SMA20']
                    sma50 = bitcoin.get_indicators()['SMA50']
                    if sma50 < sma20:
                        time.sleep(100)
                        while trade:
                            price = bitcoin.get_indicators()['close']
                            sma5 = bitcoin.get_indicators()['SMA5']
                            sma50 = bitcoin.get_indicators()['SMA50']
                            if sma50 > sma5:
                                sell(priceTB)
                                trade = False
                                print("1")
                            if ((price - priceTB) / price) * 10000 < -15:
                                print("2")
                                sell(priceTB)
                                trade = False

#refresh
def value():
    price = bitcoin.get_indicators()['close']
    sma5 = bitcoin.get_indicators()['SMA5']
    sma10 = bitcoin.get_indicators()['SMA10']
    sma20 = bitcoin.get_indicators()['SMA20']
    sma50 = bitcoin.get_indicators()['SMA50']
    sma200 = bitcoin.get_indicators()['SMA200']
    rsi = bitcoin.get_indicators()['rsi']
    return price, sma5, sma10, sma20, sma50, sma200, rsi


#buy function
def buy(priceTB):
    global price
    print(f"{Fore.GREEN}buy " + "at " + str(priceTB))
    return priceTB

#sell functoin
def sell(priceTB1):
    global totalgain
    priceTS = bitcoin.get_indicators()['close']
    gain = ((priceTS - priceTB1) / priceTB1) * 100
    totalgain = totalgain + gain
    print(f"{Fore.RED}sell at " + str(priceTS) + f"{Fore.WHITE} with " + str(gain) + "% gain")
    if totalgain > 0 :
        print(f"{Fore.GREEN}" + str(totalgain)+"% total gain.")
    else:
        print(f"{Fore.RED}" + str(totalgain) + "% total gain.")
    time.sleep(120)


while True:
    main()