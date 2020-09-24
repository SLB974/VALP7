# coding: utf-8
from unidecode import unidecode
import re

from app.core.utils import stop_words

class Parser:
    """Parse user's query"""
    
    def __init__(self, user_query):
        self.user_query = user_query
    
    def clean_string(self):
        """ remove accents, upper and punctuation
            compare to stop_words reference and remove items
            split in list"""
        
        cleaned = unidecode(self.user_query).lower()
        cleaned = re.compile('\w+').findall(cleaned)
        return [item for item in cleaned if item not in stop_words]
    
