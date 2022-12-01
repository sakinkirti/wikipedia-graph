import numpy as np
import pandas as pd

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

    def parse_wikipedia(self, term: str, num_results:int=10):
        """
        method to parse wikipedia based on a search term
        
        params:
        term: str - the term to search for
        
        return:
        """

        # search wikipedia
        res = wiki.search(query=term, results=num_results)

        # pick the top result and generate wikipedia page
        page = wiki.WikipediaPage(title=res[0])

        # find links to other wikipedia pages
        links = page.links
        
        return (page, links)

parser = WikipediaParser("en")
print(parser.parse_wikipedia("covid", 10))