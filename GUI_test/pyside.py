import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QLineEdit, QVBoxLayout
from PySide6.QtCore import Slot


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print(f"Hello {self.edit.text()}")


# @Slot(str)
# def say_hello(word):
#     app1 = QApplication(sys.argv)
#     label = QLabel(word)
#     label.show()
#     app1.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()

    sys.exit(app.exec())
    # app = QApplication(sys.argv)
    # label = QLabel("Hello World")
    # button = QPushButton("Click me")
    # word = "Button clicked, Hello!"
    # button.clicked.connect(say_hello(word))
    # button.show()
    # # label.show()
    # app.exec()
