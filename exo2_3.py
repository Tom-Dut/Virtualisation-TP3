import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


PAUSE = 2


def pause():
    time.sleep(PAUSE)


DOSSIER_SCRIPT = os.path.dirname(os.path.abspath(__file__))

FICHIER_HTML = os.path.join(
    DOSSIER_SCRIPT,
    "contact.html"
)

URL = "file://" + FICHIER_HTML


# Configuration Firefox
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

service = Service("/home/tom/.local/bin/geckodriver")

driver = webdriver.Firefox(
    service=service,
    options=options
)


try:

    # ==========================================================
    # TEST 1 : FORMULAIRE CORRECT

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
        "messageContact"
    ).send_keys("Bonjour, ceci est un test Selenium.")

    pause()

    driver.find_element(
        By.ID,
        "envoyer"
    ).click()

    pause()

    resultat = driver.find_element(
        By.ID,
        "resultat"
    )

    assert "Message envoyé avec succès" in resultat.text

    print("TEST 1 réussi : formulaire envoyé.")

    # ==========================================================
    # TEST 2 : EMAIL INVALIDE

    driver.get(URL)

    pause()

    driver.find_element(
        By.ID,
        "nom"
    ).send_keys("Tom")

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("emailincorrect")

    driver.find_element(
        By.ID,
        "messageContact"
    ).send_keys("Mon message.")

    pause()

    driver.find_element(
        By.ID,
        "envoyer"
    ).click()

    pause()

    resultat = driver.find_element(
        By.ID,
        "resultat"
    )

    assert "email invalide" in resultat.text

    print("TEST 2 réussi : email invalide détecté.")

    # ==========================================================
    # TEST 3 : MESSAGE VIDE

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

    # On ne remplit volontairement pas le message

    pause()

    driver.find_element(
        By.ID,
        "envoyer"
    ).click()

    pause()

    resultat = driver.find_element(
        By.ID,
        "resultat"
    )

    assert "required field" in resultat.text

    print("TEST 3 réussi : message vide détecté.")

    input("Appuie sur Entrée pour fermer Firefox...")


except Exception as erreur:

    capture = os.path.join(
        DOSSIER_SCRIPT,
        "error_contact.png"
    )

    driver.save_screenshot(capture)

    print("Le test a échoué.")
    print("Capture créée :", capture)
    print("Erreur :", erreur)

    raise


finally:

    driver.quit()