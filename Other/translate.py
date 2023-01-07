import speech_recognition as sr
import pyttsx3
import PyPDF2


def SpeakText(text, filename):
    engine = pyttsx3.init(driverName="sapi5", debug=True)
    # engine.say(text)
    engine.say("123")

    # print(f"123 {type(text)}")
    engine.save_to_file(text, f"{filename}.wav")
    print(f"456 {filename}")
    engine.runAndWait()


def PdfReader(filename, output):
    try:
        pdf_reader = PyPDF2.PdfReader(open(filename, 'rb'))
    except:
        print(f"{filename} is not PDF File, please input the PDF File.")
    engine = pyttsx3.init()
    clean_text = ""

    for page_num in enumerate(pdf_reader.pages):
        text = pdf_reader.pages[page_num[0]].extract_text()
        clean_text += text.strip().replace('\n', ' ')

    engine.save_to_file(clean_text, f"{output}.wav")
    engine.runAndWait()


# def WavReader(filename, output):
#     with

if __name__ == "__main__":
    mode = input("Mode 1: record, Mode 2: PDF translate")
    if mode == 1:
        r = sr.Recognizer()
        filename = input("Please input the Filename :")
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print(f"Did you say {MyText} ?")

                SpeakText(str(MyText), filename)
        except sr.RequestError as e:
            print(f"Could not request result; {e}")

        except sr.UnknownValueError:
            print("Unknown error occured !")
    elif mode == 2:
        filename = input("PDF File :")
        output = input("Output File :")
        PdfReader(filename, output)

    else:
        r = sr.Recognizer()
        filename = input("Wav File :")
        with sr.WavFile(filename) as source:
            audio = r.record(source)
            r.adjust_for_ambient_noise(source)
            print(r.recognize_sphinx(audio, language="zh-cn"))
