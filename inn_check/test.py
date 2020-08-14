# -*- encoding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont

from input_check_test import is_inn


class Communicate(QObject):
    closeApp = pyqtSignal()


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lbl = QLabel('Введите ИНН : ', self)  # лейбл
        self.textbox = QTextEdit(self)  # окно для ввода текста
        self.btn_ok = QPushButton("OK", self)  # кнопка ОК
        self.btn_clr = QPushButton("Clear", self)  # кнопка очистки
        self.btn_exit = QPushButton("Exit", self)  # кнопка выхода

        self.clr = Communicate()
        self.init_ui()

    def init_ui(self):
        # Начальный вид окна
        self.setWindowTitle('Inn check')
        self.setGeometry(350, 350, 350, 350)

        # textBox для ввода данных
        self.textbox.move(20, 50)
        self.textbox.resize(310, 170)

        # лейбл
        self.lbl.resize(150, 30)
        self.lbl.move(18, 10)
        self.lbl.setFont(QFont("Arial", 18, QFont.Black))

        # Для кнопок можно сделать блочную верстку !!!
        # Кнопка Exit
        self.btn_exit.move(15, 300)
        self.btn_exit.resize(320, 40)

        # Кнопка OK
        self.btn_ok.move(185, 250)
        self.btn_ok.resize(150, 40)

        # Кнопка Clear
        self.btn_clr.move(15, 250)
        self.btn_clr.resize(150, 40)

        # Выход при нажатии на окно (убрать)
        self.clr.closeApp.connect(self.close)

        # Выход при нажатии на Exit (мб переписать)
        self.btn_exit.clicked.connect(sys.exit)

        # Очистка при нажатии на Clear (как бы стирает, но остаются "следы")
        self.btn_clr.clicked.connect(self.clear_text)

        # Вывод в коммандную строку результатов при нажатии ОК
        self.btn_ok.clicked.connect(self.input_data)

        # Показываем всю красоту
        self.show()

    # Функция обработки нажатия мышки
    def mousePressEvent(self, event):
        self.clr.closeApp.emit()

    # функция очистки экрана (найти/придумать что получше)
    def clear_text(self):
        self.textbox.setText("")

    # функция вывода в командную строку из textBox и обработка (ее написать отдельными модулями)
    def input_data(self):
        text = self.textbox.toPlainText()
        # print(text)
        # собираем списки с инн и с ошибками
        list_for_culc, list_error = is_inn(text)
        print(' Для дальнейших расчетов : ', list_for_culc, '\n', 'Ошибки : ', list_error)
        # очищаем после расчетов --> мб и не нужно если есть clear
        # self.clear_text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
