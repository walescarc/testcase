from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Acessar a página
driver.get("https://www.demoblaze.com/index.html") 

time.sleep(2)

# Clicar no link com texto "Sony vaio i7"
elemento = driver.find_element(By.LINK_TEXT, "Sony vaio i7")
elemento.click()

time.sleep(2)

botao = driver.find_element(By.LINK_TEXT, "Add to cart")
botao.click()

time.sleep(2)

alerta = driver.switch_to.alert
print(alerta.text) 
alerta.accept() 

time.sleep(3)

# Por seletor CSS, mais confiável:
home_link = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="index.html"]')
home_link.click()

time.sleep(2)

elemento = driver.find_element(By.LINK_TEXT, "Iphone 6 32gb")
elemento.click()

time.sleep(2)

botao = driver.find_element(By.LINK_TEXT, "Add to cart")
botao.click()

time.sleep(2)

alerta = driver.switch_to.alert
print(alerta.text)  
alerta.accept()

time.sleep(3)