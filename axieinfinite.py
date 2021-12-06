import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont, QCursor, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QByteArray


class App(QWidget):

  def __init__(self):
    super().__init__()
    self.title = 'Axie INFINITE'
    self.left = 0
    self.top = 0
    self.width = 500
    self.height = 730
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    self.setStyleSheet("background-color: rgb(255, 255, 255);")
    self.setWindowFlags(
      Qt.WindowType.CustomizeWindowHint | 
      Qt.WindowType.WindowCloseButtonHint | 
      Qt.WindowType.WindowMinimizeButtonHint | 
      Qt.MSWindowsFixedSizeDialogHint
    )

    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

    pixmap = QPixmap(32, 32)
    pixmap.fill(Qt.transparent)

    self.setWindowIcon(QIcon(pixmap))
    
    self.createInput("Ronda", 170, 90, 0, "i1")
    self.createInput("1", 170, 120, 1, "i2")
    self.createInput("Energías", 170, 150, 2, "i3")
    self.createInput("3", 170, 180, 3, "i4")

    self.createButton("Energía -1", 10, 220, "e-1")
    self.createButton("Energía +1", 170, 220, "e+1")
    self.createButton("Siguiente Ronda", 330, 220, "s")
    self.createButton("Nueva Partida", 170, 260, "n")

    self.loadImage()

  def createInput(self, text, x, y, number, obj):
    textBox = QTextEdit(self)

    if number == 0:
      font = QFont("Arial", 10)
      textBox.setStyleSheet("background-color: rgb(221, 235, 247);")
    if number == 1:
      font = QFont("Arial", 11)
    if number == 2:
      font = QFont("Arial", 10)
      textBox.setStyleSheet("background-color: rgb(255, 217, 102);")
    if number == 3:  
      font = QFont("Arial", 13)
      textBox.setStyleSheet("background-color: rgb(255, 242, 204);")

    font.setBold(True)
    
    textBox.setReadOnly(True)
    textBox.setFixedSize(152, 30)
    textBox.setText(text)
    textBox.setFont(font)
    textBox.setAlignment(Qt.AlignCenter)
    textBox.move(x, y)

    if obj == "i1":
      self.textBox1 = textBox
    if obj == "i2":
      self.textBox2 = textBox
    if obj == "i3":
      self.textBox3 = textBox
    if obj == "i4":
      self.textBox4 = textBox

  def createButton(self, text, x, y, inp):
    font = QFont("Arial", 11)
    font.setBold(True)

    button = QPushButton(self)
    button.setFixedSize(152, 30)
    button.setText(text)
    button.move(x, y)
    button.setFont(font)
    button.setCursor(QCursor(Qt.PointingHandCursor))

    if inp == "n":
      button.clicked.connect(self.newGame)
      button.setStyleSheet("background-color: rgb(191, 191, 191);")
    if inp == "e-1":
      button.clicked.connect(self.energyMe)
      button.setStyleSheet("background-color: rgb(255, 124, 128);")
    if inp == "e+1":
      button.clicked.connect(self.energyMa)
      button.setStyleSheet("background-color: rgb(146, 208, 80);")
    if inp == "s":
      button.clicked.connect(self.next)
      button.setStyleSheet("background-color: rgb(191, 191, 191);")

  def energyMe(self):
    energy = int(self.textBox4.toPlainText())
    if energy > 0:
      energy -= 1

    self.textBox4.setText(str(energy))
    self.textBox4.setAlignment(Qt.AlignCenter)

  def energyMa(self):
    energy = int(self.textBox4.toPlainText())
    if energy < 10:
      energy += 1

    self.textBox4.setText(str(energy))
    self.textBox4.setAlignment(Qt.AlignCenter)

  def next(self):
    energy = int(self.textBox4.toPlainText())
    round = int(self.textBox2.toPlainText())
    energy += 2
    round += 1

    if energy > 10:
      energy = 10

    self.textBox4.setText(str(energy))
    self.textBox2.setText(str(round))
    self.textBox4.setAlignment(Qt.AlignCenter)
    self.textBox2.setAlignment(Qt.AlignCenter)

  def newGame(self):
    self.textBox2.setText("1")
    self.textBox4.setText("3")
    self.textBox2.setAlignment(Qt.AlignCenter)
    self.textBox4.setAlignment(Qt.AlignCenter)

  def loadImage(self):
    label = QLabel(self)
    pm = QPixmap("t1.png")
    label.setPixmap(pm)
    label.resize(pm.width(), pm.height())
    label.move(150, 10)

    label2 = QLabel(self)
    pm = QPixmap("t2.png")
    label2.setPixmap(pm)
    label2.resize(pm.width(), pm.height())
    label2.move(50, 300)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = App()
  ex.show()
  sys.exit(app.exec_())  
