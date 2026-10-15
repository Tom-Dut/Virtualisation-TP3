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

try:
    # Ouverture de la page de connexion
    driver.get("https://the-internet.herokuapp.com/login")

    # Recherche du champ username
    champ_username = driver.find_element(
        By.ID,
        "username"
    )

    # Saisie du nom d'utilisateur
    champ_username.send_keys("tomsmith")

    # Recherche du champ password
    champ_password = driver.find_element(
        By.ID,
        "password"
    )

    # Saisie du mot de passe
    champ_password.send_keys("SuperSecretPassword!")

    # Recherche et clic sur le bouton Login
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    # Attente du message de connexion
    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "flash")
        )
    )

    # Vérification du message
    assert "You logged into a secure area!" in message.text

    print("Test réussi : connexion correcte.")

except Exception as erreur:
    # Si une erreur survient, création automatique d'une capture d'écran
    driver.save_screenshot("error_login.png")

    # Affichage d'un message dans le terminal
    print("Le test a échoué.")
    print("Capture enregistrée dans error_login.png")
    print("Erreur :", erreur)

    # Relance l'erreur afin que le test reste considéré comme échoué
    raise

finally:
    # Fermeture du navigateur dans tous les cas
    driver.quit()