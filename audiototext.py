import speech_recognition as sr

arquivo="audio.wav"

#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
     #Habilita a gravacao para utilizacao no Speech
     r = sr.Recognizer()
     microfone = sr.AudioFile(arquivo)
     #Passa o audio para o reconhecedor de padroes do speech_recognition
     with microfone as source:
      audio = r.record(source)
      try:
        frase = r.recognize_google(audio,language='pt-BR')
      #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
      except sr.UnkownValueError:
        frase='Audio não legível'
     return frase

#retornou o texto do audio enviado
fala=ouvir_microfone()
