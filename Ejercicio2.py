#Michelle Sánchez Guerrero
#Ejercicio 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

tema = input("Búsqueda: ")

browser = webdriver.Chrome()
browser.get('https://es.wikipedia.org')

busqueda = browser.find_element_by_id('searchInput')
busqueda.send_keys(tema)
busqueda.send_keys(Keys.ENTER)

parrafo = browser.find_element_by_tag_name('p').text

print(parrafo)