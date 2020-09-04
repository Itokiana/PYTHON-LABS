import gtts
from playsound import playsound

def read_text(text):
  # make request to google to get synthesis
  tts = gtts.gTTS(text, lang="fr")
  # save the audio file
  tts.save("hello.wav")
  # play the audio file
  playsound("hello.wav")

def choose_response(intent):
  switcher={
    "greeting":'Bonjour Boss',
    "command":"Qu'est-ce que peux faire pour vous?"
  }
  return switcher.get(intent,"Désolée, je ne peux pas faire")
