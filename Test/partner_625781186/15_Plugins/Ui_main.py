# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QGroup_432987409\WoHowLearn\0_M_I_pyqt\partner_625781186\15_Plugins\main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 378)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 510, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_Recent_Files = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_Recent_Files.setObjectName("menuOpen_Recent_Files")
        self.menufile1 = QtWidgets.QMenu(self.menuOpen_Recent_Files)
        self.menufile1.setObjectName("menufile1")
        self.menufile11 = QtWidgets.QMenu(self.menufile1)
        self.menufile11.setObjectName("menufile11")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.actionadd1 = QtWidgets.QAction(MainWindow)
        self.actionadd1.setObjectName("actionadd1")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionfile2 = QtWidgets.QAction(MainWindow)
        self.actionfile2.setObjectName("actionfile2")
        self.actionfile3 = QtWidgets.QAction(MainWindow)
        self.actionfile3.setObjectName("actionfile3")
        self.actionfile11 = QtWidgets.QAction(MainWindow)
        self.actionfile11.setObjectName("actionfile11")
        self.actionfile22 = QtWidgets.QAction(MainWindow)
        self.actionfile22.setObjectName("actionfile22")
        self.actionfile111 = QtWidgets.QAction(MainWindow)
        self.actionfile111.setObjectName("actionfile111")
        self.menufile11.addAction(self.actionfile111)
        self.menufile1.addAction(self.menufile11.menuAction())
        self.menufile1.addAction(self.actionfile22)
        self.menuOpen_Recent_Files.addAction(self.menufile1.menuAction())
        self.menuOpen_Recent_Files.addAction(self.actionfile2)
        self.menuOpen_Recent_Files.addAction(self.actionfile3)
        self.menuFile.addAction(self.actionadd1)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuOpen_Recent_Files.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "modulePath"))
        self.pushButton_3.setText(_translate("MainWindow", "replace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_Recent_Files.setTitle(_translate("MainWindow", "Open Recent Files"))
        self.menufile1.setTitle(_translate("MainWindow", "file1"))
        self.menufile11.setTitle(_translate("MainWindow", "file11"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionadd1.setText(_translate("MainWindow", "New Window"))
        self.actionsave.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionfile2.setText(_translate("MainWindow", "file2"))
        self.actionfile3.setText(_translate("MainWindow", "file3"))
        self.actionfile11.setText(_translate("MainWindow", "file11"))
        self.actionfile22.setText(_translate("MainWindow", "file22"))
        self.actionfile111.setText(_translate("MainWindow", "file111"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

