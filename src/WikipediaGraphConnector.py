from neo4j import GraphDatabase
import nxneo4j as nx

from WikipediaParser import WikipediaParser as WP

class WikipediaGraphConnector:
    """
    author: Sakin Kirti and Smyan Thota
    date: 12/01/2022

    class, based on a NetworkX DiGraph, to represent the links between wikipedia articles.

    contains:
    SubClass: WikipediaGraphConnector.WikiNode
    """

    def __init__(self, username: str, password: str, url: str):
        """
        initialize WikipediaGraphConnector
        
        params:
        username: str - the username to connect to the db
        password: str - the password to connect to db
        url: str - the url where the db is stored
        
        return:
        WikipediaGraphConnector
        """

        # create connection to db
        self.driver = self.db_connect(username, password, url)
        self.graph = nx.DiGraph(self.driver)

    def db_connect(self, username, password, url):
        """
        method to connect with a database
        
        params:
        username: str - the username to connect to db
        password: str - the password to connect to db
        url: str - the url where the db is stored
        
        return:
        neo4j.GraphDatabase.driver - the driver to execute queries
        """

        return GraphDatabase.driver(uri=url, auth=(username, password))

    def db_disconnect(self):
        """
        method to close the database connection
        
        params:
        None
        
        return:
        None
        """

        self.driver.close()

    def add_nodes(self, nodes: list[str], add_links: bool=False, depth: int=0):
        """
        method to add nodes and edges to the graph
        
        params:
        nodes: list - a list of strings with article titles to add
        add_edges: bool - a boolean expression denoting whether to add edges for the added nodes
        depth: int - if add_edges is True, the depth to add edges (and nodes) for
        
        return:
        None
        """

        # add the nodes to the graph
        for n in nodes:
            nxn = self.WikiNode(n)
            self.graph.add_node(nxn.get_title(), nxn.get_properties())

            # if add_edges is True, add edges (+ new nodes) recursively
            if add_links == True:
                self.__add_nodes_edges_recursively(node=nxn, links=nxn.get_properties()["links"], depth=depth)

    def __add_nodes_edges_recursively(self, parent: any, links: list[str], depth: int):
        """
        method to add nodes and edges recursively
        
        params:
        node: WikipediaGraphConnector.WikiNode - the name of the parent node to add
        links: list - list of names of nodes to direct to from node
        depth: int - to depth to go to from here
        
        return:
        None
        """

        # add the link nodes and link to its parent
        if depth > 0:
            # add link nodes
            for l in links:
                nxn = self.WikiNode(l)
                self.graph.add_node(nxn.get_title(), nxn.get_properties())

                # add the appropriate edge
                self.graph.add_edge(parent.get_title(), nxn.get_title())

                # add the next set depth-first edge
                self.__add_nodes_edges_recursively(parent=nxn, links=nxn.get_properties()["links"], depth=depth-1)

    class WikiNode:
        """
        author: Sakin Kirti and Smyan Thota
        date: 12/01/2022

        class to define a node for this specific database
        Acts as a container to store data to add to nxn graph
        """

        def __init__(self, title: str):
            """
            method to generate a Node in the format that neo4j likes
            
            params:
            title: str - the title of the Wikipedia article to add
            
            return:
            WikipediaGraphConnector.WikiNode
            """

            # initialize the identifier
            self.article_title = title

            # get the properties of the article
            self.page = WP.parse_wikipedia(term=title)
            self.properties = {
                "categories" : self.page.categories,
                "summary" : self.page.summary,
                "references" : self.page.references,
                "images" : self.page.images,
                "links" : self.page.links
            }

        def get_title(self):
            """
            getter method for title
            
            params:
            None
            
            return:
            str - the article title (identifier)
            """

            return self.article_title

        def get_properties(self):
            """
            getter method for article properties
            
            params:
            None
            
            return:
            dictionary - containing properties of the article
            """
            
            return self.properties
