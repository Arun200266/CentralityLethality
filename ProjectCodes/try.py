import pandas as pd
import networkx as nx

def get_features(G, mi=1000):
    ''' ,
                       nx.current_flow_betweenness_centrality(G)
    '''
    nodes = nx.nodes(G)
    lrc = {}
    pagerank = {}
    for v in nodes:
        lrc[v] = nx.local_reaching_centrality(G, v)
        pagerank[v] = 0
    voterank = nx.voterank(G)
    val = nodes.__len__()
    for v in voterank:
        pagerank[v] = val
        val -= 1
    df = pd.DataFrame([nx.degree_centrality(G), nx.eigenvector_centrality(G, max_iter=mi),
                       nx.closeness_centrality(G), nx.betweenness_centrality(G),
                       nx.subgraph_centrality(G),
                       nx.load_centrality(G), nx.harmonic_centrality(G),
                       lrc, nx.clustering(G), pagerank],
                      index=["degree_centrality", "eigenvector_centrality",
                             "closeness_centrality", "betweenness_centrality",
                             "subgraph_centrality",
                             "load_centrality", "harmonic_centrality",
                             "reaching_centrality",
                             "clustering_centrality", "pagerank"])
    return df.transpose()
    pass


with open("graphs.txt") as f:
    graphs = f.readlines()
graphs = [x.strip() for x in graphs]

# print(graphs)
#
# for graphname in graphs:
#    G = nx.read_weighted_edgelist('/Users/arun/Desktop/BT/Project/Codes/Graphs/'+graphname+'.ppi.txt')
#
#    df = get_features(G)
#    df.to_csv("/Users/arun/Desktop/BT/Project/Codes/Features/"+graphname +".csv")
#    print(graphname +" : features extracted")

# RUN these values instead of 2 = [26,25,24,23,22]
graphname = graphs[8]
G = nx.read_weighted_edgelist('Graphs/' + graphname + '.ppi.txt')

df = get_features(G)
df.to_csv("Features/" + graphname + ".csv")
