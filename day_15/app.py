from flask import Flask, render_template, request, jsonify
import datetime
import random

app = Flask(__name__)

def get_ai_response(message):
    message = message.lower()
    
    if 'hello' in message or 'hi' in message:
        return "Hello! I am Ana, your AI Assistant! How can I help you? 😊"
    
    elif 'how are you' in message:
        return "I am doing great! Ready to help you with anything! 🚀"
    
    elif 'time' in message:
        time = datetime.datetime.now().strftime("%I:%M %p")
        return f"Current time is {time} ⏰"
    
    elif 'date' in message:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {date} 📅"
    
    elif 'name' in message:
        return "My name is Ana! I am an AI Chatbot built with Python and Flask! 🤖"
    
    elif 'joke' in message:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
            "Why did the AI go to school? To improve its learning! 🎓",
            "What do you call a robot that tells the truth? An honest-bot! 🤖"
        ]
        return random.choice(jokes)
    
    elif 'age' in message:
        return "I am just a few days old! Born during this AI Internship! 👶"
    
    elif 'weather' in message:
        return "I cannot check weather yet, but it is always sunny in AI world! ☀️"
    
    elif 'bye' in message or 'goodbye' in message:
        return "Goodbye! Have an amazing day! See you soon! 👋"
    
    elif 'help' in message:
        return "I can help you with: time, date, jokes, my name, and more! Just ask! 💡"
    
    else:
        responses = [
            "Interesting! Tell me more about that! 🤔",
            "I am still learning! Try asking about time, date or jokes! 😊",
            "Great question! I am an AI and I am always improving! 🚀",
        ]
        return random.choice(responses)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    response = get_ai_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)