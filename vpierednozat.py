from PyQt5.QtWidgets import*


vopotv=[
    ["Зимой и летом одним цветом","Ёлка","Груша"],
    ["Висит груша, нельзя скушать","Лампочка","Авокадо"],
    ["Не лает, не кусает, в дом не пускает","Замок","Кот"]
]


app = QApplication([])
okno = QWidget()
okno.setStyleSheet("background-image:url('dog-63.jpg')")
# картинку надо скачать и добавить в папку с программой
horline = QHBoxLayout()
okno.setLayout(horline)
#блок кода с группами 
gruppa1 = QGroupBox('Группа 1')
gruppa2 = QGroupBox('Группа 2')
horline.addWidget(gruppa1)
horline.addWidget(gruppa2)
grupline1 = QVBoxLayout()
grupline2 = QVBoxLayout()
gruppa1.setLayout(grupline1)
gruppa2.setLayout(grupline2)

#группа 1
voptxt = QLabel('здесь будет вопрос')
grupline1.addWidget(voptxt)
inline = QHBoxLayout()
grupline1.addLayout(inline)
otv1 = QRadioButton('ответ1')
otv2 = QRadioButton('ответ2')
inline.addWidget(otv1)
inline.addWidget(otv2)

txt1 = QLabel("Нажми, чтобы перейти")
grupline1.addWidget(txt1)
btn1 = QPushButton('==>')
grupline1.addWidget(btn1)
#группа 2
txt2 = QLabel("Нажми, чтобы вернуться")
grupline2.addWidget(txt2)
btn2 = QPushButton('<==')
grupline2.addWidget(btn2)
#прячем вторую группу:
gruppa2.hide()

# по нажатию на кнопку одна группа появляется,
# а другая исчезает

from random import shuffle
shuffle(vopotv)
voptxt.setText(vopotv[0][0])
otv1.setText(vopotv[0][1])
otv2.setText(vopotv[0][2])
otv = QLabel('')
grupline2.addWidget(otv)

def ongr2():
    gruppa2.show()
    gruppa1.hide()
    itog =  'правильный ответ' + vopotv[0][1]
    otv.setText(itog)
btn1.clicked.connect(ongr2)

def ongr1():
    gruppa1.show()
    gruppa2.hide()
    shuffle(vopotv)
    voptxt.setText(vopotv[0][0])
    otv1.setText(vopotv[0][1])
    otv2.setText(vopotv[0][2])
btn2.clicked.connect(ongr1)


okno.show()
app.exec_()