As of 8-2-23 There is a new form of this script with no need to use AWS Polly as I found a work around using a free alteritive
that idolizes Microsoft TTS Voices. [IN this verison of the script you will no longer need to use AWS Polly for
the TTS voice AKA MEANS YOU GET TO SKIP THE WHOLE CREATE AWS POLLY PART OF TUTORIAL
which is great for us broke boy's with a broke boy wallet] :) 

[Up above you will find a version of the orginal script but using Microsoft TTS Voices instead of AWS Polly called Julie+FreeTTS
just open that with visual studio code and replace the OpenAPI with your OpenAPI Key then replace where the pictures are located at in the scripts
directory follow Step 6: Open the script "Main.py" in Visual Studio Code and change 3 directories thats have to do with where the .png files 
are located for the script's GUI. .] LOOK AT TUTORIAL VIDEO IF YOU NEED HELP.

[IF YOU DECEIDE TO USE THIS INSTEAD OF THE ORGINAL SETUP BE SURE TO DOWNLOAD THE UNITED KINGDOM TTS VOICES IN WINDOWS SETTINGS THEN SET TTS VOICE TO HAZEL.]

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


