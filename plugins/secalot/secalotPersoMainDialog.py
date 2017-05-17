# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secalotPersoMainDialog.ui'
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

class Ui_SecalotPersoMainDialog(object):
    def setupUi(self, SecalotPersoMainDialog):
        SecalotPersoMainDialog.setObjectName(_fromUtf8("SecalotPersoMainDialog"))
        SecalotPersoMainDialog.resize(550, 335)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SecalotPersoMainDialog.sizePolicy().hasHeightForWidth())
        SecalotPersoMainDialog.setSizePolicy(sizePolicy)
        SecalotPersoMainDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(SecalotPersoMainDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.HeaderLabel = QtGui.QLabel(SecalotPersoMainDialog)
        self.HeaderLabel.setTextFormat(QtCore.Qt.RichText)
        self.HeaderLabel.setWordWrap(True)
        self.HeaderLabel.setObjectName(_fromUtf8("HeaderLabel"))
        self.gridLayout.addWidget(self.HeaderLabel, 0, 0, 1, 1)
        self.NewOrRestoreGroupBox = QtGui.QGroupBox(SecalotPersoMainDialog)
        self.NewOrRestoreGroupBox.setObjectName(_fromUtf8("NewOrRestoreGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.NewOrRestoreGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.CreateNewWalletRadioButton = QtGui.QRadioButton(self.NewOrRestoreGroupBox)
        self.CreateNewWalletRadioButton.setChecked(True)
        self.CreateNewWalletRadioButton.setObjectName(_fromUtf8("CreateNewWalletRadioButton"))
        self.gridLayout_2.addWidget(self.CreateNewWalletRadioButton, 0, 0, 1, 1)
        self.RestoreSeedLineEdit = QtGui.QLineEdit(self.NewOrRestoreGroupBox)
        self.RestoreSeedLineEdit.setEnabled(False)
        self.RestoreSeedLineEdit.setText(_fromUtf8(""))
        self.RestoreSeedLineEdit.setObjectName(_fromUtf8("RestoreSeedLineEdit"))
        self.gridLayout_2.addWidget(self.RestoreSeedLineEdit, 1, 1, 1, 1)
        self.RestoreWalletRadioButton = QtGui.QRadioButton(self.NewOrRestoreGroupBox)
        self.RestoreWalletRadioButton.setObjectName(_fromUtf8("RestoreWalletRadioButton"))
        self.gridLayout_2.addWidget(self.RestoreWalletRadioButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.NewOrRestoreGroupBox, 1, 0, 1, 1)
        self.PINCodeGroupBox = QtGui.QGroupBox(SecalotPersoMainDialog)
        self.PINCodeGroupBox.setObjectName(_fromUtf8("PINCodeGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.PINCodeGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.PINCodeLabel = QtGui.QLabel(self.PINCodeGroupBox)
        self.PINCodeLabel.setObjectName(_fromUtf8("PINCodeLabel"))
        self.verticalLayout.addWidget(self.PINCodeLabel)
        self.PINCodeLineEdit = QtGui.QLineEdit(self.PINCodeGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PINCodeLineEdit.sizePolicy().hasHeightForWidth())
        self.PINCodeLineEdit.setSizePolicy(sizePolicy)
        self.PINCodeLineEdit.setMaxLength(32)
        self.PINCodeLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.PINCodeLineEdit.setObjectName(_fromUtf8("PINCodeLineEdit"))
        self.verticalLayout.addWidget(self.PINCodeLineEdit)
        self.RepeatPINCodeLabel = QtGui.QLabel(self.PINCodeGroupBox)
        self.RepeatPINCodeLabel.setObjectName(_fromUtf8("RepeatPINCodeLabel"))
        self.verticalLayout.addWidget(self.RepeatPINCodeLabel)
        self.RepeatPINCodeLineEdit = QtGui.QLineEdit(self.PINCodeGroupBox)
        self.RepeatPINCodeLineEdit.setMaxLength(32)
        self.RepeatPINCodeLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.RepeatPINCodeLineEdit.setObjectName(_fromUtf8("RepeatPINCodeLineEdit"))
        self.verticalLayout.addWidget(self.RepeatPINCodeLineEdit)
        self.gridLayout.addWidget(self.PINCodeGroupBox, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CreateWalletPushButton = QtGui.QPushButton(SecalotPersoMainDialog)
        self.CreateWalletPushButton.setObjectName(_fromUtf8("CreateWalletPushButton"))
        self.horizontalLayout.addWidget(self.CreateWalletPushButton)
        self.CancelPushButton = QtGui.QPushButton(SecalotPersoMainDialog)
        self.CancelPushButton.setObjectName(_fromUtf8("CancelPushButton"))
        self.horizontalLayout.addWidget(self.CancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.retranslateUi(SecalotPersoMainDialog)
        QtCore.QObject.connect(self.CancelPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SecalotPersoMainDialog.reject)
        QtCore.QObject.connect(self.RestoreWalletRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.RestoreSeedLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(SecalotPersoMainDialog)

    def retranslateUi(self, SecalotPersoMainDialog):
        SecalotPersoMainDialog.setWindowTitle(_translate("SecalotPersoMainDialog", "Secalot Bitcoin Personalization", None))
        self.HeaderLabel.setText(_translate("SecalotPersoMainDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Secalot bitcoin personalization</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Here you can personalize the bitcoin application of your Secalot device. You can either create a new wallet, or restore a wallet from a known seed. Plus you need to specify the PIN code for the newly created wallet. PIN length should be between 4 and 32 characters.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.NewOrRestoreGroupBox.setTitle(_translate("SecalotPersoMainDialog", "Wallet", None))
        self.CreateNewWalletRadioButton.setText(_translate("SecalotPersoMainDialog", "New wallet", None))
        self.RestoreSeedLineEdit.setPlaceholderText(_translate("SecalotPersoMainDialog", "Enter a hexadecimal or a BIP39 mnemonic seed", None))
        self.RestoreWalletRadioButton.setText(_translate("SecalotPersoMainDialog", "Restore wallet", None))
        self.PINCodeGroupBox.setTitle(_translate("SecalotPersoMainDialog", "New PIN code", None))
        self.PINCodeLabel.setText(_translate("SecalotPersoMainDialog", "Enter the new PIN", None))
        self.PINCodeLineEdit.setPlaceholderText(_translate("SecalotPersoMainDialog", "Enter your new wallet PIN code", None))
        self.RepeatPINCodeLabel.setText(_translate("SecalotPersoMainDialog", "Repeat the new PIN", None))
        self.RepeatPINCodeLineEdit.setPlaceholderText(_translate("SecalotPersoMainDialog", "Repeat your new wallet PIN code", None))
        self.CreateWalletPushButton.setText(_translate("SecalotPersoMainDialog", "Create Wallet", None))
        self.CancelPushButton.setText(_translate("SecalotPersoMainDialog", "Cancel", None))

