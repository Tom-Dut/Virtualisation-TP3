from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration de Firefox installé dans notre dossier personnel
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration du geckodriver installé dans notre dossier personnel
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur Firefox contrôlé par Selenium
driver = webdriver.Firefox(service=service, options=options)

# Ouverture du site DuckDuckGo
driver.get("https://saucedemo.com")


champs_nom = driver.find_element(
    By.ID, "user-name"
)

input("appuie sur entrer")

# Fermeture du navigateur
driver.quit()
