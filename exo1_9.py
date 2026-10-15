from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Configuration de Firefox
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration de geckodriver
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur Firefox
driver = webdriver.Firefox(service=service, options=options)

# Création d'une attente explicite
wait = WebDriverWait(driver, 10)

# Ouverture de Google dans le premier onglet
driver.get("https://www.google.com")

# Mémorisation de l'identifiant du premier onglet
fenetre_google = driver.current_window_handle

# Mémorisation du titre de Google
titre_google = driver.title

print("Titre Google :", titre_google)

# Création d'un deuxième onglet
driver.switch_to.new_window("tab")

# Ouverture de Wikipédia dans ce deuxième onglet
driver.get("https://www.wikipedia.org")

# Recherche de l'identifiant du deuxième onglet
for handle in driver.window_handles:
    if handle != fenetre_google:
        fenetre_wikipedia = handle

# Mémorisation du titre de Wikipédia
titre_wikipedia = driver.title

print("Titre Wikipédia :", titre_wikipedia)

# Vérification que les deux titres sont différents
assert titre_google != titre_wikipedia

# Retour vers l'onglet Google
driver.switch_to.window(fenetre_google)

# Vérification du titre après le changement d'onglet
assert driver.title == titre_google

print("Retour sur Google :", driver.title)

# Passage vers l'onglet Wikipédia
driver.switch_to.window(fenetre_wikipedia)

# Vérification du titre
assert driver.title == titre_wikipedia

print("Retour sur Wikipédia :", driver.title)

print("Test réussi : navigation entre les deux onglets correcte.")

# Pause pour observer les deux onglets
input("Appuie sur Entrée pour fermer Firefox...")

# Fermeture de Firefox et de tous les onglets
driver.quit()