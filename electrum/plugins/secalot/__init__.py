from electrum.i18n import _

fullname = 'Secalot Wallet'
description = 'Provides support for Secalot hardware wallet'
requires = [('btchip', 'github.com/ledgerhq/btchip-python')]
registers_keystore = ('hardware', 'secalot', _("Secalot wallet"))
available_for = ['qt']
