import pyttsx3

synthesizer = pyttsx3.init()
synthesizer.setProperty('voice', "brazil")

my_text = input("Enter the text: ")

synthesizer.save_to_file(my_text, 'texto.mp3')
synthesizer.runAndWait()
synthesizer.stop()
