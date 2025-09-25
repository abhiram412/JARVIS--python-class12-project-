import speech_recognition as sr
import pyttsx3
import webbrowser
import newsdataapi
# inatall pocketsphinx
import pocketsphinx
recognise = sr.Recognizer()
engine= pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c): 
     if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
     elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")
     elif "open brave" in c.lower():
         webbrowser.open("https://www.brave.com")  
     elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
     elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
     
if __name__ == "__main__":
      speak("initiallizing Jarvis....")
      while True:
        
# listen for word jarvis
# obtain audio from the microphone
        
        r = sr.Recognizer()
        print ("Recognizing...")

# recognize speech using google  
        try:
          
          with sr.Microphone() as source:
           print("listenting...")
           audio = r.listen(source,timeout=2,phrase_time_limit=1)
 
          command = r.recognize_google(audio)
          if (command.lower() == "jarvis"):
           speak("Yes sir")

        #    listenfor for command 
           with sr.Microphone() as source:
             print("jarvis is active...")
             audio = r.listen(source)
             command = r.recognize_google(audio)

             processcommand(command)


        except Exception as e: 
         print("Error; {0}".format(e))

   
        

 

   
        