from PyQt4 import uic 
fin = open('ui_main.ui','r')
fout = open('ui_main.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()