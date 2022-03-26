import pyttsx3
from gtts import gTTS 
import os
engine = pyttsx3.init()    

#use for to list your system voices than copy the ID
for voice in engine.getProperty('voices'):
     print("Voice:")
     print(" - ID: %s" % voice.id)
     print(" - Name: %s" % voice.name)

#paste voice ID here HKEY.... Tolga is male in Turkish
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga')
engine.setProperty('rate',120)

#save path for files
yol="G:\\UniServerZ\\www\\konusturan.com\\sohbet_sesler\\"

#conversation array
s = ["Merhaba, ben Murat.","Merhaba murat, benim adım Ayşe.","Merhaba Ayşe, memnun oldum.","Bende memnun oldum.","Görüşmek üzere."]

for i in range(len(s)):    
    print(s[i])
    if(i % 2 == 0):
        #this is male voice (tolga) we selected before
        engine.save_to_file(s[i], yol+str(i)+".mp3")
        engine.runAndWait()        
    else:
        #gTTS use female in TR language
        tts = gTTS(text=s[i], lang='tr')
        tts.save(yol+str(i)+".mp3")
    #os.system(yol+str(i)+".mp3") #if you want to play with media player open this command
