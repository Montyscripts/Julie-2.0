As of 8-2-23 There is a new form of this script with no need to use AWS Polly as I found a work around using a free alteritive
that idolizes Microsoft TTS Voices.  

[Down Below you will find a version of the orginal script but using Microsoft TTS Voices instead of AWS Polly.]

[IF YOU DECEIDE TO USE THIS INSTEAD OF THE ORGINAL SETUP BE SURE TO DOWNLOAD THE UNITED KINGDOM TTS VOICES IN WINDOWS SETTINGS THEN SET TTS VOICE TO HAZEL.]

import tkinter as tk
from tkinter import scrolledtext
import os
import subprocess
import tempfile
import pyautogui
import pygame
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import openai
import threading
from PIL import Image, ImageTk
from gtts import gTTS

# Initialize the conversation history list
conversation_history = []

# Create the Tkinter window
window = tk.Tk()
window.title("Julie 2.0 - Created by Monty")
window.geometry("575x410")

# Load the image
image_path = "\\image.png"  # Replace with the path to your image file
image = Image.open(image_path)

# Resize the image to fit the window size 
image = image.resize((650, 450), Image.LANCZOS)

# Convert the image to Tkinter-compatible format
background_image = ImageTk.PhotoImage(image)

# Create a label to hold the image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Make the label appear as the background
background_label.image = background_image

# Load the image
image_path = "\\image.png"  # Replace with the path to your image file
image = Image.open(image_path)

# Convert the image to Tkinter-compatible format
background_image = ImageTk.PhotoImage(image)

# Create a label to hold the image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load the PNG image
image_path2 = "\\picture2.png"  # Replace with the path to your image file
image2 = Image.open(image_path2)

# Convert the image to Tkinter-compatible format
image_tk2 = ImageTk.PhotoImage(image2)

# Create a label to display the image
image_label = tk.Label(window, image=image_tk2, bg="black")
image_label.pack(pady=10)

# Initialize the conversation history list
conversation_history = []

# Create a text-to-speech engine
engine = pyttsx3.init()

# Create a variable to track whether voice interaction is enabled or not
voice_interaction_enabled = True

# Modify the speak_text function to allow enabling/disabling voice output
def speak_text(text, rate=200, volume=1.0, pitch=160, desired_voice_id=None):
    global voice_interaction_enabled
    if not voice_interaction_enabled:
        return

    # Find the desired voice if provided
    if desired_voice_id:
        voice_found = False
        for voice in engine.getProperty('voices'):
            if desired_voice_id.lower() in voice.id.lower():
                engine.setProperty('voice', voice.id)
                voice_found = True
                break

        if not voice_found:
            print("Desired voice ID not found. Using the default voice.")
    else:
        # Find a female voice among the available voices
        female_voice_id = None
        for voice in engine.getProperty('voices'):
            if "female" in voice.name.lower():
                female_voice_id = voice.id
                break

        if female_voice_id:
            engine.setProperty('voice', female_voice_id)
        else:
            print("No female voice found. Using the default voice.")

    engine.say(text)
    engine.runAndWait()

# Call the speak_text function with the desired voice ID
speak_text("Good evening, how may I be of service?", desired_voice_id="TTS_MS_EN-GB_HAZEL_11.0")

openai.api_key ="openai.api_key"

# Create a scrolled text box with purple background
text_box = scrolledtext.ScrolledText(window, width=60, height=10, font=("Helvetica", 10), bg="black", fg="purple")
text_box.pack(pady=(0, 10))

# Create an input frame
input_frame = tk.Frame(window, bg="black")
input_frame.pack(pady=(0, 10))

# Create an input label and an input box
input_label = tk.Label(input_frame, text="User Input:", bg="black", font=("Helvetica", 12), fg="purple")
input_label.pack(side=tk.LEFT, padx=(0, 10))
input_box = tk.Entry(input_frame, width=33, font=("Helvetica", 12))
input_box.pack(side=tk.LEFT)

# Initialize Pygame mixer
pygame.mixer.init()

def youtube_search(query):
    webbrowser.open("https://www.youtube.com/results?search_query=" + query.replace(" ", "+"))

def perform_search(query):
    webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))

def handle_error(message):
    print("Error:", message)
    # Perform any necessary error handling operations

# Declare the stop_listening_button_pressed variable globally
stop_listening_button_pressed = False

def start_voice_interaction():
    def voice_interaction():
        global stop_listening_button_pressed
        global conversation_history
        stop_listening_button_pressed = False  # Reset the stop button flag
        conversation_history = []  # Reset conversation history
        text_box.delete('1.0', tk.END)  # Clear the text box
        r = sr.Recognizer()

        # Display "Listening..." prompt
        conversation_history.append("Assistant: Listening...")
        text_box.insert(tk.END, "Assistant: Listening...\n")
        while not stop_listening_button_pressed:
            with sr.Microphone() as source:
                print("Speak something...")
                audio = r.listen(source, phrase_time_limit=7)
            try:
                print("Recognizing...")
                user_input = r.recognize_google(audio)
                input_box.delete(0, tk.END)
                input_box.insert(tk.END, user_input)
                button_click()
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error occurred while using Google Speech Recognition service: {0}".format(e))

    threading.Thread(target=voice_interaction).start()

# Play the specified audio file
def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

def stop_voice_interaction():
    global stop_listening_button_pressed
    stop_listening_button_pressed = True
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    # Reset conversation history and clear the text box
    conversation_history = []
    text_box.delete('1.0', tk.END)

def open_bingai_website():
    webbrowser.open("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
    time.sleep(5)
    pyautogui.click(1254, 956)

def open_tiktok():
    webbrowser.open("https://www.tiktok.com/en/")

def open_instagram():
    webbrowser.open("https://www.instagram.com/")

def open_twitch():
    webbrowser.open("https://www.twitch.tv/") 

def open_facebook():
    webbrowser.open("https://www.facebook.com/")  

# Generate response using OpenAI ChatGPT 3.5 Turbo
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,  # Set max_tokens to a high number to allow for longer responses
            temperature=0.8,
        )
        return response['choices'][0]['text'].strip()
    except openai.OpenAIError as e:
        handle_error("OpenAI API request failed: {0}".format(e))

def button_click(event=None):
    global conversation_history  # Move the global statement here
    user_input = input_box.get().strip()
    input_box.delete(0, tk.END)

    if user_input.lower() == "main menu":
        # Reset conversation history and clear the text box
        conversation_history = []
        text_box.delete('1.0', tk.END)
        return
    if user_input.lower() == "open tiktok":
        open_tiktok()
    if user_input.lower() == "open instagram":
        open_instagram()
    elif user_input.lower() == "open twitch":
        open_twitch()
    elif user_input.lower() == "open facebook":
        open_facebook()
    elif user_input.lower() == "main menu":
        # Reset conversation history and clear the text box
        conversation_history = []
        text_box.delete('1.0', tk.END)
        return
    conversation_history.append("User: " + user_input)
    text_box.insert(tk.END, "User: " + user_input + "\n")

    if "youtube search" in user_input.lower():
        query = user_input.lower().replace("youtube search", "").strip()
        youtube_search(query)
    elif "search" in user_input.lower():
        query = user_input.lower().replace("search", "").strip()
        perform_search(query)
    elif "tell me a joke" in user_input.lower():
        response = generate_response(user_input)
        conversation_history.append("Assistant: " + response)
        text_box.insert(tk.END, "Assistant: " + response + "\n")
        speak_text(response)
    else:
        response = generate_response(user_input)
        conversation_history.append("Assistant: " + response)
        text_box.insert(tk.END, "Assistant: " + response + "\n")
        speak_text(response, rate=200)  # Adjust the rate (words per minute) for better clarity and speed

def toggle_buttons():
    if buttons_frame.winfo_ismapped():
        buttons_frame.pack_forget()
    else:
        buttons_frame.pack(side=tk.TOP, padx=5, pady=5)

# Create a frame to hold the buttons
buttons_frame = tk.Frame(window, bg="black")

# Create a start button for voice interaction
start_button = tk.Button(buttons_frame, text="Start Voice Interaction", command=start_voice_interaction, font=("Helvetica", 12), bg="black", fg="purple", width=20)
start_button.pack(pady=5)

# Create a stop button for voice interaction
stop_button = tk.Button(buttons_frame, text="Stop Voice Interaction", command=stop_voice_interaction, font=("Helvetica", 12), bg="black", fg="purple", width=20)
stop_button.pack(pady=5)

# Calculate the width of the BingAI button based on the length of the text
bingai_button_text = "BingAI"
bingai_button_width = len(bingai_button_text) + 50  # Add some extra padding
# Create a "BingAI" button
bingai_button = tk.Button(buttons_frame, text=bingai_button_text, command=open_bingai_website, font=("Helvetica", 12), bg="black", fg="purple", width=20)
bingai_button.pack(pady=5)

# Add buttons to the buttons frame
buttons_frame_buttons = [
    start_button,
    stop_button,
    bingai_button,
    # Add more buttons here as needed
]

for button in buttons_frame_buttons:
    button.pack(side=tk.LEFT, padx=5)

# Create the tab button
tab_button = tk.Button(window, text="Show/Hide", command=toggle_buttons, font=("Helvetica", 12), bg="black", fg="purple")
tab_button.pack(anchor=tk.N, pady=5)

# Bind the <Return> key to the button_click function
input_box.bind("<Return>", button_click)

# Add the functionality to stop and start voice interaction
def stop_voice_interaction():
    global stop_listening_button_pressed
    global voice_interaction_enabled
    stop_listening_button_pressed = True
    voice_interaction_enabled = False
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    # Reset conversation history and clear the text box
    conversation_history = []
    text_box.delete('1.0', tk.END)

def start_voice_interaction():
    global voice_interaction_enabled
    voice_interaction_enabled = True

# Start the Tkinter event loop
window.mainloop()

[IN this verison of the script you will no longer need to use AWS Polly for
the TTS voice AKA MEANS YOU GET TO SKIP THE WHOLE CREATE AWS POLLY PART OF TUTORIAL
which is great for us broke boy's with a broke boy wallet] :)

Step 1: Create a OpenAPI Account To create Free API (Copy API KEY AFTER CREATING ACCOUNT/ SAVE FOR LATER)- https://auth0.openai.com/u/signup/identifier?state=hKFo2SB1aXdkdC1aV1ltSzNtMzV1ejF6ai1NNWpMX2dXdDR0V6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEFnU2tZOHMzbmlYdkhQeXpIN1JsVEM2ZmlTRVFRTTM5o2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q

Step 2: Create a AWS Polly Key using AWS Amazon (Copy AWS Polly KEY AFTER CREATING ACCOUNT/ SAVE FOR LATER)- https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email

Step 3: Install Visual Studio Code - https://code.visualstudio.com/

Step 4: Install Python - https://www.python.org/

Step 5: Install all dependencies needed for the script via "Install.bat" 

	List of dependencies and modules you will need to run this script | 

Run "CMD" as admin then type the pip install commands one by one, if the "install.bat" file did not work for you.

        pip install tkinter
        pip install pillow
        pip install boto3
        pip install pyautogui
        pip install pygame
        pip install pyttsx3
        pip install SpeechRecognition
        pip install openai
	pip install pyaudio

        
Be sure to set your default web-browser as Microsoft Edge.

Step 6: Open the script "Main.py" in Visual Studio Code and change 3 directories thats have to do with where the .png files are located for the script's GUI. 

                     

		   LIST OF DIRECTORIES THAT NEED CHANGED

   (Replace the image.png and picture2.png with the correct windows directory)    

	      BELOW IS THE 3 LINES OF SCRIPT NEEDED TO BE CHANGED 				    
						           

	1: { # Load the image
          image_path = "image.png"  # Replace with the path to your image file
          image = Image.open(image_path) }

	
	2: { # Load the image
          image_path = "image.png"  # Replace with the path to your image file
          image = Image.open(image_path) }


        3: { # Load the PNG image
          image_path2 = "picture2.png"  # Replace with the path to your image file
          image2 = Image.open(image_path2) }


	   FOR EXAMPLE IF SCRIPT IS LOCATED ON DESKTOP AND .PNG FILES

	   ARE LOCATED INSIDE THE SCRIPT'S FOLDER ON THE DESKTOP COPY 
							
	   THE DIRECTORY FROM WHERE THE .PNG FILES ARE LOCATED SUCH AS
							
	   "C:\\Users\\Monty's PC\\Desktop\\GitHub Julie2.0 Folder\\image.png"
	
	   BE SURE TO USE DOUBLE "\\" WHEN PASTING THE DIRECTORY INTO THE SCRIPT'S CODE. 

	   SO FOR EXAMPLE USING THE 1ST ONE : 	
	  
	  # Load the image
          image_path = "C:\\Users\\Monty's PC\\Desktop\\GitHub Julie2.0 Folder\\image.png"
          image = Image.open(image_path)


Step 7: Change the OpenAPI KEY to your OpenAPI KEY.

        THAT PART OF THE SCRIPT LOOKS LIKE THIS 

        openai.api_key ="Open_API_KEY"

Step 8: Change the AWS Polly KEY'S to your AWS Polly KEY'S.
	
	THAT PART OF THE SCRIPT LOOKS LIKE THIS

	# Set AWS credentials in environment variables
        os.environ["AWS_ACCESS_KEY_ID"] = "AWS_ACCESS_KEY_ID"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS_SECRET_ACCESS_KEY"
        os.environ["AWS_REGION"] = "AWS_REGION"

Step 9: Save The "Main.py" in Viusal Stuido Code to your Scripts Main folder. 

Step 10: Right click the "Main.py" Inside the scripts main folder and open with "Python". 

Step 11: If done correctly you should see my script and should be able to use it as intended. 

Step 12: If you like the script and find it useful please do not forget to buy me a beer :) 
	
	 by donating to my github page.
Step 13: DO NOT FORGET TO SYNC YOUR WINDOWS SYSTEM CLOCK BY GOING TO WINDOWS+SEARCH AND TYPE THE WORD "TIME" 
         
         THEN CLICK ON "CHANGE TIME AND DATE" THEN CLICK ON "SYNC" AND YOUR ALL SET 

SMALL SIDE NOTE : IF YOUR RUNNING INTO ANY ERRORS CHANGE THE 
         image = image.resize((650, 450), Image.ANTIALIAS) to 
         image = image.resize((650, 450), Image.LANCZOS) or vice versa.


SIDE NOTE: IF YOUR NOT USING A 1920x1080 DISPLAY PLEASE CHANGE THE X AND Y VAULES "(1128, 972)" 
	   
	   IN THIS PART OF THE SCRIPT TO MATCH YOUR DISPLAY'S RESOLUTION WHERE THE BINGAI MICROPHONE

	   IS LOCATED ON THE BINGAI WEBPAGE. THE X AND Y VAULES CAN BE FOUND USING THE WINDOWS APPLICATION 

	   PROVIDED IN THE SCRIPT'S MAIN FOLDER CALLED "MPos.exe".
	
	   ALSO DEPENDING ON YOUR INTERNET CONNECTION YOU MAY NEED TO CHANGE THE "time.sleep(10)" TO SOMETHING

	   LIKE "time.sleep(20)" IF YOUR INTERNET IS SLOW. NOW IF YOUR INTERNET IS FAST CHNAGE IT TO SOMETHING 

	   LIKE " time.sleep(5) "
		
	   BELOW IS THE LINE OF SCRIPT NEEDED TO BE CHANGED IF DISPLAY IS NOT 1920x1080


           def open_bingai_website():
           webbrowser.open("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
           time.sleep(10)
           pyautogui.click(1128, 972)

	   DON'T FORGET TO SAVE BEFORE RUNNING SCRIPT :)


