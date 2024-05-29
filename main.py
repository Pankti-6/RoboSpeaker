#importing pyttsx3 for text to speech conversion
import pyttsx3
text_speech = pyttsx3.init() #using init method to initialize package
while True: #putting condition to run program as many times user want to convert text to speech
    answer = input("Please enter your answer: ") #taking input from user that then want to hear from robo
    if answer == "quit": #using quit word to exit the program
        pyttsx3.speak("bye bye friend")
        break
    text_speech.say(answer)
    text_speech.runAndWait()

