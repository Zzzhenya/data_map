import graphviz
import pandas as pd


def main():
	#Open and load csvs 
	df = pd.read_csv('test1.csv')
	#Initiate the graph
	dot = graphviz.Graph()
	#Create the Nodes for columns  
	for i in df.columns:
		dot.node(i)
	print(dot.source) 
if __name__ == "__main__":
    main()