# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secalotPersoDisplaySeedDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_SecalotPersoDisplaySeedDialog(object):
    def setupUi(self, SecalotPersoDisplaySeedDialog):
        SecalotPersoDisplaySeedDialog.setObjectName(_fromUtf8("SecalotPersoDisplaySeedDialog"))
        SecalotPersoDisplaySeedDialog.resize(550, 270)
        SecalotPersoDisplaySeedDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SecalotPersoDisplaySeedDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.HeaderLabel = QtGui.QLabel(SecalotPersoDisplaySeedDialog)
        self.HeaderLabel.setWordWrap(True)
        self.HeaderLabel.setObjectName(_fromUtf8("HeaderLabel"))
        self.verticalLayout.addWidget(self.HeaderLabel)
        self.SeedTextBrowser = QtGui.QTextBrowser(SecalotPersoDisplaySeedDialog)
        self.SeedTextBrowser.setObjectName(_fromUtf8("SeedTextBrowser"))
        self.verticalLayout.addWidget(self.SeedTextBrowser)
        self.SeedDialogButtonBox = QtGui.QDialogButtonBox(SecalotPersoDisplaySeedDialog)
        self.SeedDialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.SeedDialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.SeedDialogButtonBox.setObjectName(_fromUtf8("SeedDialogButtonBox"))
        self.verticalLayout.addWidget(self.SeedDialogButtonBox)

        self.retranslateUi(SecalotPersoDisplaySeedDialog)
        QtCore.QObject.connect(self.SeedDialogButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SecalotPersoDisplaySeedDialog.accept)
        QtCore.QObject.connect(self.SeedDialogButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SecalotPersoDisplaySeedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SecalotPersoDisplaySeedDialog)

    def retranslateUi(self, SecalotPersoDisplaySeedDialog):
        SecalotPersoDisplaySeedDialog.setWindowTitle(_translate("SecalotPersoDisplaySeedDialog", "New wallet created", None))
        self.HeaderLabel.setText(_translate("SecalotPersoDisplaySeedDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Your new wallet is created. Your new wallet\'s seed is written below. Please save it in a safe place, so you would be able to restore your wallet in case your Secalot device gets stolen or damaged.</span></p><p><span style=\" font-size:10pt;\">Please note that</span></p><p><span style=\" font-size:10pt;\">1. Anybody getting access to your seed would have access to you wallet and all the bitcoins on it.</span></p><p><span style=\" font-size:10pt;\">2. It is safer to store your seed in a non-electronic form, for example on paper.</span></p><p><br/></p></body></html>", None))

