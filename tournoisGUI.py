# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tournois.ui'
#
# Created: Wed Nov  9 23:04:49 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(715, 519)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 691, 431))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabDept = QtGui.QWidget()
        self.tabDept.setObjectName(_fromUtf8("tabDept"))
        self.lbDept = QtGui.QListView(self.tabDept)
        self.lbDept.setGeometry(QtCore.QRect(10, 10, 201, 371))
        self.lbDept.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lbDept.setObjectName(_fromUtf8("lbDept"))
        self.btnNext = QtGui.QPushButton(self.tabDept)
        self.btnNext.setGeometry(QtCore.QRect(560, 350, 94, 27))
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.tabWidget.addTab(self.tabDept, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL(_fromUtf8("triggered(QAction*)")), MainWindow.menuClick)
        QtCore.QObject.connect(self.btnNext, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.btnNextClick)
        QtCore.QObject.connect(self.lbDept, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.lbClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnNext.setText(_translate("MainWindow", "Suivant", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDept), _translate("MainWindow", "Départements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Poules", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

