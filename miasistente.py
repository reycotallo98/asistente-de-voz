import re
import webbrowser
import pywhatkit
import speech_recognition as sr  # le ponemos un apodo
import pyttsx3
import yfinance as yf
import pyjokes
import datetime
import wikipedia


# escuchar microfono y devolver audio como texto

def transfAudio():
    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configuramos el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar de grabacion
        print('ya puedes hablar')

        # Guardar lo escuchado
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-es")

            # prueba de que pudo ingresar
            print("Dijiste " + pedido)

            # devolver pedido
            return pedido
        # En caso de no comprender
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Ups, no entendí")

            # devolver error
            return "sigo esperando"
        # En caso de no procesar bien
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("Ups, no hay servicio")

            # devolver error
            return "sigo esperando"
        # error inesperado
        except:
            # prueba de que no comprendio el audio
            print("Ups, algo salio mal")

            # devolver error
            return "sigo esperando, "


def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar dia d ela semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()

    dia_semana = dia.weekday()
    # diccionario con dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}
    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Informar hora
def pedir_hora():
    # crea una variable con datos de la hora
    hora = datetime.datetime.now()

    # Decir la hora
    if hora.hour < 13:
        hablar(f'Son las {hora.hour} y {hora.minute} minutos')
    else:
        hablar(f'Son las {hora.hour - 12} y {hora.minute} minutos')


# funcion saludo_inicial
def saludo_inicial():
    # decir saludo

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        hablar('Buenas noches, me llamo Lola soy tu asistente virtual. Si necesitas mi ayuda di hey lola')
    elif hora.hour > 6 or hora.hour < 13:
        hablar('Buenos dias, me llamo Lola soy tu asistente virtual. Si necesitas mi ayuda di hey lola')
    else:
        hablar('Buenas tardes, me llamo Lola soy tu asistente virtual. Si necesitas mi ayuda di hey lola')


def pedir_cosas():
    # activamos el saludo
    saludo_inicial()
    while True:
        pedido = transfAudio().lower()
        if 'hey lola' in pedido:
            # variable de corte
            comenzar = True
            while comenzar:

                # activamos el micro y guardamos el pedido en un string
                pedido = transfAudio().lower()

                if 'youtube' in pedido:
                    hablar('enseguida')
                    webbrowser.open(
                        'https://www.youtube.com/results?search_query=' + pedido[pedido.find('youtube') + 7::1])
                elif 'google' in pedido:
                    hablar('allá voy')
                    webbrowser.open(
                        f'https://www.google.com/search?q={pedido[pedido.find("google") + 6::1].replace(" ", "+")}')
                elif 'dia' in pedido:
                    pedir_dia()
                    continue
                elif 'hora' in pedido:
                    pedir_hora()
                elif 'Wikipedia' in pedido:
                    hablar('Voy a revisar la wiki')
                    pedido = pedido[pedido.find("wikipedia") + 9::1]
                    wikipedia.set_lang('es')
                    resultado = wikipedia.summary(pedido, sentences=1)
                    hablar('He encontrado esto.')
                    hablar(resultado)
                    continue
                elif 'reproduc' in pedido:
                    hablar('Vamos a darle caña')
                    pywhatkit.playonyt(pedido[pedido.find("reproduc") + 10::1])
                elif 'chiste' in pedido:
                    hablar(pyjokes.get_joke('es'))
                    continue
                elif 'precio de' in pedido:
                    accion = pedido[pedido.find("precio de ") + 10::1].replace(" ", "+")
                    try:
                        accion = yf.Ticker(accion)
                        precio_actual = accion.info['regularMarketPrice']
                        hablar(precio_actual)
                    except:
                        hablar('No lo encontre')

                elif 'transcribe' in pedido:
                    hola = True
                    while hola:
                        pywhatkit.text_to_handwriting(transfAudio(),'saludo.png')
                elif 'callate' in pedido:
                    hablar('XAO')
                    comenzar = False


if __name__ == '__main__':
    pedir_cosas()
