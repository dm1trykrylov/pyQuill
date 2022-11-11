from PyQt5.QtGui import QIcon, QFont

from PyQt5.QtWidgets import QVBoxLayout, QPlainTextEdit, QWidget, QToolBar, QAction, QMainWindow
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtPrintSupport import *

import os

from utility import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Setup the QTextEdit editor configuration
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()

        # Setup default font
        font = QFont('Ubuntu', 12)
        self.editor.setFont(font)
        self.editor.setFont(font)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # edit toolbar
        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        # Set standard operations
        set_cut_action(edit_toolbar, edit_menu, self)
        set_copy_action(edit_toolbar, edit_menu, self)
        set_paste_action(edit_toolbar, edit_menu, self)
        set_select_action(edit_toolbar, edit_menu, self)

        self.show()
