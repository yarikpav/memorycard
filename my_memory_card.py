#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки задать при создании обекта, они запоминаются  в свойствах
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('Кто такой Юрий Цацын', 'Преподователь', 'Учитель', 'Программист', 'Учёный'))
question_list.append(Question('Что такое Rust?', 'Предмет', 'Имя', 'Игра', 'Музыка'))
question_list.append(Question('Сколько серной кислоты надо потратить для нейтрализации 4 моль гидроксида натрия в случае образования кислой соли?', '4 моль', '20 моль', '1 моль', '12 моль'))
question_list.append(Question('Что не входит в состав С-4?', 'серная кислота', 'пластификатор', 'гексоген', 'полиизобутилен'))
question_list.append(Question('Сколько в сколько в электрашокере вольт?', '50-60кВ', '30-35В', '70мВ', '200В'))
question_list.append(Question('RFisrgjzspdgawefaweyfeh0idqa[8y?', 'фжшркпцпитузкы', 'alsherfguawdkbcfawyoq', 'usrtgsndkvbarug', 'Незнаю'))
question_list.append(Question('Кто сосздал проект Венера', 'Жак Фресско', 'Стивен Хокинг', 'Я', 'Илон Маск'))
question_list.append(Question('akjvrrauwgj;oaeogjbnerlu', 'йпцуайрцдсмйцшп', 'гшркуйцптймрпйцукп', 'ushergjibacuigq', 'нет верного ответа'))
question_list.append(Question('Что такое временная постоянная переменная?', 'Переменная в пространственном покое', 'Это время при остановки часов', 'Незнаю', 'Переменная в полете'))
question_list.append(Question('Сколько составляет высота Бурдж Халифа?', '825м', '850м', '1м', '900м'))
question_list.append(Question('Кто такой Люцифер?', 'Демон', 'Дьявол', 'Бог', 'Человек'))
question_list.append(Question('фипжщшрфмлтпукщжрпгу3324йиа4', 'nitewcgfqw1', 'wuefgajw3gv2', 'gargsaer3', 'ajsrfgasbrfg4'))
question_list.append(Question('й34787834528936523кй3ирфпр34', '2634кагшйциа4738йе', '+77770552381', 'UAJAHjgijhun7834', '34ntc we5hntwo7394'))
question_list.append(Question('Хто я?', 'Незнаю', 'Я', 'I', 'Оно'))
question_list.append(Question('qo34yntq9q8jm8guihw5t', 'yn7og5d', '72gncrj9vhe', 'ygnbwjhe', 'v54nhne'))
question_list.append(Question('uyj7uuuuuuuuuuuuuuuuuuuuuuuuuuuuy6', 'gtfrrrrrrrrrrrrrrrrrrx', 'ggh', 'jhnuuu', 'hjnmg'))
question_list.append(Question(' mcvjmncv,mnvmn', 'uivgboifgvb', 'keghlwtyp8easg', 'ryghcbnm,j,uy', '45drtcfhgn'))
question_list.append(Question('qouierfvniabhvivbu', 'ugsddilueeg', '73tqrgbvaskjver', '28347gyabjvkjberg', 'w9y8tgqwjfiq'))

app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире?')

window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(300, 150)
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('8')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    '''функци записывает значение вопроса и ответов в соответствующие виджеты,
    при этом варианты ответов располодены в случайном образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    '''показать результат - установить переданный текст в надпись 'результат' и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    '''задаёт следующий вопрос из списка'''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильный ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    '''определяет, надо ли показать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()