from tkinter import *   # Used for making interactive GUI
import pyttsx3          #pip install pyttsx3
import datetime
import speech_recognition as sr     #pip install speechRecognition
import wikipedia         #pip install wikipedia
import webbrowser        # To take information or to operate browser
import os            # To open or search any software in our system
import smtplib     # To send email


#numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
#a = {'name':'your email'}

# This is used for selecting the voice for using in our program 

engine = pyttsx3.init('sapi5')
# SAPI5 (speech application programming interface) is an API developed by microsoft to allow the use of speech recognition.
voices = engine.getProperty('voices')
# To print the name of the voice 
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

window = Tk()  # To create GUI's Window

global var
global var1

var = StringVar()
var1 = StringVar()


# This function is used by the assistant to speak.
# This function gives the voice to my assistant

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



# It is used for sending the email.
'''def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'password') # email id - use any email id whose security/privacy is off
    server.sendmail('email id', to, content)
    server.close()'''

# This function is used to tell the assistant about the time so that he can wish me.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning! Sir") 
        window.update()
        speak("Good Morning! Sir")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon! Sir")
        window.update()
        speak("Good Afternoon! Sir")
    else:
        var.set("Good Evening! Sir")
        window.update()
        speak("Good Evening! Sir")
    speak("I am your Assistant Sir. Please tell me how may I help you") 


# This function take the command by the user to recognise it and work on it.

def takeCommand():
#It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')

	# If the assistant does not recognise the command given by the user then it will run exception.
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query


# Here main program starts by pressing the play butten in the GUI Window.
def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'grey')
    wishme()
    while True:
        btn1.configure(bg = 'grey')
        query = takeCommand().lower()
		# Logic for executing tasks based on query.
		# To quit our program here we use exit function by giving quit, bye or exit command.
        if 'exit' in query or 'quit' in query or 'bye' in query:
            var.set("Quitting Sir. Thanks for your time")
            btn1.configure(bg = 'grey')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Quitting Sir. Thanks for your time")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course error' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
			
        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

		
        # To play music from your internal directeries.
		# I don't have any music file in the system.
        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'D:\My Music\Favourites'       #Enter the correct Path according to your system
            songs = os.listdir(music_dir)
            n = random.randint(0,27) # For suffling the music files.
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Tushar's Assistant Sir")
            window.update()
            speak("myself Tushar's Assistant sir")

        elif 'who creates you' in query:
            var.set('My Creator is Mr. Tushar')
            window.update()
            speak('My Creator is Mr. Tushar')

        elif 'say hello' in query:
            var.set("Hello Everyone! My self Tushar's Assistant")
            window.update()
            speak("Hello Everyone! My self Tushar's Assistant")

        elif 'open vs code' in query:
            var.set("Opening VS code")
            window.update()
            speak("Opening VS code")
            path = "C:\\Users\\This PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'email to me' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a['name']
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')

        elif 'open code block' in query:
            var.set('Opening Codeblocks')
            window.update()
            speak('opening Codeblocks')
            os.startfile("C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe") #Enter the correct Path according to your system

        elif 'how are you' in query:
            var.set('I am fine, Thank you')
            window.update()
            speak("I am fine, Thank you")
            var.set('How are you, Sir')
            window.update()
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            var.set("It's good to know that your fine")
            window.update()
            speak("It's good to know that your fine")

        elif "what's your name" in query or "What is your name" in query:
            var.set("My friends call me Tushar's assistant")
            window.update()
            speak("My friends call me")
            speak("Tushar's assistant")
            #print("My friends call me Tushar's assistant")

        elif "who made you" in query:
#           print("I have been created by Tushar.")
            var.set('I have been created by Tushar.')
            window.update()
            speak("I have been created by Tushar.")


        elif "who are you" in query:
            var.set("I am your virtual assistant created by Tushar")
            window.update()
            speak("I am your virtual assistant created by Tushar")

        elif "open powerpoint" in query:
            var.set("opening powerpoint")
            window.update()
            Path= "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"      #Enter the correct Path according to your system
            os.startfile(Path)
            speak("opening powerpoint")


        elif "open word" in query:
            var.set("Opening Word")
            window.update()
            wPath= "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"      #Enter the correct Path according to your system
            os.startfile(wPath)
            speak("opening Word")














        '''
        elif 'enter student details' in query:
            s = Student()
            var.set('Name of the student')
            window.update()
            speak('Name of the student')
            name = takeCommand()
            var.set('standard in which he/she study')
            window.update()
            speak('standard in which he/she study')
            standard = takeCommand()
            var.set('Role Number')
            window.update()
            speak('Role number')
            rollno = takeCommand()
            s.Enterdetalis(name,standard,rollno)
            var.set('Details are saved')
            window.update()
            speak('Details are saved')
        elif 'show me details' in query:
            var.set('Name: '+name+' Standard: '+ standard+' Roll No.: '+ rollno)
            window.update()

        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg',frame)
            stream.release()

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        
        elif 'read the photo' in query: #If you have Pytesseract installed for Optical Character Recognition
            try:
                im = Image.open('pic.jpg')
                text = pytesseract.image_to_string(im)
                speak(text)
            except Exception as e:
                print("Unable to read the data")
                print(e)
            '''
                

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = 'WHITE')
label2.config(font=("Engravers MT", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Engravers MT", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title("TUSHAR'S ASSIATANT")


label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Engravers MT", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Engravers MT", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Engravers MT", 12))
btn2.pack()


window.mainloop()
