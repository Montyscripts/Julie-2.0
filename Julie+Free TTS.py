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

openai.api_key ="openai.api_key"

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