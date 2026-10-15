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
driver.get("https://www.selenium.dev/documentation/test_practices/")

clique_lien = driver.find_element(By.LINK_TEXT, "Testing Types")

clique_lien.click()

driver.implicitly_wait(10)

# Vérification du titre de la page
title = driver.find_element(By.TAG_NAME, "body").text

if "Acceptance testing" in title:
    print("Ca marche bien")

# Pause pour voir le résultat dans Firefox
input("Appuie sur Entrée pour fermer Firefox...")



# Fermeture du navigateur
driver.quit()
