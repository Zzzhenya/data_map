import graphviz
import pandas as pd

def draw_graph(dot):
	#print(dot.source)
	dot.render('./test.gv', view=True)
	#dot.render('./test.gv')


def create_graph(dot, df):
	a = 1
	dot.attr('node', shape='box', style = "rounded")
	dot.node('0', "Graph")
	#Create the Nodes for columns  
	for i in df.columns:
		dot.node(i)
		dot.edge('0', i)
		dot.node(str(a), str(df.dtypes[i]))
		dot.edge(i, str(a))
		a = a + 1

def main():
	#Open and load csvs 
	df = pd.read_csv('test1.csv'
	#Initiate the graph
	dot = graphviz.Graph()
	create_graph(dot, df)
	draw_graph(dot)

if __name__ == "__main__":
    main()