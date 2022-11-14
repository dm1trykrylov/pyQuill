from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
import os


def set_open_file_action(file_menu, file_toolbar, window):
    open_file_action = QAction(QIcon(os.path.join(
        'images', 'blue-folder-open-document.png')), "Open file...", window)
    open_file_action.setStatusTip("Open file")
    open_file_action.triggered.connect(window.open_file)
    file_menu.addAction(open_file_action)
    file_toolbar.addAction(open_file_action)


def set_save_file_action(file_menu, file_toolbar, window):
    save_file_action = QAction(
        QIcon(os.path.join('images', 'disk.png')), "Save", window)
    save_file_action.setStatusTip("Save current page")
    save_file_action.triggered.connect(window.save_file)
    file_menu.addAction(save_file_action)
    file_toolbar.addAction(save_file_action)


def set_saveas_file_action(file_menu, file_toolbar, window):
    saveas_file_action = QAction(
        QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", window)
    saveas_file_action.setStatusTip("Save current page to specified file")
    saveas_file_action.triggered.connect(window.saveas_file)
    file_menu.addAction(saveas_file_action)
    file_toolbar.addAction(saveas_file_action)


def set_print_action(file_menu, file_toolbar, window):
    print_action = QAction(
        QIcon(os.path.join('images', 'printer.png')), "Print...", window)
    print_action.setStatusTip("Print current page")
    print_action.triggered.connect(window.print_file)
    file_menu.addAction(print_action)
    file_toolbar.addAction(print_action)


def set_undo_action(edit_menu, edit_toolbar, window):
    undo_action = QAction(
        QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", window)
    undo_action.setStatusTip("Undo last change")
    undo_action.triggered.connect(window.editor.undo)
    edit_toolbar.addAction(undo_action)
    edit_menu.addAction(undo_action)


def set_redo_action(edit_menu, edit_toolbar, window):
    redo_action = QAction(
        QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", window)
    redo_action.setStatusTip("Redo last change")
    redo_action.triggered.connect(window.editor.redo)
    edit_toolbar.addAction(redo_action)
    edit_menu.addAction(redo_action)


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


def set_select_action(edit_menu, window):
    select_action = QAction(
        QIcon(os.path.join('images', 'selection-input.png')), "Select all", window)
    select_action.setStatusTip("Select all text")
    select_action.triggered.connect(window.editor.selectAll)
    edit_menu.addAction(select_action)


def set_wrap_action(edit_menu, window):
    wrap_action = QAction(QIcon(os.path.join(
        'images', 'arrow-continue.png')), "Wrap text to window", window)
    wrap_action.setStatusTip("Toggle wrap text to window")
    wrap_action.setCheckable(True)
    wrap_action.setChecked(True)
    wrap_action.triggered.connect(window.edit_toggle_wrap)
    edit_menu.addAction(wrap_action)
