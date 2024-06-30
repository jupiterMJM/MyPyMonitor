"""
:auteur: Maxence Barré
:fichier: essai_client_zenoh.py
:comment: un exemple de client zenoh. Par exemple, ce fichier pourrait représenter un capteur quelconque qui enverrait
    des données scalaires à intervalles régulier.
"""

# importation des modules
import zenoh
import random as r
import time as t

# création du client
def client():
    """
    :comment: cette fonction permet de simuler un client qui enverraient des données à intervalles régulier
    """
    # Initialize Zenoh
    print("[INFO] Initialisation of zenoh")
    z = zenoh.open()

    # Declare a publisher
    print("[INFO] Initialisation of the publisher")
    pub = z.declare_publisher('demo/example/hello')     # on déclare ici l'adresse sur laquelle les données sont envoyées
    try:
        while True:
            to_send = str(r.randint(0, 9))
            print("[INFO] Sending data: ", to_send)
            pub.put(to_send)               # on envoie des données à intervalle régulier
            t.sleep(1)
    except:
        print("[INFO] Closing the zenoh connection")
        z.close()                                       # on ferme la connexion

if __name__ == '__main__':
    client()
    print("[INFO] End of the program")