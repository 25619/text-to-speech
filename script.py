import pyttsx3
engine = pyttsx3.init()
preset = {}

def config():
  content = ""
  dicty = ""
  with open("presets.txt", "r") as f:
    content = f.read().split("-----")
    for i in content:
      if i != "<EOF>":
        dicty = i.split("\n")
        preset[dicty[0]] = dicty[1]
        dicty = ""
      else:
        break
counter = 1
setting = input("Play preset? Y/N")
while True:
  if setting == "Y":
    print("Which preset to play?")
    for i in preset:
      print(f"{counter}. {i}")
      counter += 1
    select = preset[input("I wanna play number ")[0]]
    print(select)
    engine.say(select)
    engine.runAndWait()
    input("Press ENTER to end...")
    break
  else:
    engine.say(input("type statement here: "))
    engine.runAndWait()
