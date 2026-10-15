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
driver.get("https://duckduckgo.com")

# Recherche de la barre de recherche grâce à son attribut name="q"
barre_recherche = driver.find_element(By.NAME, "q")

# Écriture de la recherche dans la barre
barre_recherche.send_keys("Selenium WebDriver tutorial")

# Simulation de la touche Entrée pour valider la recherche
barre_recherche.send_keys(Keys.ENTER)

# Création d'une attente explicite de maximum 10 secondes
wait = WebDriverWait(driver, 10)

# Attente jusqu'à ce que le mot "Selenium" soit présent dans la page de résultats
resultat = wait.until(
    EC.text_to_be_present_in_element(
        (By.TAG_NAME, "body"),
        "Selenium"
    )
)

# Vérification que Selenium est bien présent dans les résultats
assert resultat

# Affichage d'un message si le test a réussi
print("Test réussi : Selenium est présent dans les résultats.")

# Pause pour voir le résultat dans Firefox
input("Appuie sur Entrée pour fermer Firefox...")

# Fermeture du navigateur
driver.quit()