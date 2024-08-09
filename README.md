# Calm Space - Mental Health Chatbot

## Overview
Calm Space is a mental health chatbot designed to provide support and resources for users. The chatbot can respond to user inquiries related to mental health topics using a pre-trained model and can be easily deployed using Flask for the backend and HTML,CSS,JavaScript for the frontend.

![Chatbot](bot1.png)

## Features
User Interaction: Users can send messages to the chatbot and receive responses based on the trained model.
Mental Health Support: The bot is designed to handle various intents related to mental health, including anxiety, depression, self-care, and more.
Real-time Messaging: Messages are displayed in a chat interface, with user and bot messages aligned on the same line for clear conversation flow.

## Installation

Python 3.x
Flask
Keras (for model loading and prediction)
NLTK (for text processing)
Other dependencies listed in requirements.txt

Setup
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/calm-space-chatbot.git
cd calm-space-chatbot
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Prepare the Models and Data

Ensure that you have the following files in your project directory:

model.h5 (your trained Keras model)
intents.json (JSON file containing intents and responses)
texts.pkl (pickled file of words used in the model)
labels.pkl (pickled file of class labels)
Run the Application

bash
Copy code
python app.py
The application will start running on http://127.0.0.1:5000/.

## Usage
Open your web browser and navigate to http://127.0.0.1:5000/.
Type a message into the input field and click "Send."
The chatbot will respond based on the trained model and display responses in the chat interface.

## Code Structure
app.py: Flask backend handling routes and integrating with the chatbot model.
static/js/bot.js: JavaScript file managing chat interactions and user input.
templates/index.html: HTML file providing the chat interface.
requirements.txt: List of Python dependencies for the project.

## Contact
For any questions or feedback, please reach out to nehaannie2002@gmail.com
