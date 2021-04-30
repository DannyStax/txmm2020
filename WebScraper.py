# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:50:53 2021

@author: Danny Stax
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def get_articles():
    article_links = []
    for x in range(32):
        if x < 10:
            html = urlopen("https://nos.nl/nieuws/archief/2020-12-0" + str(x) + "/")
        else:
            html = urlopen("https://nos.nl/nieuws/archief/2020-12-" + str(x) + "/")
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        articles = bsObj.findAll("li", {"class": "list-time__item"})
        for article in articles:
            article_links.append(article.find('a')['href'])
    return article_links        
    

article_links = get_articles()
print(len(article_links))

    
#xml_articles = ET.Element('articles')
#iteration = 1
#for article in article_links:
#    if iteration % 10 == 0:
#        print(iteration)
#    html = urlopen("https://nos.nl" + article)
#    bsObj = BeautifulSoup(html.read(), 'html.parser')
#    title = bsObj.find('h1', {"class": "title_iP7Q1aiP"})
#    paragraphs = bsObj.findAll("p", {"class": "text_3v_J6Y0G"})
#    
#    xml_article = ET.SubElement(xml_articles, "article")
#    
#    if title is not None:
#        xml_title = ET.SubElement(xml_article, "title").text = title.text
#        for paragraph in paragraphs:
#            xml_paragraph = ET.SubElement(xml_article, "paragraph").text = paragraph.text
#    iteration += 1
#
#tree = ET.ElementTree(xml_articles)
#
#tree.write('articles.xml')

#print(articles[0].find('a')['href'])

#articles[0].find('a')['href']

#Title class name: title_iP7Q1aiP
#Content class name: text_3v_J6Y0G
#ElementTree for xml parsing