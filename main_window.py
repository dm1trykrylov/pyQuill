from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QFile, QTextStream
from PyQt5.QtPrintSupport import QPrintDialog

import os

from utility import *

import json
import qdarktheme


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Open configuration file
        config_file = open('settings.json')
        config = json.load(config_file)

        # Set theme
        if config['use_default_theme'] == True:
             self.toggle_theme_default(config['theme'])
        else:
            self.toggle_theme_custom(config['stylesheet'])

        # Setup the QTextEdit editor configuration
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()

        # Setup default font
        font = QFont(config['default_font']['font_name'],
                     config['default_font']['size'])
        self.editor.setFont(font)

        # Path of the currently open file
        self.path = None
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # edit toolbar
        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")

        # Set standard file actions
        set_open_file_action(file_menu, file_toolbar, self)
        set_save_file_action(file_menu, file_toolbar, self)
        set_saveas_file_action(file_menu, file_toolbar, self)
        set_print_action(file_menu, file_toolbar, self)

        # Set standard operations
        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        set_undo_action(edit_menu, edit_toolbar, self)
        set_redo_action(edit_menu, edit_toolbar, self)

        edit_menu.addSeparator()

        set_cut_action(edit_toolbar, edit_menu, self)
        set_copy_action(edit_toolbar, edit_menu, self)
        set_paste_action(edit_toolbar, edit_menu, self)
        set_select_action(edit_menu, self)
        set_wrap_action(edit_menu, self)
        #set_find_action(edit_menu, self)

        self.update_title()
        self.show()
        config_file.close()

    def show_error(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def toggle_theme_default(self, theme):
        try:
            if theme == 'dark':
                app = QApplication.instance()
                app.setStyleSheet(qdarktheme.load_stylesheet(theme))
        except Exception as e:
            self.show_error(self, e)

    def toggle_theme_custom(self, path):
        try:
            app = QApplication.instance()
            file = QFile(path)
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            app.setStyleSheet(stream.readAll())
        except Exception as e:
            self.show_error(e)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.show_error(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def save_file(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.saveas_file()

        self._save_to_path(self.path)

    def saveas_file(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.show_error(str(e))

        else:
            self.path = path
            self.update_title()

    def print_file(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle(
            "{:s} - pyQuill".format(os.path.basename(self.path) if self.path else "Untitled"))

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(
            1 if self.editor.lineWrapMode() == 0 else 0)
