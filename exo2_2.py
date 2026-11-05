import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Durée entre les actions pour pouvoir observer Selenium
PAUSE = 2


def pause():
    time.sleep(PAUSE)


# Récupération du dossier
DOSSIER_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# Création du chemin vers notre page HTML 
FICHIER_HTML = os.path.join(
    DOSSIER_SCRIPT,
    "inscription.html"
)

# Transformation en URL utilisable par Firefox
URL = "file://" + FICHIER_HTML


# Configuration de Firefox
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration de geckodriver
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur
driver = webdriver.Firefox(
    service=service,
    options=options
)

# Attente explicite
wait = WebDriverWait(driver, 10)


try:

    # ==========================================================
    # TEST 1 : CHAMP OBLIGATOIRE MANQUANT

    driver.get(URL)

    pause()

    # On ne remplit volontairement pas le nom

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("tom@example.com")

    pause()

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("motdepasse123")

    pause()

    # Validation
    driver.find_element(
        By.ID,
        "inscription"
    ).click()

    pause()

    # Récupération du message
    message = driver.find_element(
        By.ID,
        "message"
    )

    # Vérification
    assert "champ obligatoire manquant" in message.text

    print("TEST 1 réussi : champ manquant détecté.")

    # ==========================================================
    # TEST 2 : EMAIL INVALIDE

    driver.get(URL)

    pause()

    driver.find_element(
        By.ID,
        "nom"
    ).send_keys("Tom")

    pause()

    # Email volontairement faux
    driver.find_element(
        By.ID,
        "email"
    ).send_keys("tomexample.com")

    pause()

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("motdepasse123")

    pause()

    driver.find_element(
        By.ID,
        "inscription"
    ).click()

    pause()

    message = driver.find_element(
        By.ID,
        "message"
    )

    assert "email invalide" in message.text

    print("TEST 2 réussi : email invalide détecté.")

    # ==========================================================
    # TEST 3 : MOT DE PASSE TROP COURT

    driver.get(URL)

    pause()

    driver.find_element(
        By.ID,
        "nom"
    ).send_keys("Tom")

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("tom@example.com")

    pause()

    # Seulement 3 caractères
    driver.find_element(
        By.ID,
        "password"
    ).send_keys("abc")

    pause()

    driver.find_element(
        By.ID,
        "inscription"
    ).click()

    pause()

    message = driver.find_element(
        By.ID,
        "message"
    )

    assert "mot de passe trop court" in message.text

    print("TEST 3 réussi : mot de passe faible détecté.")

    # ==========================================================
    # TEST 4 : INSCRIPTION CORRECTE

    driver.get(URL)

    pause()

    driver.find_element(
        By.ID,
        "nom"
    ).send_keys("Tom")

    pause()

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("tom@example.com")

    pause()

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("motdepasse123")

    pause()

    driver.find_element(
        By.ID,
        "inscription"
    ).click()

    pause()

    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    assert "Inscription réussie" in message.text

    print("TEST 4 réussi : inscription correcte.")

    input("Appuie sur Entrée pour fermer Firefox...")


except Exception as erreur:

    # Création du chemin de la capture
    capture = os.path.join(
        DOSSIER_SCRIPT,
        "error_inscription.png"
    )

    # Capture de l'état du navigateur au moment de l'erreur
    driver.save_screenshot(capture)

    print("Le test a échoué.")
    print("Capture créée :", capture)
    print("Erreur :", erreur)

    raise


finally:

    driver.quit()