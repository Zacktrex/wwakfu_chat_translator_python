import os
import time
from textblob import TextBlob

filename = 'C:\\Users\\prowo\\AppData\\Roaming\\zaap\\gamesLogs\\wakfu\\logs\\wakfu_chat.log'  # Replace with the name of your file
inputLangCode ='es'
outputLangCode ="en"
chatSelected = ["Vicinity", "Recruitment", "Group","Guild", "Private"] 

def read_last_line(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            last_line = None
            for line in file:
                last_line = line.strip()
            return last_line
    except FileNotFoundError:
        return None



def monitor_file(filename):
    last_mod_time = os.path.getmtime(filename)
    last_line = None
    l1 = "testing"
    

    while True:
        time.sleep(3)  # Adjust the sleep interval as needed
        new_mod_time = os.path.getmtime(filename)
        
        if new_mod_time != last_mod_time:
            last_mod_time = new_mod_time
            new_last_line = read_last_line(filename)
            
            if new_last_line is not None and new_last_line != last_line:
                last_line = new_last_line
                l1=last_line.split(":",2)[-1].split('-',1)[1]
                l4 = l1.split(':',1)
                b = TextBlob( l4[-1].strip())
                try:
                    for word in chatSelected:
                       if word in l4[-2].strip():
                          print(l4[0],':',b.translate(from_lang=inputLangCode,to=outputLangCode))
                except:
                    print('error ocurr')
   

if __name__ == "__main__":
   monitor_file(filename)