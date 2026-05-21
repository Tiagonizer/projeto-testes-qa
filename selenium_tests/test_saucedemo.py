# Projeto de testes automatizados — Selenium + Python
# Site de exemplo: https://www.saucedemo.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def iniciar_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def test_ct01_carregar_pagina():
    print("\n▶ CT01 - Carregando página de login...")
    driver = iniciar_driver()
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title
    assert driver.find_element(By.ID, "user-name").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    print("✅ CT01 passou!")
    driver.quit()

def test_ct02_login_valido():
    print("\n▶ CT02 - Login com credenciais válidas...")
    driver = iniciar_driver()
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("/inventory"))
    assert "/inventory" in driver.current_url
    print("✅ CT02 passou!")
    driver.quit()

def test_ct03_login_invalido():
    print("\n▶ CT03 - Login com credenciais inválidas...")
    driver = iniciar_driver()
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("usuario_errado")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-button").click()
    erro = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert erro.is_displayed()
    print("✅ CT03 passou!")
    driver.quit()

def test_ct04_adicionar_carrinho():
    print("\n▶ CT04 - Adicionando produto ao carrinho...")
    driver = iniciar_driver()
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"
    print("✅ CT04 passou!")
    driver.quit()

def test_ct05_logout():
    print("\n▶ CT05 - Realizando logout...")
    driver = iniciar_driver()
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert driver.current_url == "https://www.saucedemo.com/"
    print("✅ CT05 passou!")
    driver.quit()

if __name__ == "__main__":
    print("=== Iniciando testes Selenium ===")
    test_ct01_carregar_pagina()
    test_ct02_login_valido()
    test_ct03_login_invalido()
    test_ct04_adicionar_carrinho()
    test_ct05_logout()
    print("\n✅ Todos os testes concluídos!")