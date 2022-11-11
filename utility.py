from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
import os


def set_cut_action(edit_toolbar, edit_menu, window):
    cut_action = QAction(
        QIcon(os.path.join('images', 'scissors.png')), "Cut", window)
    cut_action.setStatusTip("Cut selected text")
    cut_action.triggered.connect(window.editor.cut)
    edit_toolbar.addAction(cut_action)
    edit_menu.addAction(cut_action)


def set_copy_action(edit_toolbar, edit_menu, window):
    copy_action = QAction(
        QIcon(os.path.join('images', 'document-copy.png')), "Copy", window)
    copy_action.setStatusTip("Copy selected text")
    copy_action.triggered.connect(window.editor.copy)
    edit_toolbar.addAction(copy_action)
    edit_menu.addAction(copy_action)


def set_paste_action(edit_toolbar, edit_menu, window):
    paste_action = QAction(QIcon(os.path.join(
        'images', 'clipboard-paste-document-text.png')), "Paste", window)
    paste_action.setStatusTip("Paste from clipboard")
    paste_action.triggered.connect(window.editor.paste)
    edit_toolbar.addAction(paste_action)
    edit_menu.addAction(paste_action)


def set_select_action(edit_toolbar, edit_menu, window):
    select_action = QAction(
        QIcon(os.path.join('images', 'selection-input.png')), "Select all", window)
    select_action.setStatusTip("Select all text")
    select_action.triggered.connect(window.editor.selectAll)
    edit_toolbar.addAction(select_action)
    edit_menu.addAction(select_action)
