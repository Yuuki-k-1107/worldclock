import guibase
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = guibase.GuiBase()
    window.show()
    sys.exit(app.exec_())
