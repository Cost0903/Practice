# This script converts a pdf file to an mp3 file.
"""test
"""
import PyPDF2
import pyttsx3

pdf_reader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()
clean_text = None

for page_num in range(pdf_reader.numPages):
    text = pdf_reader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
