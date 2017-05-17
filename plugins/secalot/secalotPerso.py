import secalotPersoMainDialog
import secalotPersoDisplaySeedDialog

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog, QMessageBox

from btchip.btchip import btchip

import binascii

from .mnemonic import Mnemonic

class SecalotDisplaySeedDialog(QtGui.QDialog):
    def __init__(self, seed):
        QDialog.__init__(self, None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui = secalotPersoDisplaySeedDialog.Ui_SecalotPersoDisplaySeedDialog()
        self.ui.setupUi(self)
        self.mnemonic = Mnemonic('english')
        self.ui.SeedTextBrowser.setText(self.mnemonic.to_mnemonic(seed))

class SecalotPersoMainDialog(QtGui.QDialog):

    def __init__(self, parent, btchip):
        QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui = secalotPersoMainDialog.Ui_SecalotPersoMainDialog()
        self.ui.setupUi(self)
        self.mnemonic = Mnemonic('english')
        self.dongle = btchip

    @QtCore.pyqtSlot()
    def on_CreateWalletPushButton_clicked(self):

        seed = None
        pin = self.ui.PINCodeLineEdit.text()
        repeatedPin = self.ui.RepeatPINCodeLineEdit.text()
        pinLength = pin.length()

        if pin.compare(repeatedPin) != 0:
            QMessageBox.warning(self, "Error", "PIN codes do not match", "OK")
            return

        if pinLength < 4 or pinLength > 32:
            QMessageBox.warning(self, "Error", "PIN length should be between 4 and 32 characters", "OK")
            return

        if self.ui.RestoreWalletRadioButton.isChecked():
            restoringWallet = True
            seedText = str(self.ui.RestoreSeedLineEdit.text())
            try:
                if seedText.startswith('0X') or seedText.startswith('0x'):
                    seedText = seedText[2:]
                
                seed = seedText.decode('hex')

                if len(seed) > 64 or len(seed) < 32:
                    QMessageBox.warning(self, "Error", "Hexadecimal seed length should be between 32 and 64 bytes", "OK")
                    return
            except:
                try:
                    if self.mnemonic.check(seedText) == False:
                        QMessageBox.warning(self, "Error", "The seed mnemonic is invalid", "OK")
                        return
                    seed = Mnemonic.to_seed(seedText)
                except:
                    QMessageBox.warning(self, "Error", "The seed mnemonic is invalid", "OK")
                    return
        else:
            restoringWallet = False

        try:
            setupResult = self.dongle.setup(btchip.OPERATION_MODE_WALLET, btchip.FEATURE_RFC6979, 0x00, 0x05, str(pin), '', '', seed)
        except Exception as e:
            QMessageBox.warning(self, "Error", "Personalization failed", "OK")
            return

        if not restoringWallet:
            setupResult = setupResult['trustedInputKey'] + setupResult['developerKey']
            setupResult.pop(0)
            displaySeedDialog = SecalotDisplaySeedDialog(setupResult)
            displaySeedDialog.exec_()
        else:
            QMessageBox.information(self, "Success", "Your new wallet is successfully created", "OK")
            

        self.done(QDialog.Accepted)
