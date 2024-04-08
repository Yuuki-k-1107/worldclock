import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QFontDatabase, QFont

# フォントのテスト

class FontListTab(QWidget):
    def __init__(self):
        super().__init__()

        # フォントデータベースの初期化
        font_db = QFontDatabase()

        # フォントファミリーのリストを取得
        font_families = font_db.families()

        # フォントリストの作成
        font_list = QListWidget()
        for font_family in font_families:
            font_item = QListWidgetItem(font_family)
            font_list.addItem(font_item)

        # フォント名を表示するラベル
        font_label = QLabel()

        # フォントファミリーが選択されたときの動作
        def on_font_selected():
            selected_font_family = font_list.currentItem().text()
            font_label.setText(f'Selected Font: {selected_font_family}')
            font_label.setFont(QFont(selected_font_family))

        font_list.currentItemChanged.connect(on_font_selected)

        # レイアウトの設定
        layout = QVBoxLayout()
        layout.addWidget(font_list)
        layout.addWidget(font_label)

        self.setLayout(layout)

class FontListApp(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Font List')

        # タブの作成
        font_tab = FontListTab()
        self.addTab(font_tab, 'Font List')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontListApp()
    window.show()
    sys.exit(app.exec_())
