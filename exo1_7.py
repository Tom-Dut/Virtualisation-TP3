from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
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

# Ouverture de la page de connexion
driver.get("https://the-internet.herokuapp.com/login")

# Recherche du champ username grâce à son id
champ_username = driver.find_element(
    By.ID,
    "username"
)

# Saisie du bon nom d'utilisateur
champ_username.send_keys("tomsmith")

# Recherche du champ password grâce à son id
champ_password = driver.find_element(
    By.ID,
    "password"
)

# Saisie du bon mot de passe
champ_password.send_keys("SuperSecretPassword!")

# Recherche du bouton Login
bouton_login = driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
)

# Clic sur Login
bouton_login.click()

# Attente de l'apparition du message de connexion
message = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "flash")
    )
)

# Vérification du message de connexion
assert "You logged into a secure area!" in message.text

print("Connexion valide réussie.")

# Recherche du bouton Logout
bouton_logout = wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Logout")
    )
)

# Déconnexion
bouton_logout.click()

# Attente du retour vers la page login
wait.until(
    EC.url_contains("/login")
)

# Vérification de la redirection
assert "/login" in driver.current_url

print("Déconnexion réussie.")

# Recherche à nouveau du champ username
champ_username = driver.find_element(
    By.ID,
    "username"
)

# Saisie d'un mauvais nom d'utilisateur
champ_username.send_keys("mauvaisUtilisateur")

# Recherche du champ password
champ_password = driver.find_element(
    By.ID,
    "password"
)

# Saisie d'un mauvais mot de passe
champ_password.send_keys("mauvaisMotDePasse")

# Clic sur Login
driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
).click()

# Attente du message d'erreur
message_erreur = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "flash")
    )
)

# Vérification qu'un message d'erreur est affiché
assert "invalid" in message_erreur.text.lower()

print("Connexion invalide correctement détectée.")
print("Message :", message_erreur.text)

# Pause pour observer le résultat
input("Appuie sur Entrée pour fermer Firefox...")

# Fermeture du navigateur
driver.quit()