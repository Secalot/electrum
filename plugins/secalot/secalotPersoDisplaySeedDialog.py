# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secalotPersoDisplaySeedDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecalotPersoDisplaySeedDialog(object):
    def setupUi(self, SecalotPersoDisplaySeedDialog):
        SecalotPersoDisplaySeedDialog.setObjectName("SecalotPersoDisplaySeedDialog")
        SecalotPersoDisplaySeedDialog.resize(587, 313)
        SecalotPersoDisplaySeedDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SecalotPersoDisplaySeedDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HeaderLabel = QtWidgets.QLabel(SecalotPersoDisplaySeedDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeaderLabel.sizePolicy().hasHeightForWidth())
        self.HeaderLabel.setSizePolicy(sizePolicy)
        self.HeaderLabel.setWordWrap(True)
        self.HeaderLabel.setObjectName("HeaderLabel")
        self.verticalLayout.addWidget(self.HeaderLabel)
        self.SeedTextBrowser = QtWidgets.QTextBrowser(SecalotPersoDisplaySeedDialog)
        self.SeedTextBrowser.setObjectName("SeedTextBrowser")
        self.verticalLayout.addWidget(self.SeedTextBrowser)
        self.SeedDialogButtonBox = QtWidgets.QDialogButtonBox(SecalotPersoDisplaySeedDialog)
        self.SeedDialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.SeedDialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.SeedDialogButtonBox.setObjectName("SeedDialogButtonBox")
        self.verticalLayout.addWidget(self.SeedDialogButtonBox)

        self.retranslateUi(SecalotPersoDisplaySeedDialog)
        self.SeedDialogButtonBox.accepted.connect(SecalotPersoDisplaySeedDialog.accept)
        self.SeedDialogButtonBox.rejected.connect(SecalotPersoDisplaySeedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SecalotPersoDisplaySeedDialog)

    def retranslateUi(self, SecalotPersoDisplaySeedDialog):
        _translate = QtCore.QCoreApplication.translate
        SecalotPersoDisplaySeedDialog.setWindowTitle(_translate("SecalotPersoDisplaySeedDialog", "New wallet created"))
        self.HeaderLabel.setText(_translate("SecalotPersoDisplaySeedDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Your new wallet is created. Your new wallet\'s seed is written below. Please save it in a safe place, so you would be able to restore your wallet in case your Secalot device gets stolen or damaged.</span></p><p><span style=\" font-size:10pt;\">Please note that</span></p><p><span style=\" font-size:10pt;\">1. Anybody getting access to your seed would have access to you wallet and all the bitcoins on it.</span></p><p><span style=\" font-size:10pt;\">2. It is safer to store your seed in a non-electronic form, for example on paper.</span></p><p><br/></p></body></html>"))

