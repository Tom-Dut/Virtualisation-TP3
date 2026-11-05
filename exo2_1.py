import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Durée de pause entre les actions pour voir ce qu'il se passe
PAUSE = 1.5


# Fonction permettant de ralentir le scénario
def pause():
    time.sleep(PAUSE)


# Configuration de Firefox
options = Options()
options.binary_location = "/home/tom/Applications/firefox/firefox"

# Configuration de geckodriver
service = Service("/home/tom/.local/bin/geckodriver")

# Création du navigateur Firefox
driver = webdriver.Firefox(
    service=service,
    options=options
)

# Création d'une attente explicite de 10 secondes
wait = WebDriverWait(driver, 10)


try:

    # ==========================================================
    # TEST 1 : CONNEXION INVALIDE

    # Ouverture de SauceDemo
    driver.get("https://www.saucedemo.com/")
    pause()

    # Recherche du champ username
    champ_nom = driver.find_element(
        By.ID,
        "user-name"
    )

    # Saisie d'un mauvais utilisateur
    champ_nom.send_keys("mauvais_utilisateur")
    pause()

    # Recherche du champ password
    champ_mdp = driver.find_element(
        By.ID,
        "password"
    )

    # Saisie d'un mauvais mot de passe
    champ_mdp.send_keys("mauvais_mot_de_passe")
    pause()

    # Clic sur le bouton Login
    driver.find_element(
        By.ID,
        "login-button"
    ).click()

    pause()

    # Attente de l'affichage du message d'erreur
    message_erreur = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    # Vérification qu'une erreur est bien affichée
    assert "Epic sadface" in message_erreur.text

    print("TEST 1 réussi : connexion invalide détectée.")

    pause()

    # ==========================================================
    # TEST 2 : CONNEXION VALIDE

    # Recherche du champ username
    champ_nom = driver.find_element(
        By.ID,
        "user-name"
    )

    # On vide le champ
    champ_nom.clear()

    # On entre le bon utilisateur
    champ_nom.send_keys("standard_user")

    pause()

    # Recherche du champ password
    champ_mdp = driver.find_element(
        By.ID,
        "password"
    )

    # On vide le champ
    champ_mdp.clear()

    # On entre le bon mot de passe
    champ_mdp.send_keys("secret_sauce")

    pause()

    # Clic sur Login
    driver.find_element(
        By.ID,
        "login-button"
    ).click()

    # Attente de la page des produits
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "inventory_container")
        )
    )

    pause()

    # Vérification que nous sommes sur la page inventory
    assert "inventory" in driver.current_url

    print("TEST 2 réussi : connexion valide.")

    # ==========================================================
    # TEST 3 : AJOUT DE PRODUITS AU PANIER

    # Recherche du bouton Add to cart du Backpack
    bouton_backpack = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    # Ajout du Backpack
    bouton_backpack.click()

    pause()

    # Recherche du bouton Add to cart du Bike Light
    bouton_bike = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    )

    # Ajout du Bike Light
    bouton_bike.click()

    pause()

    # Recherche du compteur du panier
    compteur_panier = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    # Vérification qu'il y a bien deux produits
    assert compteur_panier.text == "2"

    print("TEST 3 réussi : 2 produits ajoutés au panier.")

    pause()

    # ==========================================================
    # TEST 4 : SUPPRESSION D'UN PRODUIT

    # Ouverture du panier
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Attente de la page panier
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_list")
        )
    )

    pause()

    # Suppression du Bike Light
    driver.find_element(
        By.ID,
        "remove-sauce-labs-bike-light"
    ).click()

    pause()

    # Recherche du compteur
    compteur_panier = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    # Vérification qu'il reste un produit
    assert compteur_panier.text == "1"

    print("TEST 4 réussi : un produit a été supprimé.")

    pause()

    # ==========================================================
    # TEST 5 : PASSAGE DE LA COMMANDE

    # Clic sur Checkout
    driver.find_element(
        By.ID,
        "checkout"
    ).click()

    pause()

    # Remplissage du prénom
    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys("Tom")

    pause()

    # Remplissage du nom
    driver.find_element(
        By.ID,
        "last-name"
    ).send_keys("Dupont")

    pause()

    # Remplissage du code postal
    driver.find_element(
        By.ID,
        "postal-code"
    ).send_keys("62300")

    pause()

    # Clic sur Continue
    driver.find_element(
        By.ID,
        "continue"
    ).click()

    pause()

    # ==========================================================
    # TEST 6 : VERIFICATION DU PRIX

    # Récupération du prix du produit
    prix_texte = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    # Suppression du symbole $
    prix_produit = float(
        prix_texte.replace("$", "")
    )

    # Récupération du sous-total
    sous_total_texte = driver.find_element(
        By.CLASS_NAME,
        "summary_subtotal_label"
    ).text

    # Transformation du sous-total en nombre
    sous_total = float(
        sous_total_texte.replace(
            "Item total: $",
            ""
        )
    )

    # Vérification du prix
    assert prix_produit == sous_total

    print(
        "TEST 6 réussi : prix correct :",
        sous_total,
        "$"
    )

    pause()

    # ==========================================================
    # TEST 7 : VALIDATION DE LA COMMANDE

    # Clic sur Finish
    driver.find_element(
        By.ID,
        "finish"
    ).click()

    pause()

    # Attente du message de confirmation
    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    # Vérification du message
    assert "Thank you for your order!" in confirmation.text

    print("TEST 7 réussi : commande validée.")

    pause()

    # ==========================================================
    # TEST 8 : DECONNEXION
    

    # Ouverture du menu
    driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    ).click()

    pause()

    # Attente du bouton Logout
    bouton_logout = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "logout_sidebar_link")
        )
    )

    # Déconnexion
    bouton_logout.click()

    pause()

    # Vérification du retour sur la page Login
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        )
    )

    print("TEST 8 réussi : déconnexion réussie.")

    print("Tous les tests SauceDemo sont réussis.")

    # Pause finale
    input("Appuie sur Entrée pour fermer Firefox...")


except Exception as erreur:

    # Capture d'écran automatique en cas d'échec
    driver.save_screenshot(
        "error_saucedemo.png"
    )

    print("Le test a échoué.")
    print("Capture créée : error_saucedemo.png")
    print("Erreur :", erreur)

    # L'erreur est relancée pour que le test reste en échec
    raise


finally:

    # Fermeture de Firefox dans tous les cas
    driver.quit()