import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os, sys, inspect
# busca o caminho para o diretório onde o arquivo atual está, da pasta raíz ou C:\
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extrai o caminho para o diretório pai
parentdir = os.path.dirname(currentdir)
# insere o caminho para a pasta do diretório pai de onde o arquivo python (módulo) está para ser importado
sys.path.insert(0, parentdir)

from Resources.Locators import Locators
from Resources.TestData import TestData

class BasePage():
    """Essa classe é a classe pai para todas as páginas da aplicação."""
    """Contém todos os elementos comuns e funcionalidades disponíveis para todas as páginas."""

    # função chamada toda vez que um novo objeto da base class é criado.
    def __init__(self, driver):
        self.driver = driver

    # essa função clica no elemento referenciado pelo locator.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    
    # função que compara o texto do elemento com o texto passado.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # essa função preenche texto no locator que foi passado.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # checa se o elemento está habilitado ou não e retorna o elemento se estiver habilitado
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # função checa se o elemento está visível ou não e retorna true ou false dependendo da visibilidade
    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # função move o ponteiro do mouse sobre um elemento.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
        
class HomePage(BasePage):
    """Página inicial da Amazon"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX, TestData.search_term)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)

class SearchResultsPage(BasePage):
    """Página de resultados da busca da Amazon"""
    def __init__(self, driver):
        super().__init__(driver)        

    def click_search_result(self):
        self.click(Locators.SEARCH_RESULT_LINK)

class ProductDetailsPage(BasePage):
    """Página de detalhes do produto para o produto clicado na Amazon"""
    def __init__(self,driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        self.click(Locators.ADD_TO_CART_BUTTON)

class SubCartPage(BasePage):
    """Página sub carrinho da Amazon"""
    def __init__(self,driver):
        super().__init__(driver)

    def click_cart_link(self):
        self.click(Locators.CART_LINK)

class CartPage(BasePage):
    """Página do Carrinho da Amazon"""
    def __init__(self,driver):
        super().__init__(driver)
    
    def delete_item(self):
        cartCount = int(self.driver.find_element(*Locators.CART_COUNT).text)
        # imprime ("Cart Count is"+ str(cartCount))
        if (cartCount < 1):
            print("Cart is empty")
            exit()
        if (self.driver.title.startswith("Carrinho de compras da Amazon.com")):
            # deleta um item do carrinho 
            self.click(Locators.DELETE_ITEM_LINK)
            time.sleep(2)        
    
    def click_proceed_to_checkout_button(self):
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON)        

class SignInPage(BasePage):
    """Página de Login da Amazon"""
    def __init__(self,driver):
        super().__init__(driver)