# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

tree = ET.parse('articles.xml')
articles = tree.getroot()

paragraphs_with_quotes = []
paragraphs_with_double_quotes = []
quotes = []
extracted_paragraphs = []


for article in articles:
    for paragraph in article.findall('paragraph'):
        text = paragraph.text
        count = text.count("\'")
        indexes = []
        if count > 1:
            paragraphs_with_quotes.append(text)
            index = text.index("\'")
            while count > 0:
                
                if text[index-1] == " " or index == len(text) - 1 or text[index+1] in " .,":
                    indexes.append(index)
                if count > 1:    
                    index = text.index("\'", index+1)
                count -= 1
            for i in range(0, len(indexes), 2):
                start = indexes[i]
                end = indexes[min(len(indexes)-1,i+1)]
                print(text)
                
                quotes.append(text[indexes[i]:indexes[min(len(indexes)-1,i+1)]+1])
                extracted_paragraphs.append(text)
        
                print("Quote:" + quotes[len(quotes)-1])
                print()
            
d = {'Paragraph:':extracted_paragraphs, 'Quote:':quotes, 'Scare_Quote:':np.nan}
quote_data = pd.DataFrame(d)
quote_data.to_csv('quote_data.csv')

for i in range(20):
    print(quote_data.loc[i])
    print()
    
print(len(paragraphs_with_quotes))
    
#"\"" in paragraph.text or 
#seaborne