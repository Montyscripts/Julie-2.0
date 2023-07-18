import tkinter as tk
from tkinter import scrolledtext
import os
import subprocess
import tempfile
import boto3
import pyautogui
import pygame
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import openai
import threading
from PIL import Image, ImageTk

# Initialize the conversation history list
conversation_history = []

# Create a text-to-speech engine
engine = pyttsx3.init()

# Handle errors
def handle_error(message):
    print("Error:", message)
    exit()

# Create the Tkinter window
window = tk.Tk()
window.title("Julie 2.0 - Created by Monty")
window.geometry("575x410")

# Load the image
image_path = "image.png"  # Replace with the path to your image file
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
image_path = "image.png"  # Replace with the path to your image file
image = Image.open(image_path)

# Convert the image to Tkinter-compatible format
background_image = ImageTk.PhotoImage(image)

# Create a label to hold the image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load the PNG image
image_path2 = "picture2.png"  # Replace with the path to your image file
image2 = Image.open(image_path2)

# Resize the image if needed
# image2 = image2.resize((width, height), Image.ANTIALIAS)

# Convert the image to Tkinter-compatible format
image_tk2 = ImageTk.PhotoImage(image2)

# Create a label to display the image
image_label = tk.Label(window, image=image_tk2, bg="black")
image_label.pack(pady=10)

# Initialize the conversation history list
conversation_history = []

# Create a text-to-speech engine
engine = pyttsx3.init()

openai.api_key ="Open_API_KEY"

# Set AWS credentials in environment variables
os.environ["AWS_ACCESS_KEY_ID"] = "AWS_ACCESS_KEY_ID"
os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS_SECRET_ACCESS_KEY"
os.environ["AWS_REGION"] = "AWS_REGION"

# Check if any of the credentials are missing
if not (
    os.environ.get("AWS_ACCESS_KEY_ID")
    and os.environ.get("AWS_SECRET_ACCESS_KEY")
    and os.environ.get("AWS_REGION")
):
    print("AWS credentials not found. Please ensure the environment variables are set correctly.")
    exit()

# Create the AWS Polly client
polly = boto3.client('polly', region_name="us-east-1")

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

# Function to convert text to speech using AWS Polly
def aws_polly_tts(text, voice_id):
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice_id
    )
    audio_stream = response["AudioStream"]

    temp_file = tempfile.NamedTemporaryFile(delete=True)
    with open(temp_file.name + ".mp3", "wb") as file:
        file.write(audio_stream.read())

    pygame.mixer.init()
    pygame.mixer.music.load(temp_file.name + ".mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

def speak_text(text):
    # Choose the AWS Polly voice ID (e.g., "Joanna", "Matthew", "Emma", etc.)
    voice_id = "Joanna"
    aws_polly_tts(text, voice_id)

def transcribe_audio_to_text(audio):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 2500  # Adjust the energy threshold according to your audio input
    recognizer.pause_threshold = 0.8  # Adjust the pause threshold according to your audio input

    try:
        # Use the Google Speech Recognition API for speech recognition
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print("Request to Google Speech Recognition API failed: {0}".format(e))
        handle_error("Request to Google Speech Recognition API failed.")

def open_application(application_name):
    try:
        subprocess.Popen(application_name)
        print(f"Opened {application_name} successfully.")
    except Exception as e:
        print(f"Failed to open {application_name}. Error: {e}")

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

def open_bingai_website():
    webbrowser.open("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
    time.sleep(10)
    pyautogui.click(1128, 972)

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

def stop_voice_interaction():
    global stop_listening_button_pressed
    global conversation_history
    stop_listening_button_pressed = True
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    # Reset conversation history and clear the text box
    conversation_history = []
    text_box.delete('1.0', tk.END)

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
        speak_text(response)

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

# Start the Tkinter event loop
window.mainloop()
