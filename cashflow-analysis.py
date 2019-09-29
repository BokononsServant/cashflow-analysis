import pandas as pd
import numpy as np
# settings for importing the csv files
DKB_EC = {'filename'   : '1002923447.csv'           
        , 'header'     : 4
		, 'engine'     : 'python'
		, 'sep'        : ';'
		, 'usecols'    : ['Buchungstag', 'Auftraggeber / Begünstigter', 'Verwendungszweck', 'Betrag (EUR)']
		, 'parse_dates': ['Buchungstag']
		, 'decimal'    : ','
		, 'thousands'  : '.' 
		}
DKB_KK = {'filename'   : '4930________0893.csv'
        , 'header'     : 5
		, 'engine'     : 'python'
		, 'sep'        : ';'
		, 'usecols'    : ['Belegdatum', 'Beschreibung', 'Betrag (EUR)']
		, 'parse_dates': ['Belegdatum']
		, 'decimal'    : ','
		, 'thousands'  : '.' 
		}
categories = ['health','fitness','BVG','vacation']

def read_data():
	"""Read in data for credit card and giro. Assign proper datatypes, drop unnecessary columns, rename columns and combine credit card data and giro data.
       Return dataframe.	
	"""
	dfGK = pd.read_csv(     DKB_EC['filename']
	        , header      = DKB_EC['header']
			, engine      = DKB_EC['engine']
			, sep         = DKB_EC['sep']
			, usecols     = DKB_EC['usecols']
			, parse_dates = DKB_EC['parse_dates']
			, decimal     = DKB_EC['decimal']
			, thousands   = DKB_EC['thousands'] #Broke after adding decimal and thousands: is now int64
			, decimal     = DKB_KK['decimal']
			, thousands   = DKB_KK['thousands']
			)
	return dfGK, dfKK


def main():
	dfGK, dfKK = read_data()

	print (dfGK.info())
	print (dfKK.info())
	#print (dfKK.columns)

if __name__ == "__main__":

	main()