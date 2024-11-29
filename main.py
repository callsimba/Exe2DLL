from gui import ConverterApp
import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        with open("resources/styles.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: styles.qss not found. Default styles will be used.")

    splash_pix = QPixmap("resources/splash.png")
    if not splash_pix.isNull():
        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setMask(splash_pix.mask())
        splash.showMessage("Loading EXE ↔ DLL Converter...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
        splash.show()
    else:
        splash = None
        print("Warning: Splash image not found. Skipping splash screen.")

    window = ConverterApp()
    if splash:
        splash.finish(window)
    window.show()

    sys.exit(app.exec_())
