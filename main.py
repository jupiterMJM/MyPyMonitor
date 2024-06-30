import zenoh
import time
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

def listener(sample):
    global curve, p6, data
    print(f"Received data: {sample.payload.decode('utf-8')}")
    data.append(float(sample.payload.decode('utf-8')))
    curve.setData(data)
  

data = list()
win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')
# and we add a plotItem to the window
p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen="red")  # color the plot (the background is automatically black


def main():
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


if __name__ == "__main__":
    main()