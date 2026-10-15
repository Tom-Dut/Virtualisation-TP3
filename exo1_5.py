from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import os

# Configuration de Firefox
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration de geckodriver
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur Firefox contrôlé par Selenium
driver = webdriver.Firefox(service=service, options=options)

# Création d'une attente explicite de maximum 10 secondes
wait = WebDriverWait(driver, 10)

# Ouverture du formulaire demandé dans le TP
driver.get(
    "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
)

# Recherche du champ Name grâce à son id
#wait.until permet d'attendre que la zone soit remplis 
champ_nom = wait.until(
    EC.visibility_of_element_located((By.ID, "name"))
)

# Remplissage du nom
champ_nom.send_keys("Tom")

# Recherche du champ Email grâce à son placeholder
champ_email = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='name@example.com']"
)

# Remplissage de l'adresse email
champ_email.send_keys("tom@example.com")

# Recherche du bouton radio Male
bouton_genre = driver.find_elements(
    By.XPATH,
    "//*[@id='practiceForm']//input[@type='radio'][1]"
)

# Sélection du genre
bouton_genre[2].click()

# Recherche du champ Mobile
champ_mobile = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Enter Mobile Number']"
)

# Remplissage du numéro de téléphone
champ_mobile.send_keys("0612345678")

# Recherche du champ Date of Birth
date_naissance = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='date']"
)

# Remplissage de la date de naissance ( en format HTML)
date_naissance.send_keys("2006-10-18")

# Recherche du champ Subjects
champ_sujet = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Enter Subject']"
)

# Remplissage du sujet
champ_sujet.send_keys("Selenium")

# Recherche de la première case à cocher Hobbies
case_hobby = driver.find_elements(
    By.XPATH,
    "//*[@id='practiceForm']//input[@type='checkbox'][1]"
)

# Coche la case
case_hobby[1].click()
case_hobby[2].click()


# Recherche du champ permettant de choisir un fichier
champ_image = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='file']"
)

# Création du chemin absolu vers l'image
chemin_image = os.path.abspath("imagetest.png")

# Envoi du fichier dans le champ Picture
champ_image.send_keys(chemin_image)

# Recherche de la zone Current Address
champ_adresse = driver.find_element(
    By.TAG_NAME,
    "textarea"
)


# Remplissage de l'adresse
champ_adresse.send_keys("Lens, France")


# Recherche de la liste State grâce à son id
champ_state = driver.find_element(By.ID, "state")

# Transformation de l'élément en liste déroulante Selenium
liste_state = Select(champ_state)

# Sélection de NCR grâce au texte visible
liste_state.select_by_visible_text("NCR")

# Attente jusqu'à ce que les villes soient chargées après le choix de l'État
wait.until(
    lambda d: len(
        Select(d.find_element(By.ID, "city")).options
    ) > 1
)

# Recherche de la liste City grâce à son id
champ_city = driver.find_element(By.ID, "city")

# Transformation en liste déroulante Selenium
liste_city = Select(champ_city)

# Sélection de Meerut grâce au texte visible
liste_city.select_by_visible_text("Meerut")

# Vérification que le bon État est sélectionné
assert liste_state.first_selected_option.text == "NCR"

# Vérification que la bonne ville est sélectionnée
assert liste_city.first_selected_option.text == "Meerut"


# Recherche du bouton Submit
bouton_submit = driver.find_element(
    By.XPATH,
    "//*[@id='practiceForm']/div[11]/input"
)

# Descend automatiquement jusqu'au bouton
driver.execute_script(
    "arguments[0].scrollIntoView();",
    bouton_submit
)

# Validation du formulaire
bouton_submit.click()

# Affichage d'un message une fois le clic effectué
print("Le formulaire a été rempli et validé.")

# Pause pour observer le résultat dans Firefox
input(" appuie sur Entrée pour fermer Firefox")

# Fermeture du navigateur
driver.quit()