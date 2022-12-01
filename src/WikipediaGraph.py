import networkx as nx
import neo4j
import nxneo4j

class WikipediaGraph(nxneo4j.DiGraph):
    """
    author: Sakin Kirti and Smyan Thota
    date: 12/01/2022

    class, based on a NetworkX DiGraph, to represent the links between wikipedia articles.

    contains:
    SubClass: WikipediaGraph.WikiNode
    """

    def __init__(self, incoming_graph_data=None, **attr):
        """
        simple __init__ method that calls the nx.Graph constructor
        """

        super().__init__(incoming_graph_data, **attr)

    def add_node(self, node_for_adding, **attr):
        """
        method to add a node to the MCEGraph
        
        params:
        node_for_adding - the node to add
        """

        # call DiGraph's add_node method
        super().add_node(node_for_adding, **attr)

    class WikiNode:
        """
        authors: Sakin Kirti and Smyan Thota
        date: 12/01/2022
        
        custom class to design a wikipedia node
        """

        def __init__(self, title: str, ) -> None:
            pass