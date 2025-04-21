import speech_recognition as sr

def voice_to_text():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hablá ahora...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language="es-ES")  # Español
        print("Dijiste:", texto)
        return texto
    except sr.UnknownValueError:
        print("No se entendió el audio")
    except sr.RequestError:
        print("Error al conectarse con el servicio de reconocimiento")
