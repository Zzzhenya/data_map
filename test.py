import graphviz
import pandas as pd

def main():
	#Open and load csvs 
	df = pd.read_csv('test1.csv')
	#Initiate the graph
	dot = graphviz.Digraph()
	dot.node("Graph")
	dot.attr('node', shape='box')
	#Create the Nodes for columns  
	for i in df.columns:
		dot.node(i)
		dot.edge("Graph", i)
		dot.node(str(df.dtypes[i]))
		dot.edge(i, str(df[i].dtype))

	print(dot.source)
	dot.render('./test.gv')
	dot.render('./test.gv', view=True)
if __name__ == "__main__":
    main()