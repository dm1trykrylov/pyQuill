import sys
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication

import qdarktheme
import json

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("pyQuill")
    window = MainWindow()


    app.exec_()
