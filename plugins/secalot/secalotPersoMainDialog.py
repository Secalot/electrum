# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secalotPersoMainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecalotPersoMainDialog(object):
    def setupUi(self, SecalotPersoMainDialog):
        SecalotPersoMainDialog.setObjectName("SecalotPersoMainDialog")
        SecalotPersoMainDialog.resize(532, 382)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SecalotPersoMainDialog.sizePolicy().hasHeightForWidth())
        SecalotPersoMainDialog.setSizePolicy(sizePolicy)
        SecalotPersoMainDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(SecalotPersoMainDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.HeaderLabel = QtWidgets.QLabel(SecalotPersoMainDialog)
        self.HeaderLabel.setTextFormat(QtCore.Qt.RichText)
        self.HeaderLabel.setWordWrap(True)
        self.HeaderLabel.setObjectName("HeaderLabel")
        self.gridLayout.addWidget(self.HeaderLabel, 0, 0, 1, 1)
        self.NewOrRestoreGroupBox = QtWidgets.QGroupBox(SecalotPersoMainDialog)
        self.NewOrRestoreGroupBox.setObjectName("NewOrRestoreGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.NewOrRestoreGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CreateNewWalletRadioButton = QtWidgets.QRadioButton(self.NewOrRestoreGroupBox)
        self.CreateNewWalletRadioButton.setChecked(True)
        self.CreateNewWalletRadioButton.setObjectName("CreateNewWalletRadioButton")
        self.gridLayout_2.addWidget(self.CreateNewWalletRadioButton, 0, 0, 1, 1)
        self.RestoreSeedLineEdit = QtWidgets.QLineEdit(self.NewOrRestoreGroupBox)
        self.RestoreSeedLineEdit.setEnabled(False)
        self.RestoreSeedLineEdit.setText("")
        self.RestoreSeedLineEdit.setObjectName("RestoreSeedLineEdit")
        self.gridLayout_2.addWidget(self.RestoreSeedLineEdit, 1, 1, 1, 1)
        self.RestoreWalletRadioButton = QtWidgets.QRadioButton(self.NewOrRestoreGroupBox)
        self.RestoreWalletRadioButton.setObjectName("RestoreWalletRadioButton")
        self.gridLayout_2.addWidget(self.RestoreWalletRadioButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.NewOrRestoreGroupBox, 1, 0, 1, 1)
        self.PINCodeGroupBox = QtWidgets.QGroupBox(SecalotPersoMainDialog)
        self.PINCodeGroupBox.setObjectName("PINCodeGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PINCodeGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PINCodeLabel = QtWidgets.QLabel(self.PINCodeGroupBox)
        self.PINCodeLabel.setObjectName("PINCodeLabel")
        self.verticalLayout.addWidget(self.PINCodeLabel)
        self.PINCodeLineEdit = QtWidgets.QLineEdit(self.PINCodeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PINCodeLineEdit.sizePolicy().hasHeightForWidth())
        self.PINCodeLineEdit.setSizePolicy(sizePolicy)
        self.PINCodeLineEdit.setMaxLength(32)
        self.PINCodeLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PINCodeLineEdit.setObjectName("PINCodeLineEdit")
        self.verticalLayout.addWidget(self.PINCodeLineEdit)
        self.RepeatPINCodeLabel = QtWidgets.QLabel(self.PINCodeGroupBox)
        self.RepeatPINCodeLabel.setObjectName("RepeatPINCodeLabel")
        self.verticalLayout.addWidget(self.RepeatPINCodeLabel)
        self.RepeatPINCodeLineEdit = QtWidgets.QLineEdit(self.PINCodeGroupBox)
        self.RepeatPINCodeLineEdit.setMaxLength(32)
        self.RepeatPINCodeLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RepeatPINCodeLineEdit.setObjectName("RepeatPINCodeLineEdit")
        self.verticalLayout.addWidget(self.RepeatPINCodeLineEdit)
        self.gridLayout.addWidget(self.PINCodeGroupBox, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CreateWalletPushButton = QtWidgets.QPushButton(SecalotPersoMainDialog)
        self.CreateWalletPushButton.setObjectName("CreateWalletPushButton")
        self.horizontalLayout.addWidget(self.CreateWalletPushButton)
        self.CancelPushButton = QtWidgets.QPushButton(SecalotPersoMainDialog)
        self.CancelPushButton.setObjectName("CancelPushButton")
        self.horizontalLayout.addWidget(self.CancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.retranslateUi(SecalotPersoMainDialog)
        self.CancelPushButton.clicked.connect(SecalotPersoMainDialog.reject)
        self.RestoreWalletRadioButton.toggled['bool'].connect(self.RestoreSeedLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(SecalotPersoMainDialog)

    def retranslateUi(self, SecalotPersoMainDialog):
        _translate = QtCore.QCoreApplication.translate
        SecalotPersoMainDialog.setWindowTitle(_translate("SecalotPersoMainDialog", "Secalot Bitcoin Personalization"))
        self.HeaderLabel.setText(_translate("SecalotPersoMainDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Secalot bitcoin personalization</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Here you can personalize the bitcoin application of your Secalot device. You can either create a new wallet, or restore a wallet from a known seed. Plus you need to specify the PIN code for the newly created wallet. PIN length should be between 4 and 32 characters.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.NewOrRestoreGroupBox.setTitle(_translate("SecalotPersoMainDialog", "Wallet"))
        self.CreateNewWalletRadioButton.setText(_translate("SecalotPersoMainDialog", "New wallet"))
        self.RestoreSeedLineEdit.setPlaceholderText(_translate("SecalotPersoMainDialog", "Enter a hexadecimal or a BIP39 mnemonic seed"))
        self.RestoreWalletRadioButton.setText(_translate("SecalotPersoMainDialog", "Restore wallet"))
        self.PINCodeGroupBox.setTitle(_translate("SecalotPersoMainDialog", "New PIN code"))
        self.PINCodeLabel.setText(_translate("SecalotPersoMainDialog", "Enter the new PIN"))
        self.PINCodeLineEdit.setPlaceholderText(_translate("SecalotPersoMainDialog", "Enter your new wallet PIN code"))
        self.RepeatPINCodeLabel.setText(_translate("SecalotPersoMainDialog", "Repeat the new PIN"))
        self.RepeatPINCodeLineEdit.setPlaceholderText(_translate("SecalotPersoMainDialog", "Repeat your new wallet PIN code"))
        self.CreateWalletPushButton.setText(_translate("SecalotPersoMainDialog", "Create Wallet"))
        self.CancelPushButton.setText(_translate("SecalotPersoMainDialog", "Cancel"))

