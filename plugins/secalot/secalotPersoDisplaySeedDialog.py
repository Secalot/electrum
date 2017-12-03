# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secalotPersoDisplaySeedDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecalotPersoDisplaySeedDialog(object):
    def setupUi(self, SecalotPersoDisplaySeedDialog):
        SecalotPersoDisplaySeedDialog.setObjectName("SecalotPersoDisplaySeedDialog")
        SecalotPersoDisplaySeedDialog.resize(627, 362)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SecalotPersoDisplaySeedDialog.sizePolicy().hasHeightForWidth())
        SecalotPersoDisplaySeedDialog.setSizePolicy(sizePolicy)
        SecalotPersoDisplaySeedDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SecalotPersoDisplaySeedDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SecalotPersoDisplaySeedDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.SeedTextBrowser = QtWidgets.QTextBrowser(SecalotPersoDisplaySeedDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeedTextBrowser.sizePolicy().hasHeightForWidth())
        self.SeedTextBrowser.setSizePolicy(sizePolicy)
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
        self.label.setText(_translate("SecalotPersoDisplaySeedDialog", "Your new wallet is created. Your new wallet\'s seed is written below. Please save it in a safe place, so you would be able to restore your wallet in case your Secalot device gets stolen or damaged.\n"
"\n"
"Please note that:\n"
"1. Anybody getting access to your seed would have access to you wallet and all the bitcoins on it.\n"
"2. It is safer to store your seed in a non-electronic form, for example on paper.\n"
""))

