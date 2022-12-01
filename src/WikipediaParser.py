import wikipedia as wiki

class WikipediaParser:
    """
    authors: Sakin Kirti and Smyan Thota
    date: 12/01/2022
    
    class to create a parser for wikipedia
    """

    def __init__(self, lang:str="en"):
        
        # set the wikipedia language
        wiki.set_lang(lang)

    @staticmethod
    def parse_wikipedia(term: str):
        """
        method to parse wikipedia based on a search term
        
        params:
        term: str - the term to search for
        
        return:
        wiki.WikipediaPage - the page(s) of the search term for the number of results
        """

        # search wikipedia
        titles = wiki.search(query=term, results=1)

        # pick the top result and generate wikipedia page
        page = wiki.WikipediaPage(title=titles[0])

        # return the relevant
        return page

    @staticmethod
    def find_links(page: wiki.WikipediaPage):
        """
        method to get the links based on a wikipedia page
        
        params:
        page: wiki.WikipediaPage - the page to get links of
        
        return:
        list - titles of the linked pages
        """

        # get links and return
        return page.links
