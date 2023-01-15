from selenium import webdriver
driver = webdriver.Firefox()


# Para acceder a una página:
# driver.get('https://slider.kz/#antes de morirme')
driver.get('https://www.wikipedia.org/')

input("Esperando que no se cierre webdriver: ")

# firstScreen = driver.find_elements_by_css_selector('div.fullwrapper')

#mirar xpath loko.
searchBar = driver.find_element_by_id('searchInput')
searchBar.send_keys('Pedro')

# searchButton = driver.find_element_by_class('pure-button pure-button-primary-progressive')
# searchButton.click()

# #Para realizar busquedas
# searchBar = driver.find_elements_by_class_name('buttonQuery')
# searchBar.send_keys('Antes de morirme - c tangana')

# searchButton = driver.find_element_by_id('searchButton')
# searchButton.click()

