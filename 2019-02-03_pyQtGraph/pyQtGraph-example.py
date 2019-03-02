"""
Minimal-case example how to launch a standalone, interactive, pyqtgraph

First install pyqtgraph with: 
     pip install --upgrade pyqtgraph
"""
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np

# set the styling of pyqtgraph
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

# create some data
pointCount = 1000
xs = np.arange(pointCount)/pointCount*np.pi*2*5
ys = np.sin(xs)

# add noise
ys += np.random.random_sample(len(ys))/10

# create plot
plt = pg.plot(xs, ys, title="Example PyQtGraph", pen='r')
plt.showGrid(x=True,y=True)

## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()