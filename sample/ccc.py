import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt


class IncrementerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Incrementer')
        self.setGeometry(100, 100, 300, 100)

        # ラベルの作成
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        # レイアウトの作成
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # インクリメント用のタイマーの作成
        self.timer = QTimer()
        self.timer.timeout.connect(self.increment)
        self.timer.start(1000)  # 1000ミリ秒 = 1秒ごとにタイマーが発火

        # 初期値の設定
        self.counter = 0

    def increment(self):
        self.counter += 1
        self.label.setText(str(self.counter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IncrementerApp()
    window.show()
    sys.exit(app.exec_())
