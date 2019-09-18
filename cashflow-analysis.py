import pandas as pd

# settings for importing the csv files
DKB_KK = {'filename':'1002923447.csv'           , 'header':4, 'engine':'python', 'sep':';'}
DKB_EC = {'filename':'4930________0893.csv'     , 'header':5, 'engine':'python', 'sep':';'}




def main():
	dfGK = pd.read_csv(DKB_EC['filename'], header=DKB_EC['header'], engine=DKB_EC['engine'], sep=DKB_EC['sep'])
	dfKK = pd.read_csv(DKB_KK['filename'], header=DKB_KK['header'], engine=DKB_KK['engine'], sep=DKB_KK['sep'])
	print (dfGK.head())
	print (dfKK.head())
	#print (dfKK.columns)

if __name__ == "__main__":

	main()