from PyQt4 import QtGui,QtCore
import sys
import ui_main
import numpy as np
import pylab
import time

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        #self.btnAdd.clicked.connect(self.update)
        self.matplotlibwidget.axes.hold(False) #clear on plot()
        self.matplotlibwidget.axes.set_axis_bgcolor('none') # make a transparent graph background
        self.matplotlibwidget.figure.set_facecolor('none') # make a transparent frame background

    def update(self):
        t1=time.time()
        nPoints=100 #number of data points
        Xs=np.arange(nPoints)+time.time()*3 # make an X axis
        Ys=np.sin(Xs/8) # add some slowly moving data
        Xs-=Xs[0] # make X-axis start at 0
        self.matplotlibwidget.axes.plot(Xs,Ys,alpha=.5,lw=2)
        self.matplotlibwidget.axes.grid()
        self.matplotlibwidget.axes.margins(0,0.1)
        self.matplotlibwidget.axes.get_figure().tight_layout() # fill space
        self.matplotlibwidget.draw() # required to update the window
        print("update took %.02f ms"%((time.time()-t1)*1000))
        QtCore.QTimer.singleShot(100, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")