import speech_recognition as sr
from datetime import datetime


text_file = "text.txt"
r = sr.Recognizer()

def get_text_from_mic():
    with sr.Microphone(device_index=1, sample_rate=44100, chunk_size=1024) as source:
        audio = r.listen(source)
        text = r.recognize_google(audio, language="ru-RU")
        print(text)
        return text

def write_into_file(file, text):
    with open(file, 'a') as f:
        f.write(str(datetime.now()) + '|')
        f.write(text + '\n')


while True:
    try:
        text = get_text_from_mic()
        write_into_file(text_file, text)
    except sr.UnknownValueError:
        print('dont understand')

    except sr.RequestError as e:
        print(e)
    print('next\n')



