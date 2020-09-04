
# NOTE: this example requires PyAudio because it uses the Microphone
import speech_recognition as sr
import requests

# obtain audio from the microphone 
r = sr.Recognizer() 
with sr.Microphone() as source:
  print("Please wait. Calibrating microphone...")
  # listen for 5 seconds and create the ambient noise energy level        
  r.adjust_for_ambient_noise(source, duration=2)
  while (1):
    print("Say something!")
    audio = r.listen(source)

    try:
      # print("Google thinks you said :" + r.recognize_google(audio, language = "fr-FR"))
      
      payload = {'question': r.recognize_google(audio, language = "fr-FR") }
      r = requests.post("http://localhost:5000", params=payload)
    except sr.UnknownValueError:
      print("Google could not understand audio")
    except sr.RequestError as e:
      print("Google error; {0}".format(e))