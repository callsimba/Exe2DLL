from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QLineEdit, QVBoxLayout, QTabWidget, QHBoxLayout, QWidget, QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QIcon
from converter import exe_to_dll, dll_to_exe
import sys


class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: #0078d7; color: white; border-radius: 5px; padding: 5px 10px;")
        self.animation = QPropertyAnimation(self, b"geometry")

    def enterEvent(self, event):
        self.animation.setDuration(200)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.geometry().adjusted(-2, -2, 2, 2))
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDuration(200)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.geometry().adjusted(2, 2, -2, -2))
        self.animation.start()
        super().leaveEvent(event)


class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXE ↔ DLL Converter")
        self.setGeometry(300, 200, 600, 400)
        self.setWindowIcon(QIcon("resources/icon.ico"))
        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        self.exe_to_dll_tab = self.create_exe_to_dll_tab()
        tabs.addTab(self.exe_to_dll_tab, "EXE to DLL")
        self.dll_to_exe_tab = self.create_dll_to_exe_tab()
        tabs.addTab(self.dll_to_exe_tab, "DLL to EXE")
        self.about_tab = self.create_about_tab()
        tabs.addTab(self.about_tab, "About")
        self.setCentralWidget(tabs)

    def create_exe_to_dll_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        input_label = QLabel("Select EXE file:")
        self.exe_input_path = QLineEdit()
        browse_input = AnimatedButton("Browse")
        browse_input.clicked.connect(self.browse_exe_input)
        layout.addWidget(input_label)
        layout.addWidget(self.exe_input_path)
        layout.addWidget(browse_input)
        output_label = QLabel("Destination DLL path:")
        self.dll_output_path = QLineEdit()
        browse_output = AnimatedButton("Browse")
        browse_output.clicked.connect(self.browse_dll_output)
        layout.addWidget(output_label)
        layout.addWidget(self.dll_output_path)
        layout.addWidget(browse_output)
        convert_button = AnimatedButton("Convert to DLL")
        convert_button.clicked.connect(self.convert_exe_to_dll)
        layout.addWidget(convert_button)
        tab.setLayout(layout)
        return tab

    def create_dll_to_exe_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        input_label = QLabel("Select DLL file:")
        self.dll_input_path = QLineEdit()
        browse_input = AnimatedButton("Browse")
        browse_input.clicked.connect(self.browse_dll_input)
        layout.addWidget(input_label)
        layout.addWidget(self.dll_input_path)
        layout.addWidget(browse_input)
        output_label = QLabel("Destination EXE path:")
        self.exe_output_path = QLineEdit()
        browse_output = AnimatedButton("Browse")
        browse_output.clicked.connect(self.browse_exe_output)
        layout.addWidget(output_label)
        layout.addWidget(self.exe_output_path)
        layout.addWidget(browse_output)
        convert_button = AnimatedButton("Convert to EXE")
        convert_button.clicked.connect(self.convert_dll_to_exe)
        layout.addWidget(convert_button)
        tab.setLayout(layout)
        return tab

    def create_about_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        about_message = QLabel(
            """
            <h2>EXE ↔ DLL Converter</h2>
            <p>This software was built by <b>Call Simba</b> for <b>CallEnki</b>.</p>
            <p>It is designed to help you seamlessly convert EXE files to DLL files and vice versa.</p>
            <p><i>Version: 1.1.0</i></p>
            """
        )
        about_message.setWordWrap(True)
        about_message.setStyleSheet("font-size: 14px; color: #333; margin: 10px;")
        layout.addWidget(about_message)
        tab.setLayout(layout)
        return tab

    def browse_exe_input(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select EXE File", "", "Executable Files (*.exe)")
        if file_name:
            self.exe_input_path.setText(file_name)

    def browse_dll_output(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Destination", "", "DLL Files (*.dll)")
        if file_name:
            self.dll_output_path.setText(file_name)

    def browse_dll_input(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select DLL File", "", "Dynamic Link Library Files (*.dll)")
        if file_name:
            self.dll_input_path.setText(file_name)

    def browse_exe_output(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Destination", "", "Executable Files (*.exe)")
        if file_name:
            self.exe_output_path.setText(file_name)

    def convert_exe_to_dll(self):
        exe_path = self.exe_input_path.text()
        dll_path = self.dll_output_path.text()
        if exe_path and dll_path:
            success, message = exe_to_dll(exe_path, dll_path)
            self.show_message("EXE to DLL Conversion", message, success)
        else:
            self.show_message("Error", "Please specify both input and output paths.", False)

    def convert_dll_to_exe(self):
        dll_path = self.dll_input_path.text()
        exe_path = self.exe_output_path.text()
        if dll_path and exe_path:
            success, message = dll_to_exe(dll_path, exe_path)
            self.show_message("DLL to EXE Conversion", message, success)
        else:
            self.show_message("Error", "Please specify both input and output paths.", False)

    def show_message(self, title, message, success=True):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information if success else QMessageBox.Critical)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())
