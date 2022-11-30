import sys
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
app.setApplicationName("pyQuill")
window = MainWindow()
app.exec_()
