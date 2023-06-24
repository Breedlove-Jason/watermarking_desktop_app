import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QIcon
from PyQt5.QtCore import Qt


class WatermarkingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Watermarking App")
        self.setGeometry(200, 200, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(20, 20, 400, 400)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.watermark_label = QPushButton("Add Text Watermark", self)
        self.watermark_label.setGeometry(450, 50, 200, 30)
        self.watermark_label.clicked.connect(self.open_watermark)

        self.watermark_logo = QPushButton("Add Watermark Logo", self)
        self.watermark_logo.setGeometry(450, 100, 200, 30)
        self.watermark_logo.clicked.connect(self.open_watermark_logo)

        self.show()

    def open_watermark(self):
        pass

    def open_watermark_logo(self):
        pass
