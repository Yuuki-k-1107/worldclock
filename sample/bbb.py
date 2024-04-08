import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QLabel
from PyQt5.QtGui import QFont

class FontSwitcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Font Switcher')
        self.setGeometry(100, 100, 400, 100)

        # フォントのリストを作成
        self.fonts = ['Arial', 'Times New Roman', 'Courier New']

        # コンボボックスの作成
        self.font_combo = QComboBox()
        self.font_combo.addItems(self.fonts)
        self.font_combo.currentIndexChanged.connect(self.update_font)

        # ラベルの作成
        self.label = QLabel('Hello, World!')

        # レイアウトの作成
        layout = QHBoxLayout()
        layout.addWidget(self.font_combo)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def update_font(self):
        # 選択されたフォントを取得し、ラベルのフォントを更新
        font_name = self.font_combo.currentText()
        font = QFont(font_name, 16)  # フォントサイズは16に設定
        self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontSwitcher()
    window.show()
    sys.exit(app.exec_())
