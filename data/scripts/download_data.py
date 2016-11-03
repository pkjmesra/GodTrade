import pandas_datareader.data as web
from datetime import datetime
import pandas as pd


start = datetime(1900, 1, 1)	#(YYYY, MM, DD)
end   = datetime(2016, 11, 2)


#Download Nifty500 stocks
nse = pd.read_csv('NSE/ind_nifty500list.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
    try:
        symbol = symbols[rows]
        stock_symbol = symbol + ".NS"
        stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
        filename = '../NSE/Cap-Size/' + symbol + '.csv'
        stock_prices.to_csv(filename)
    except Exception, arg:
        print("Error downloading symbol:"+str(symbol))
        print(str(arg))
        continue
        
'''
#Download Nifty Auto stocks
nse = pd.read_csv('NSE/ind_niftyautolist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Auto/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty Bank stocks
nse = pd.read_csv('NSE/ind_niftybanklist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Bank/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty Finance stocks
nse = pd.read_csv('NSE/ind_niftyfinancelist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Finance/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty FMCG stocks
nse = pd.read_csv('NSE/ind_niftyfmcglist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/FMCG/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty IT stocks
nse = pd.read_csv('NSE/ind_niftyitlist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/IT/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty Media stocks
nse = pd.read_csv('NSE/ind_niftymedialist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Media/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty Metal stocks
nse = pd.read_csv('NSE/ind_niftymetallist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Metal/' + symbol + '.csv'
	stock_prices.to_csv(filename)

	
#Download Nifty Pharma stocks
nse = pd.read_csv('NSE/ind_niftypharmalist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Pharma/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty Private-Bank stocks
nse = pd.read_csv('NSE/ind_nifty_privatebanklist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Private_Bank/' + symbol + '.csv'
	stock_prices.to_csv(filename)

#Download Nifty PSU-Bank stocks
nse = pd.read_csv('NSE/ind_niftypsubanklist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/PSU_Bank/' + symbol + '.csv'
	stock_prices.to_csv(filename)


#Download Nifty Realty stocks
nse = pd.read_csv('NSE/ind_niftyrealtylist.csv')
symbols = nse[nse.columns[2]]

for rows in range(0, len(symbols)):
	symbol = symbols[rows]
	stock_symbol = symbol + ".NS"
	stock_prices = web.DataReader(stock_symbol, "yahoo", start, end)
	filename = '../NSE/Sectors/Realty/' + symbol + '.csv'
	stock_prices.to_csv(filename)
	'''

