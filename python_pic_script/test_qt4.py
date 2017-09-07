from PyQt4 import QtGui, QtCore
import sys

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self)
		
		self.resize(550, 450)
		self.setWindowTitle('main')
		
		exit = QtGui.QAction(QtGui.QIcon('exit.png'), u'exit', self)
		exit.setShortcut('ctrl+Q')
		exit.setStatusTip(u'exit process')
		exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))
		
		self.statusBar()
		
		menubar = self.menuBar()
		f = menubar.addMenu(u'file')
		f.addAction(exit)

app = QtGui.QApplication([])
main = MainWindow()
main.show()
sys.exit(app.exec_())
