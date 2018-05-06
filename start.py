#!/usr/sbin/env python3

import locale
import sys
from os import path

from PyQt5.QtWidgets import QApplication

DIRECTORY_PROGRAM = sys._MEIPASS if getattr(sys, "frozen", False) else path.dirname(path.realpath(__file__))
APPLICATION_VERSION = "0.0.1"
APPLICATION_NAME = "mpv-qc"

if __name__ == "__main__":
    # todo validation if mpv dependencies are installed and display a message box if not

    from src.gui.uihandler.main import MainHandler

    app = QApplication(sys.argv)

    locale.setlocale(locale.LC_NUMERIC, "C")

    container = MainHandler(app)
    container.show()

    sys.exit(app.exec_())
