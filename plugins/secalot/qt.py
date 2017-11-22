import threading

from PyQt5.Qt import (QDialog, QInputDialog, QLineEdit,
                      QVBoxLayout, QLabel)
import PyQt5.QtCore as QtCore

from electrum.i18n import _
from .secalot import SecalotPlugin
from ..hw_wallet.qt import QtHandlerBase, QtPluginBase
from electrum_gui.qt.util import *

from .secalotPerso import SecalotPersoMainDialog

class Plugin(SecalotPlugin, QtPluginBase):
    icon_unpaired = ":icons/secalot_unpaired.png"
    icon_paired = ":icons/secalot.png"

    def create_handler(self, window):
        return Secalot_Handler(window)


class Secalot_Handler(QtHandlerBase):

    def __init__(self, win):
        super(Secalot_Handler, self).__init__(win, 'Secalot')

    def word_dialog(self, msg):
        response = QInputDialog.getText(self.top_level_window(), "Secalot Wallet Authentication", msg, QLineEdit.Password)
        if not response[1]:
            self.word = None
        else:
            self.word = str(response[0])
        self.done.set()

    def perso_dialog(self, dongleObject):
        dialog = SecalotPersoMainDialog(self.top_level_window(), dongleObject)
        dialog.exec_()

        return dialog.result()
