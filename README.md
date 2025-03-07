﻿# Voice-Assistant-Using-Speech-Recognition---Python

# J.A.R.V.I.S - Your Personal Voice Assistant

J.A.R.V.I.S is a Python-based voice assistant that leverages speech recognition and text-to-speech synthesis to perform various tasks such as opening applications, conducting Google searches, playing YouTube videos, retrieving the current time, and more.

## Features

- **Voice Interaction:** Uses speech recognition to understand user commands.
- **Application Management:** Open and close popular applications like Chrome, Notepad, Calendar, and more.
- **Web Browsing:** Search Google, open YouTube, Amazon, Flipkart, and other websites.
- **Media Playback:** Play songs or open YouTube channels by voice command.
- **Time Inquiry:** Get the current time instantly.
- **Conversational Abilities:** Responds to basic greetings and interactions.

## Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

Install the required dependencies using:

\`\`\`sh
pip install pyttsx3 speechrecognition wikipedia pywhatkit psutil
\`\`\`

## Usage

### Run the script:
\`\`\`sh
python jarvis.py
\`\`\`

### The assistant will greet you based on the time of day.

### Speak a command, such as:
- **"Open Chrome"** → Opens Google Chrome  
- **"Play [song name]"** → Plays the requested song on YouTube  
- **"Make a Google search on Python programming"** → Performs a Google search  
- **"What is the time?"** → Tells the current time  
- **"Close Notepad"** → Closes Notepad  

### To exit, say:
- **"Goodbye Jarvis"**  
- **"Exit Jarvis"**  

## Commands List

| Command Example                   | Functionality                                  |
|------------------------------------|----------------------------------------------|
| \`open youtube\`                     | Opens YouTube in the browser                  |
| \`open google\`                      | Opens Google in the browser                   |
| \`play [song name]\`                 | Plays a song on YouTube                       |
| \`make a google search on [query]\`  | Searches the given query on Google           |
| \`what is the time\`                 | Announces the current time                    |
| \`open [application name]\`          | Opens the specified application               |
| \`close [application name]\`         | Closes the specified application              |
| \`goodbye jarvis\` / \`exit jarvis\`   | Closes the assistant                          |

## Customization

- You can modify the \`app_mapping\` dictionary to add support for additional applications.
- Adjust the \`voice\` and \`rate\` in \`pyttsx3\` to change the assistant's voice output.
- Enhance features by integrating additional APIs or functionalities.

## License

This project is open-source and available for personal or educational use.

EOL
