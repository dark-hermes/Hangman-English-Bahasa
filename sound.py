import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def set_language(lang):
    global engine

    if lang=="1":
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM')
    elif lang=="2":
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_idID_Andika')

def sayit(phrase):
    global engine
    engine.say(phrase)
    engine.runAndWait()