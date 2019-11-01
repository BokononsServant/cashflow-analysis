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
        , 'parse_dates': ['Belegdatum', 'Wertstellung']
        , 'decimal'    : ','
        , 'thousands'  : '.'
        , 'drop'       : ['Umsatz abgerechnet und nicht im Saldo enthalten', 'Wertstellung', 'Ursprünglicher Betrag', 'Unnamed: 6']
        , 'rename'     : {'Belegdatum' : 'Buchungstag', 'Beschreibung' : 'Verwendungszweck'}
        }
categories = ['health', 'fitness', 'BVG', 'vacation', 'cash', 'salary', 'dining', 'presents', 'entertainment', 'travelling']
analysis_file = 'DKB_cashflow.csv'

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
            , thousands   = DKB_EC['thousands'] 
            )

    dfKK = pd.read_csv(     DKB_KK['filename']
            , header      = DKB_KK['header']
            , engine      = DKB_KK['engine']
            , sep         = DKB_KK['sep']
            , usecols     = None # Datetime conversion does not work when using usecols. Bug in Pandas? Drop unwanted columns later.
            , parse_dates = DKB_KK['parse_dates']
            , decimal     = DKB_KK['decimal']
            , thousands   = DKB_KK['thousands'] 
            )
    # GK: Girokonto, KK: Kreditkarte
    dfGK['Konto']='GK'
    dfKK['Konto']='KK'

    dfKK.drop(labels=DKB_KK['drop'], axis=1, inplace=True)
    dfKK.rename(columns=DKB_KK['rename'], inplace=True)

    df_GK_KK = pd.concat([dfGK, dfKK], ignore_index=True, keys=['GK', 'KK'], sort=True)

    #There can't be any real duplicates in the data. If there are, they are valid transactions that have the same metadata.
    #But we need to drop_duplicates later, so we will add a "Duplicates" column to be able to make those entries unique.

    df_GK_KK['Duplicates'] = 0
    dup = df_GK_KK.columns.get_loc('Duplicates')
    duplicates = df_GK_KK[df_GK_KK.duplicated()]
    for i in duplicates.index:
        df_GK_KK.iloc[i,dup]=i

    return df_GK_KK

def analysis ():
    pass

def main():
    
    
    val = 'd' #input("Perform analysis (a) or add new data (d): ")

    if val == 'a':
        analysis()
    elif val == 'd':
        df_GK_KK = read_data()
        print(df_GK_KK.info())
        try:
            df = pd.read_csv(analysis_file, parse_dates=['Buchungstag'])
            df_GK_KK = pd.concat([df_GK_KK, df], ignore_index=True, sort=True)
            df_GK_KK.drop_duplicates(inplace=True)
        except:
            df_GK_KK.to_csv(analysis_file, index=False)
    else:
        pass
        #print ('Please try again.')
    
    print(df_GK_KK.info())

    



 



    

    #print (df_GK_KK.sort_values('Buchungstag'))
if __name__ == "__main__":

    main()