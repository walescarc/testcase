from selenium import webdriver
import time
from selenium.webdriver.common.by import By

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
driver.quit()