from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Acessar a página
driver.get("https://www.demoblaze.com/index.html") 

time.sleep(1)

# Clicar no link com texto "Sony vaio i7"
elemento = driver.find_element(By.LINK_TEXT, "Sony vaio i7")
elemento.click()

time.sleep(1)

botao = driver.find_element(By.LINK_TEXT, "Add to cart")
botao.click()

time.sleep(1)

alerta = driver.switch_to.alert
print(alerta.text) 
alerta.accept() 

time.sleep(2)

# Por seletor CSS, mais confiável:
home_link = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="index.html"]')
home_link.click()

time.sleep(1)

elemento = driver.find_element(By.LINK_TEXT, "Iphone 6 32gb")
elemento.click()

time.sleep(1)

botao = driver.find_element(By.LINK_TEXT, "Add to cart")
botao.click()

time.sleep(1)

alerta = driver.switch_to.alert
print(alerta.text)  
alerta.accept()

time.sleep(2)

# Por seletor CSS, mais confiável:
cart_link = driver.find_element(By.LINK_TEXT, "Cart")
cart_link.click()

time.sleep(1)

# Localiza o elemento pelo ID
total_element = driver.find_element(By.ID, "totalp")

# Obtém o texto (ex: '1580') e converte para inteiro, se necessário
total_value = int(total_element.text)

# Verifica se o valor é o esperado
assert total_value == 1580, f"Valor incorreto: {total_value}"
print("✅ Valor correto no carrinho:", total_value)

time.sleep(1)

botao_place_order = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
botao_place_order.click()

time.sleep(1)

campo_nome = driver.find_element(By.ID, "name")
campo_nome.send_keys("Hanzo Hasashi") 

time.sleep(1)

campo_nome = driver.find_element(By.ID, "country")
campo_nome.send_keys("Japan") 

time.sleep(1)

campo_nome = driver.find_element(By.ID, "city")
campo_nome.send_keys("Tokyo") 

time.sleep(1)

campo_nome = driver.find_element(By.ID, "card")
campo_nome.send_keys("4485572801000971") 

time.sleep(1)

campo_nome = driver.find_element(By.ID, "month")
campo_nome.send_keys("01") 

time.sleep(1)

campo_nome = driver.find_element(By.ID, "year")
campo_nome.send_keys("2039") 

time.sleep(1)

botao_purchase = driver.find_element(By.XPATH, "//button[text()='Purchase']")
botao_purchase.click()

wait = WebDriverWait(driver, 5)
modal_body = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible"))
)

print("Modal apareceu na tela!")


driver.quit()