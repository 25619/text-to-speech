import pyttsx3
engine = pyttsx3.init()
preset = []

while True:
  engine.say(input("type statement here: "))
  engine.runAndWait()

