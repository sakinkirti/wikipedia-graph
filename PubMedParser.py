import json

import numpy as np
import pandas as pd
from Bio import Entrez

class PubMedParser:
    """
    class which calls the Entrez Database of PubMed to get articles
    """

    def __init__(self):
        """
        initializes the object
        """

        # identifier
        Entrez.email = "sak207@case.edu"

    def search_papers(self, topic: str):
        """
        method to search the pubmed db
        
        parameters
        topic: str - the keyword/phrase to search
        
        return type
        dictionary - the results of the search
        """

        Entrez.esearch()
