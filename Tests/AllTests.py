import unittest
from selenium import webdriver
import HtmlTestRunner
import os, sys, inspect
# busca o caminho para o diretório onde o arquivo atual está, da pasta raíz ou C:\
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extrai o caminho para o diretório pai
parentdir = os.path.dirname(currentdir)
# insere o caminho para a pasta do diretório pai de onde o arquivo python (módulo) está para ser importado
sys.path.insert(0, parentdir)
from Resources.Locators import Locators
from Resources.PO.Pages import HomePage, SearchResultsPage, ProductDetailsPage, SubCartPage, CartPage, SignInPage
from Resources.TestData import TestData

# Classe Base para os testes
class Test_AMZN_Search_Base(unittest.TestCase):

    def setUp(self):
        # Define como o crhome será executado
        chrome_options=webdriver.ChromeOptions()
        self.driver=webdriver.Chrome(TestData.chrome_executable_path, options=chrome_options)
        # navegador será executado com a janela maximizada
        self.driver.maximize_window()
    
    def tearDown(self):
        # Finaliza a instância do browser.
        self.driver.close()
        self.driver.quit()
        
# Classe de teste contendo os métodos correspondentes aos casos de teste.
class Test_AMZN_Search(Test_AMZN_Search_Base):
    def setUp(self):
        # chama o método setup() da base classe ou super classe (nesse caso é a Test_AMZN_Search_Base).
        super().setUp()

    """def test_home_page_loaded_successfully(self):
        # Instancia um objeto da classe HomePage. Lembre-se que quando o construtor da classe HomePage é chamado
        # ele abre o navegador e navega até a página inicial do site em teste.
        self.homePage = HomePage(self.driver)
        
        # certifica se o título da página contém Amazon
        self.assertIn(TestData.home_page_title, self.homePage.driver.title)

    def test_user_should_be_able_to_search(self):
        # Instancia um objeto da classe HomePage. Lembre-se que quando o construtor da classe HomePage é chamado
        # ele abre o navegador e navega até a página inicial do site em teste.        
        self.homePage = HomePage(self.driver)

        # busca o termo na Página Inicial. O termo será coletado do arquivo TestData
        self.homePage.search()
        
        # instancia um objeto da classe SearchResultsPage passando o driver como parâmetro.
        # isso permitirá que o novo objeto tenha acesso ao navegador e execute operações mais à frente
        self.searchResultsPage = SearchResultsPage(self.homePage.driver)

        # verifica se o termo está presente no título da página de resultados da Amazon
        self.assertIn(TestData.search_term,self.searchResultsPage.driver.title)

        # verifica que o termo de fato retorna resultados.
        self.assertNotIn(TestData.no_results_text,self.searchResultsPage.driver.page_source)"""

    def test_user_should_be_able_to_add_item_to_cart(self):
        self.homePage = HomePage(self.driver)
        self.homePage.search()
        self.searchResultsPage=SearchResultsPage(self.homePage.driver)

        # clica no primeiro resultado
        self.searchResultsPage.click_search_result()

        # instancia um objeto da classe Product Details Page
        self.productDetailsPage = ProductDetailsPage(self.searchResultsPage.driver)

        # clica no botão Adicionar ao Carrinho 
        self.productDetailsPage.click_add_to_cart_button()

        # instancia um objeto da classe Sub Cart Page 
        self.subCartPage = SubCartPage(self.productDetailsPage.driver)

        # verifica se a página do carrinho foi carregada 
        self.assertTrue(self.subCartPage.is_enabled(Locators.SUB_CART_DIV))
        
        # verifica se o produto foi adicionado ao carrinho
        self.assertTrue(self.searchResultsPage.is_visible(Locators.PROCEED_TO_BUY_BUTTON))

    def test_user_should_be_able_to_delete_item_from_cart(self):
        self.homePage=HomePage(self.driver)
        self.homePage.search()
        self.searchResultsPage=SearchResultsPage(self.homePage.driver)
        self.searchResultsPage.click_search_result()
        
        # self.searchResultsPage.driver.switch_to_window(self.searchResultsPage.driver.window_handles[0])
        self.productDetailsPage=ProductDetailsPage(self.searchResultsPage.driver)
        self.productDetailsPage.click_add_to_cart_button()
        self.subCartPage=SubCartPage(self.productDetailsPage.driver)
        
        # clica no link do carrinho para carregar a página do carrinho
        self.subCartPage.click_cart_link()
        
        # instancia um objeto da classe Cart Page 
        self.cartPage=CartPage(self.subCartPage.driver)
        
        # conta a quantidade de itens antes de deletar o item do carrinho
        cartCountBeforeDeletion=int(self.driver.find_element(*Locators.CART_COUNT).text)
        
        # deleta um item do carrinho 
        self.cartPage.delete_item()
        
        # verifica se o item foi deletado 
        self.assertTrue(int(self.driver.find_element(*Locators.CART_COUNT).text) < cartCountBeforeDeletion) 

    def test_user_must_signin_to_checkout(self):
        self.homePage=HomePage(self.driver)
        self.homePage.search()
        self.searchResultsPage=SearchResultsPage(self.homePage.driver)
        self.searchResultsPage.click_search_result()
        self.searchResultsPage.driver.switch_to_window(self.searchResultsPage.driver.window_handles[0])
        self.productDetailsPage=ProductDetailsPage(self.searchResultsPage.driver)
        self.productDetailsPage.click_add_to_cart_button()
        self.subCartPage=SubCartPage(self.productDetailsPage.driver)
        self.subCartPage.click_cart_link()
        
        # instancia um objeto da classe Cart Page
        self.cartPage=CartPage(self.subCartPage.driver)    
        
        # clica no botão Ir para o Carrinho 
        self.cartPage.click_proceed_to_checkout_button()
        
        # instancia um onjeto da classe SignIn Page
        self.signInPage=SignInPage(self.cartPage.driver)
       
        # verifica se realmente está na página de login, primeiro verifica o títulod da página
        self.assertTrue(TestData.sign_in_page_title,self.signInPage.driver.title)
        
        # e então verifica a presença do campo de email na página
        self.assertTrue(self.signInPage.is_visible(Locators.USER_EMAIL_OR_MOBIL_NO_TEXTBOX))

if __name__ == '__main__':
    # especifica o caminho onde os relatórios dos casos de testes serão gerados
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=parentdir + '\\Reports'))
