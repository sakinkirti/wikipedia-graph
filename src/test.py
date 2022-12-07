from WikipediaGraphConnector import WikipediaGraphConnector as WGC

def main():
    # establish connection
    connector = WGC(
        username="neo4j", 
        password="OZQERmHm1vdC0A1Z7oPD0-SQwDhtDpz_Nqtud8DHaA4",
        url="neo4j+s://1d990c5b.databases.neo4j.io"
    )

    # add some nodes (lowkey a ton of nodes)
    connector.add_nodes(nodes=["star wars"], add_links=True, depth=3, max_nodes=10)
    connector.add_nodes(nodes=["kim kardashian"], add_links=True, depth=3, max_nodes=10)
    connector.add_nodes(nodes=["chipotle"], add_links=True, depth=3, max_nodes=10)
    #connector.add_nodes(nodes=["toilet paper"], add_links=True, depth=3, max_nodes=10)

    # disconnect from db
    connector.db_disconnect()

if __name__ == "__main__":
    main()