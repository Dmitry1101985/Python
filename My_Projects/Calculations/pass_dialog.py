from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QInputDialog
import sys

class PasswordDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Создаем кнопку, по нажатию на которую будет вызываться диалог
        self.btn = QPushButton('Enter Password', self)
        self.btn.clicked.connect(self.showDialog)

        # Создаем текстовое поле, в которое будет введен пароль
        self.le = QLineEdit(self)
        self.le.setEchoMode(QLineEdit.Password)

        # Добавляем виджеты на вертикальный layout
        layout.addWidget(self.btn)
        layout.addWidget(self.le)

        # Устанавливаем layout на окно
        self.setLayout(layout)
        self.setWindowTitle('Password Dialog')

    def showDialog(self):
        # Вызываем стандартный диалог для ввода пароля
        text, ok = QInputDialog.getText(self, 'Password Dialog', 'Enter password:', QLineEdit.Password)

        if ok:
            # Пользователь нажал OK, сохраняем введенный пароль в текстовое поле
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordDialog()
    ex.show()
    sys.exit(app.exec_())
