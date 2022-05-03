import pyttsx3 
import speech_recognition as sr 
import webbrowser   
import datetime   
import wikipedia  
  
  
def takeCommand(): 
  
    r = sr.Recognizer() 
  
    
    
    
    with sr.Microphone() as source: 
        print('Listening') 
          
        
        
        r.pause_threshold = 0.7
        audio = r.listen(source) 
          
        
        
        
        
        try: 
            print("Escuchando...") 
              
            
            
            
            Query = r.recognize_google(audio, language='es-es') 
            print("el comando es: ", Query) 
              
        except Exception as e: 
            print(e) 
            print("repitelo por favor") 
            return "None"
          
        return Query 
  
def speak(audio): 
      
    engine = pyttsx3.init() 
    
    
    voices = engine.getProperty('voices') 
      
    
    
    engine.setProperty('voice', voices[0].id) 
      
    
    engine.say(audio)   
      
    
    
    engine.runAndWait() 
  
def tellDay(): 
      
    
    
    day = datetime.datetime.today().weekday() + 1
      
    
    
    Day_dict = {1: 'Lunes', 2: 'Martes',  
                3: 'Miercoles', 4: 'Jueves',  
                5: 'Viernes', 6: 'Sabado', 
                7: 'Domindo'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("hoy es " + day_of_the_week) 
  
  
def tellTime(): 
      
    
    time = str(datetime.datetime.now()) 
      
    
    
    
    print(time) 
    hour = time[11:13] 
    min = time[14:16] 
    speak("son las " + hour + "y" + min + "Minutos")     
  
def Hello(): 
      
    
    
    
    speak("Hola, soy tu asistente virtual, ¿que desea hacer?") 
  
  
def Take_query(): 
  
    
    
    Hello() 
      
    
    
    
    
    while(True): 
          
        
        
        
        
        query = takeCommand().lower() 
        if "abre el marca" in query: 
            speak("viendo las ultimas noticias en el mundo del deporte ") 
              
            
            
            
            webbrowser.open("www.marca.com") 
            continue
          
        elif "abre google" in query: 
            speak("abriendo el buscador ") 
            webbrowser.open("www.google.com") 
            continue
              
        elif "qué día es hoy" in query: 
            tellDay() 
            continue
          
        elif "qué hora es" in query: 
            tellTime() 
            continue
          
        
        elif "adiós" in query: 
            speak("xao") 
            exit() 
          
        elif "busca en wikipedia" in query: 
              
            
            
            speak("comprobando wikipedia ") 
            query = query.replace("wikipedia", "") 
              
            
            
            
            result = wikipedia.summary(query, sentences=4) 
            speak("de acuerdo con wikipedia") 
            speak(result) 
          
        elif "cómo te llamas" in query: 
            speak("Soy manolo, tu asistente virtual") 
  
if __name__ == '__main__': 
      
    
    
    Take_query()