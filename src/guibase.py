import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QComboBox, QVBoxLayout, QListWidget, \
    QListWidgetItem
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase, QColor, QPainter
import timegetter

# constant(s)
REFRESH_RATE = 50  # ms


class GuiBase(QWidget):
    def __init__(self):
        super().__init__()
        self.label_list = []
        # Title and Window_size
        self.setWindowTitle("The World Time")
        self.setGeometry(100, 100, 1600, 840)
        # Load the worldmap
        self.pixmap = QPixmap("../696072.png")
        self.label_main = QLabel(self)
        self.label_main.setPixmap(self.pixmap)
        self.label_main.setStyleSheet(
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(72,72,180,255), "
            "stop:0.5 rgba(128,128,192,255), stop:1 rgba(72,72,180,255));")
        self.label_main.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())
        # Set the label
        self.cities = [{"Asia/Tokyo": (600, 200)}, {"America/New_York": (1200, 125)},
                       {"Europe/London": (100, 100)}, {"Australia/Sydney": (600, 600)},
                       {"Europe/Moscow": (250, 200)}, {"Asia/Kolkata": (350, 350)},
                       {"America/Los_Angeles": (1000, 250)}, {"America/Argentina/Buenos_Aires": (1250,550)},
                       {"Asia/Shanghai": (500,100)}]
        self.labels = []
        for city in self.cities:
            key = str(list(city.keys())[0])
            label = self.set_text_label(key, city[key][0], city[key][1])
            self.labels.append(label)
        # Set the timer to refresh the time
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_time)
        self.timer.start(REFRESH_RATE)

    def set_text_label(self, timezone, x, y):
        if "Argentina" in timezone:
            city = timezone.split("/")[2].replace("_", " ")
        else:
            city = timezone.split("/")[1].replace("_", " ")
        print(city)
        label = QLabel(self)
        label.setStyleSheet(
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255,192,192,255), "
            "stop:0.8 rgba(204,180,180,204), stop:1 rgba(204,180,180,0));")
        label.setText("<font size=1>{}</font> \n{}".format(city, timegetter.get_time_text(timezone)))
        label.setFont((QFont("A-OTF UD新ゴ Pr6N L", 24, italic=True)))
        # label.setFont((QFont("メイリオ", 24, italic=True)))
        # label.setFont((QFont("A-OTF じゅん Pro 101", 24, italic=True)))
        label.setGeometry(x, y, 350, 60)
        self.label_list.append(label)
        return label

    def create_font_list(self, font_families):
        font_list = QListWidget(self)
        for font_family in font_families:
            font_item = QListWidgetItem(font_family)
            font_list.addItem(font_item)
        return font_list

    def refresh_time(self):
        for i in range(0, len(self.cities)):
            timezone = str(list(self.cities[i].keys())[0])
            if "Argentina" in timezone:
                city = timezone.split("/")[2].replace("_", " ")
            else:
                city = timezone.split("/")[1].replace("_", " ")
            self.labels[i].setText("<font size=1>{}</font> \n{}".format(city, timegetter.get_time_text(timezone)))
