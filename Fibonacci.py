from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QScrollArea,QVBoxLayout, QMainWindow, QToolButton, QLineEdit,QPlainTextEdit
from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
import sys
import threading

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()   
        self.widget = QWidget()                 
        self.vbox = QVBoxLayout()               

        self.setGeometry(0, 0, 750, 850)
        self.setMinimumHeight(850)
        self.setMaximumHeight(850)
        self.setMinimumWidth(750)
        self.setMaximumWidth(750)
        self.setWindowTitle("Sequência de Fibonacci")
        self.setStyleSheet("background-color: rgb(240,240,240);")
        mainWindow_icon = QIcon()
        mainWindow_icon.addPixmap(QPixmap("./src/icones/icon.png"))
        self.setWindowIcon(mainWindow_icon)

        background = QLabel(self)
        background.setStyleSheet("background-color: rgb(255,255,255);")
        background.resize(750, 850)
        background.move(0,0)
        background.setPixmap(QPixmap('./src/icones/background.png'))

        n1_text = QLabel(self)
        n1_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 20px;}")
        n1_text.resize(96,25)
        n1_text.setText("1° Número")
        n1_text.move(80,100)

        n1_line = QLineEdit(self)
        n1_line.setGeometry(100, 125, 50, 30)
        n1_line.setStyleSheet("background-color: rgb(255,255,255);")

        n2_text = QLabel(self)
        n2_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 20px;}")
        n2_text.resize(96,25)
        n2_text.setText("2° Número")
        n2_text.move(580,100)

        n2_line = QLineEdit(self)
        n2_line.setGeometry(600, 125, 50, 30)
        n2_line.setStyleSheet("background-color: rgb(255,255,255);")

        ts_text = QLabel(self)
        ts_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 20px;}")
        ts_text.resize(210,25)
        ts_text.setText("Tamanho da Sequência")
        ts_text.move(270,150)

        ts_line = QLineEdit(self)
        ts_line.setGeometry(350, 175, 50, 30)
        ts_line.setStyleSheet("background-color: rgb(255,255,255);")

        go_button = QToolButton(self)
        go_button.setGeometry(320, 210, 100, 100)
        go_button_icon = QIcon()
        go_button_icon.addPixmap(QPixmap("./src/icones/go.png"))
        go_button.setIcon(go_button_icon)
        go_button.setStyleSheet("background-color: transparent;")
        go_button.setIconSize(QSize(85, 85))

        ults_text = QLabel(self)
        ults_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 18px;}")
        ults_text.resize(750,25)
        ults_text.setText("Último Número da Sequencia: X")
        ults_text.move(50,310)

        ulto_text = QLabel(self)
        ulto_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 18px;}")
        ulto_text.resize(750,25)
        ulto_text.setText("Último Número de Ouro: X")
        ulto_text.move(50,340)

        tls_text = QLabel(self)
        tls_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 20px;}")
        tls_text.resize(210,25)
        tls_text.setText("Sequência de Fibonacci")
        tls_text.move(280,370)

        listas_text = QPlainTextEdit(self)
        listas_text.setStyleSheet("QLabel { background-color : transparent; color : black; font-size : 20px;}")
        listas_text.resize(650,200)
        listas_text.move(50,400)

        tlo_text = QLabel(self)
        tlo_text.setStyleSheet("QLabel { background-color : transparent; color : white; font-size : 20px;}")
        tlo_text.resize(210,25)
        tlo_text.setText("Número de Ouro")
        tlo_text.move(310,600)

        listao_text = QPlainTextEdit(self)
        listao_text.setStyleSheet("QLabel { background-color : transparent; color : black; font-size : 20px;}")
        listao_text.resize(650,200)
        listao_text.move(50,630)

        error = QLabel(self)
        error.setStyleSheet("QLabel { background-color : transparent; color : black; font-size : 25px;}")
        error.resize(425,25)

        def go():
            error.setText("")
            error.move(-100,-100)
            listas_text.clear()
            listao_text.clear()
            try:  
                n1 = (int)(n1_line.text())
                n2 = (int)(n2_line.text())
                g = (int)(ts_line.text())
                lista=[]
                listao=[]
                lista.append(n1)
                lista.append(n2)
                for i in range(1,g-1):
                    listao.append(n2/n1)
                    ns = n1+n2
                    lista.append(ns)
                    n1 = n2
                    n2 = ns
                ults = lista[g-1]
                gos = len(listao)
                ulto = listao[gos-1]
                ults_text.setText(f"Último Número da Sequencia: {ults}")
                ulto_text.setText(f"Último Número de Ouro: {ulto}")
                listas_text.insertPlainText(f"{lista}")
                listao_text.insertPlainText(f"{listao}")
            except:
                ults_text.setText("Último Número da Sequencia: ?")
                ulto_text.setText("Último Número de Ouro: ?")
                error.setText(f"Houve Algum erro, Verique os Inputs!")
                error.move(165,60)

        def go_e(mainWindow):
            threading.Thread(target=go).start()

        go_button.clicked.connect(go_e)


        self.show()
        return



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = mainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()