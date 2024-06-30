"""
:auteur: Maxence Barré
:fichier: essai_serveur_zenoh.py
:comment: un exemple de server zenoh. Ce programme vient uniquement écouter une adresse zenoh quelconque et affiche les données
    à chaque mise-à-jour.
"""

# importation des modules
import zenoh
import time

# création du listener, cad la fonction qui écoute
def listener(sample):
    """
    cette fonction est éxecutée à chaque fois que les données sont mises à jour
    """
    print(f"Received data: {sample.payload.decode('utf-8')}")

def server():
    # Initialize Zenoh
    print("[INFO] Initialisation of zenoh")
    z = zenoh.open()

    # Declare a subscriber
    print("[INFO] Initialisation of the publisher")
    sub = z.declare_subscriber('demo/example/**', listener)

    try:
        print("[INFO] listening for data")
        while True:
            time.sleep(1)       # juste pour tourner dans le vide
    except KeyboardInterrupt:
        print("Terminating server.")
    finally:
        print("[INFO] closing server")
        z.close()

if __name__ == '__main__':
    server()
    print("[INFO] End of the program")
