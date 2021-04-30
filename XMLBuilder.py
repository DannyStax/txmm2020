# -*- coding: utf-8 -*-

from urllib.request import urlopen
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


xml_articles = ET.Element('articles')
iteration = 1

for article in article_links:
    if iteration % 10 == 0:
        print(iteration)
    html = urlopen("https://nos.nl" + article)
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    title = bsObj.find('h1', {"class": "title_iP7Q1aiP"})
    paragraphs = bsObj.findAll("p", {"class": "text_3v_J6Y0G"})
    
    xml_article = ET.SubElement(xml_articles, "article")
    xml_title = ET.SubElement(xml_article, "title").text = title.text
    
    for paragraph in paragraphs:
        xml_paragraph = ET.SubElement(xml_article, "paragraph").text = paragraph.text
    iteration += 1
    
    
tree = ET.ElementTree(xml_articles)

tree.write('articles.xml')
