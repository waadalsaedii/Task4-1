#authenticate
url='https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/a972c7bd-5319-4da3-bd6a-0ada60114308'
apikey='KIJiXiiQd6PcXmQGaGqQdfNvbA1voy876Ok2GpJEkPJK'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
tts=TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


#convert a string
with open('./speech.mp3','wb')as audio_file:
    res=tts.synthesize('hellow world',accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
    
#convert from a file 

with open('c.txt','r')as f:
    text=f.readlines()
    
    text=[line.replace('\n','')for line in text]
    text=''.join(str(line)for line in text)
 
    

