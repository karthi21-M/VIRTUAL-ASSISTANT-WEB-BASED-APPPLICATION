Virtual Assistant
This project is a simple virtual assistant web application built using Flask. It responds to various 
commands such as fetching the current time, rolling a dice, and more. The assistant is named 
"Panda" and can be expanded with additional functionalities.
Project Structure
virtual_assistant/
├── app.py
├── static/
│ └── style.css
└── templates/
 └── index.html
- `app.py`: The main application file containing the Flask server and command handling logic.
- `static/style.css`: The CSS file for styling the web interface.
- `templates/index.html`: The HTML file for the web interface.
Prerequisites
- Python 3.x
- Pip (Python package installer)
Installation
1. Clone the repository or download the project files.
2. Navigate to the project directory:
 cd virtual_assistant
3. Create a virtual environment:
 python -m venv venv
4. Activate the virtual environment:
 On Windows:
➢ .\venv\Scripts\Activate.ps1
 On macOS/Linux:
➢ source venv/bin/activate
5. Install the required packages:
➢ pip install Flask pyttsx3 SpeechRecognition wikipedia requests
Running the Application
1. Ensure the virtual environment is activated.
2. Run the Flask application:
➢ python app.py
3. Open your web browser and navigate to `http://127.0.0.1:5000`.
Usage
1. Enter a command in the input field and press the "Send" button.
2. The virtual assistant will respond to your command. Here are some example commands you can 
try:
 - "What is your name?"
 - "Who created you?"
 - "Roll a dice."
 - "What time is it?"
 - "Search Wikipedia for Python programming."
License
This project is licensed under the MIT License.
Acknowledgements
- Created by Abarna J, Karthikeyan M, Kisanth R.
- Inspired by various online resources and tutorials.
Feel free to contribute to this project by forking the repository and submitting pull requests.
