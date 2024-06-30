"""
:auteur: Maxence Barré
:fichier: main.py
:version: 0.1
:comment: le programme fonctionne actuellement dans le cas où il n'y a qu'une seule source de données
"""

# importation des modules
import zenoh
import time
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

# definition de la fonction d'écoute
def listener(sample):
    """
    fonction d'écoute
    :param: sample
    :comment: cette fonction est exécutée à chaque fois que le lien zenoh associé est mis-à-jour
    """
    global curve, p6, data
    print(f"Received data: {sample.payload.decode('utf-8')}")
    data.append(float(sample.payload.decode('utf-8')))
    curve.setData(data)
  

def main():
    """
    fonction principale
    :comment: le seul intéret que ca soit sous forme de fonction est de mieux gérer la fin de programme
    """
    try:
        print("opening server")
        z = zenoh.open()
        sub = z.declare_subscriber('demo/example/**', listener)
        pg.exec()
    except KeyboardInterrupt:
        print("[INFO] Exception occured; shutting down the program")
        win.close()
        z.close()
    finally:
        z.close()
        print("[INFO] End of the program")


# mise en place de la fenêtre graphique
data = list()
win = pg.GraphicsLayoutWidget(show=True, title="MyPyMonitor v0.1")
win.resize(1000, 600)
win.setWindowTitle('pyqtgraph example: Plotting')
p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen="red")

if __name__ == "__main__":
    main()