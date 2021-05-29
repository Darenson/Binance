import config, csv
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(config.API_KEY, config.API_SECRET)

# get all symbol prices
#prices = client.get_all_tickers()

#for price in prices:
#    print(price)

#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

#csvfile = open('2012-2021.csv', 'w', newline='')
csvfile = open('2021_15minutes.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')


# for candlestick in candles:
#     print(candlestick)

#     candlestick_writer.writerow(candlestick)

# print(len(candles))

#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "1 May, 2021")
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2021", "12 May, 2021")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close() 
