import snap
import networkx as nx
import matplotlib.pyplot as plt
import re
from scipy import stats
p = open('aristas_id.txt', 'r')
nodosfile = open('nodos.txt', 'r')
#bajar enlace
#https://snap.stanford.edu/data/web-Stanford.txt.gz
read= p.readline()

total = re.search(r"Nodes: (\d+) Edges: (\d+)",read)


nodos= int(total.group(1))
edges=int(total.group(2))

f = open ("nodo.gexf", "w")

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<gexf xmlns:viz="http:///www.gexf.net/1.1draft/viz" version="1.1" xmlns="http://www.gexf.net/1.1draft">\n')
f.write('<meta lastmodifieddate="2010-03-03+23:44">\n')
f.write('<creator>Gephi 0.7</creator>\n')
f.write('</meta>\n')
f.write('<graph defaultedgetype="undirected" idtype="string" type="static">\n')
f.write('<nodes count="'+str(nodos)+'">\n')
for x in nodosfile:
	an = x
	pares = an.split(" ")
	n1= (pares[0])
	if(len(pares)>1):
		n2= (pares[1])	
	else:
		n2 = " "
	f.write('<node id="'+str(n1)+'" label="'+str(n2)+'"/>\n')

f.write('</nodes>\n')
f.write('<edges count="'+str(edges)+'">\n')
G=nx.Graph()
print "Numero de nodos ",nodos
print "Numero de aristas ", edges

read= p.readline()
#print read
a=1

i=0
for line in p:
	an =line
	#print an
	pares = an.split(" ")
	n1= (int(pares[0]))
	n2= (int(pares[1]))
	f.write('<edge id="'+str(i)+'" source="'+str(n1)+'" target="'+str(n2)+'"/>\n')
	i=i+1
f.write('</edges>\n')
f.write('</graph>\n')
f.write('</gexf>\n')











