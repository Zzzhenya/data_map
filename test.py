import graphviz
import pandas as pd

def draw_graph(dot):
	#print(dot.source)
	dot.render('./test.gv', view=True)
	#dot.render('./test.gv')


def create_graph(dot, df):
	dot.attr('node', shape='box', style = "rounded")
	dot.node('0', "DataFrame")
	#Create the Nodes for columns  
	for i in df.columns:
		dot.node(i)
		dot.edge('0', i)
		dot.node(i + str(df.dtypes[i]), "Dtype: "+ str(df.dtypes[i]))
		dot.edge(i, i + str(df.dtypes[i]))
		dot.node(i + "count" + str(df[i].count()), "Count: "+ str(df[i].count()))
		dot.edge(i, i + "count" + str(df[i].count()))
		dot.node(i + "min" + str(df[i].min()), "Min: "+ str(df[i].min()))
		dot.edge(i, i + "min" + str(df[i].min()))
		dot.node(i + "max" + str(df[i].max()), "Max: "+ str(df[i].max()))
		dot.edge(i, i + "max" + str(df[i].max()))

def main():
	#Open and load csvs 
	df = pd.read_csv('test1.csv')
	#Initiate the graph
	dot = graphviz.Graph(engine = "circo")
	create_graph(dot, df)
	draw_graph(dot)

if __name__ == "__main__":
    main()