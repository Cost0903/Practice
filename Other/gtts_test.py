"""
The pdf translate to mp3 file script
I want to format those texts into speech so I can hear them.
And it will save mime time also.

First, I need to custom input the file name, speed range, output file name,
maybe I need to call the mp3 player to play it.

Finally, I will package it to exe file, and I can use it on windows or another platform
"""
import os
from gtts import gTTS
import PyPDF2
import pyttsx3
import subprocess
import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QLineEdit, QVBoxLayout
from PySide6.QtCore import Slot


class Form(QDialog):
    """
    Form for the input

    Args:
        QDialog (_type_): _description_
    """

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.input = QLineEdit("The input file.")
        self.output = QLineEdit("The output file.")
        self.button = QPushButton("Translate")

        layout = QVBoxLayout(self)
        layout.addWidget(self.input)
        layout.addWidget(self.output)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.translate)

    # def translate(self):
    #     """
    #     text to speech
    #     """
    #     print(f"Hello {self.edit.text()}")


def translate(file, output):
    """
    read the pdf file

    Args:
        file (String): The file name.
        output (String): The output name.
        speed (String): The speed of reading.
    """
    pdf_reader = PyPDF2.PdfReader(open(file, 'rb'))
    speaker = pyttsx3.init()
    clean_text = "\""

    for page_num in enumerate(
            pdf_reader.pages
    ):  # it will too many request, or maybe too many words.
        text = pdf_reader.pages[page_num[0]].extract_text()
        clean_text += text.strip().replace('\n', ' ') + "\""
        with open(f"{output}-{page_num[0]}.txt", "w") as f:
            f.writelines(clean_text)
        print(clean_text)
        # speaker.say(clean_text)
        # speaker.runAndWait()
        speaker.save_to_file(clean_text, f"{output}-{page_num[0]}.wav")

        # subprocess.run(
        #     ['espeak-ng', clean_text, '-w', f"{output}-{page_num[0]}.wav"])
        # audio = gTTS(text=clean_text, lang="en", slow=False)
        # audio.save(f"{output}-{page_num[0]}.mp3")


def check_enviroment():
    """
    Check the enviroment of system
    """
    OS = os.sys.platform
    if OS == 'Linux':
        return 1
    elif OS == 'Win32':
        return 0
    else:
        return -1


def check_media_player(os):
    """Chioce the media player

    Args:
        os (bool): OS Enviroment

    Returns:
        String: The media player name
    """
    if os:
        return "sox"
    else:
        return "windowsmediaplayer"


if __name__ == "__main__":
    # Check system enviroment, Linux or Windows (The player depending)
    os = check_enviroment()
    media_player = check_media_player(os)
    file_name = input("Please input the pdf file name : ")
    output_file = input("Please input the file name of the output : ")
    translate(file_name, output_file)
    # app = QApplication(sys.argv)
    # form = Form()
    # form.show()

    # sys.exit(app.exec())