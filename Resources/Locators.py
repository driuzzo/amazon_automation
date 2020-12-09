from selenium.webdriver.common.by import By

class Locators():
    # --- Home Page Locators ---
    SEARCH_TEXTBOX=(By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON=(By.XPATH,"//header/div[@id='navbar']/div[@id='nav-belt']/div[2]/div[1]/form[1]/div[3]/div[1]/span[1]/input[1]")
    

    # --- Search Results Page Locators ---
    SEARCH_RESULT_LINK=(By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]")

    # --- Product Details Page Locators ---
    ADD_TO_CART_BUTTON=(By.ID, "add-to-cart-button")

    # --- Sub Cart Page Locators ---
    SUB_CART_DIV=(By.ID,"hlb-subcart")
    PROCEED_TO_BUY_BUTTON=(By.ID,"hlb-ptc-btn-native")
    CART_COUNT=(By.ID,"nav-cart-count")
    CART_LINK=(By.ID,"nav-cart")

    # --- Cart Page Locators ---
    DELETE_ITEM_LINK=(By.XPATH,"//body/div[@id='a-page']/div[4]/div[1]/div[6]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[3]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[2]/span[1]/input[1]")
    CART_COUNT=(By.ID,'nav-cart-count-container')
    PROCEED_TO_CHECKOUT_BUTTON=(By.XPATH,"//span[@id='sc-buy-box-ptc-button']")
    # --- Signin Page Locators ---
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX=(By.ID,"ap_email")