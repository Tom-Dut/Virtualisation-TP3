from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Configuration de Firefox car notre Firefox est installé dans un dossier personnel
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration de geckodriver installé dans notre dossier personnel
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur Firefox contrôlé par Selenium
driver = webdriver.Firefox(service=service, options=options)

# Ouverture du site de l'IUT
driver.get("https://www.iut-lens.univ-artois.fr/")

# Affichage du titre de la page
print(driver.title)

# Fermeture du navigateur
driver.quit()