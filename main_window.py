from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtPrintSupport import *

import os
import sys


def set_cut_action(cut_action, edit_toolbar, edit_menu, window):
    cut_action.setStatusTip("Cut selected text")
    cut_action.triggered.connect(window.editor.cut)
    edit_toolbar.addAction(cut_action)
    edit_menu.addAction(cut_action)


def set_copy_action(copy_action, edit_toolbar, edit_menu, window):
    copy_action.setStatusTip("Copy selected text")
    copy_action.triggered.connect(window.editor.copy)
    edit_toolbar.addAction(copy_action)
    edit_menu.addAction(copy_action)


def set_paste_action(paste_action, edit_toolbar, edit_menu, window):
    paste_action.setStatusTip("Paste from clipboard")
    paste_action.triggered.connect(window.editor.paste)
    edit_toolbar.addAction(paste_action)
    edit_menu.addAction(paste_action)


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

        # standard operations
        cut_action = QAction(
            QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        set_cut_action(cut_action, edit_toolbar, edit_menu, self)

        copy_action = QAction(
            QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        set_copy_action(copy_action, edit_toolbar, edit_menu, self)

        paste_action = QAction(QIcon(os.path.join(
            'images', 'clipboard-paste-document-text.png')), "Paste", self)
        set_paste_action(paste_action, edit_toolbar, edit_menu, self)

        select_action = QAction(
            QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        self.show()
