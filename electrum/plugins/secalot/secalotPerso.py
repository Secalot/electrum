from .secalotPersoMainDialog import Ui_SecalotPersoMainDialog
from  .secalotPersoDisplaySeedDialog import Ui_SecalotPersoDisplaySeedDialog

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog, QLineEdit

from btchip.btchip import btchip

import binascii

from .mnemonic import Mnemonic

class SecalotDisplaySeedDialog(QDialog):
    def __init__(self, entropy):
        QDialog.__init__(self, None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui = Ui_SecalotPersoDisplaySeedDialog()
        self.ui.setupUi(self)
        self.mnemonic = Mnemonic('english')
        self.ui.SeedTextBrowser.setText(self.mnemonic.to_mnemonic(entropy))

class SecalotPersoMainDialog(QDialog):

    def __init__(self, parent, btchip):
        QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui = Ui_SecalotPersoMainDialog()
        self.ui.setupUi(self)
        self.mnemonic = Mnemonic('english')
        self.dongle = btchip

    @QtCore.pyqtSlot()
    def on_CreateWalletPushButton_clicked(self):

        seed = None
        pin = self.ui.PINCodeLineEdit.text()
        repeatedPin = self.ui.RepeatPINCodeLineEdit.text()
        pinLength = len(pin)

        if pin != repeatedPin:
            QMessageBox.warning(self, "Error", "PIN codes do not match", QMessageBox.Ok)
            return

        if pinLength < 4 or pinLength > 32:
            QMessageBox.warning(self, "Error", "PIN length should be between 4 and 32 characters", QMessageBox.Ok)
            return

        if self.ui.RestoreWalletRadioButton.isChecked():
            restoringWallet = True
            seedText = str(self.ui.RestoreSeedLineEdit.text())
            try:
                if seedText.startswith('0X') or seedText.startswith('0x'):
                    seedText = seedText[2:]

                seed = bytearray.fromhex(seedText)

                if len(seed) > 64 or len(seed) < 32:
                    QMessageBox.warning(self, "Error", "Hexadecimal seed length should be between 32 and 64 bytes", QMessageBox.Ok)
                    return
            except:
                try:
                    if self.mnemonic.check(seedText) == False:
                        QMessageBox.warning(self, "Error", "The seed mnemonic is invalid", QMessageBox.Ok)
                        return
                    seed = self.mnemonic.to_seed(seedText)
                except:
                    QMessageBox.warning(self, "Error", "The seed mnemonic is invalid", QMessageBox.Ok)
                    return
        else:
            entropy = self.dongle.getRandom(32)
            phrase = self.mnemonic.to_mnemonic(entropy)
            seed = self.mnemonic.to_seed(phrase)
            restoringWallet = False

        try:
            setupResult = self.dongle.setup(btchip.OPERATION_MODE_WALLET, btchip.FEATURE_RFC6979, 0x00, 0x05, str(pin), '', '', seed)
        except Exception as e:
            QMessageBox.warning(self, "Error", "Personalization failed", QMessageBox.Ok)
            return

        if not restoringWallet:
            displaySeedDialog = SecalotDisplaySeedDialog(entropy)
            displaySeedDialog.exec_()
        else:
            QMessageBox.information(self, "Success", "Your new wallet is successfully created", QMessageBox.Ok)
            

        self.done(QDialog.Accepted)
