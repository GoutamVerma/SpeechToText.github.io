import speech_recognition as sr 


r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speack Now: ")
    audio = r.listen(Source)
    
    
print(r.recognize_google(audio))    
    
