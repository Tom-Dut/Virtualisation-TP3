from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration de Firefox
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration de geckodriver
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur Firefox
driver = webdriver.Firefox(service=service, options=options)

# Création d'une attente explicite de 10 secondes maximum
wait = WebDriverWait(driver, 10)

# Ouverture de la page du formulaire
driver.get("https://testpages.herokuapp.com/pages/forms/html-form/")

# Recherche de la liste déroulante
champ_dropdown = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "select[name='dropdown']")
    )
)

# Transformation de l'élément en liste déroulante Selenium
liste_dropdown = Select(champ_dropdown)

# Sélection du deuxième élément de la liste
liste_dropdown.select_by_visible_text("Drop Down Item 2")

# Recherche de toutes les cases à cocher
checkboxes = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

# Sélection de la deuxième case
if not checkboxes[1].is_selected():
    checkboxes[1].click()

# Recherche de tous les boutons radio
radios = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='radio']"
)

# Sélection du deuxième bouton radio
radios[1].click()

# Mémorisation de l'URL avant validation
ancienne_url = driver.current_url

# Recherche du bouton Submit
bouton_submit = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='submit']"
)

# Validation du formulaire
bouton_submit.click()

# Attente jusqu'au changement de page
wait.until(
    EC.url_changes(ancienne_url)
)

# Vérification que nous avons bien changé de page
assert driver.current_url != ancienne_url

print("Test réussi : liste, checkbox et radio sélectionnés, formulaire validé.")

# Pause pour voir le résultat
input("Appuie sur Entrée pour fermer Firefox...")

# Fermeture du navigateur
driver.quit()