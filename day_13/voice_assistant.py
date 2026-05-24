import pyttsx3
import datetime
import random
import speech_recognition as sr

# Initialize text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    print(f"🤖 Arjun: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"👤 You said: {text}")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            print("❌ Could not understand, please try again!")
            return ""
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""

def get_response(user_input):
    user_input = user_input.lower()
    
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you?"
    
    elif 'time' in user_input:
        time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {time}"
    
    elif 'date' in user_input:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {date}"
    
    elif 'name' in user_input:
        return "My name is Arjun, your personal AI Assistant!"
    
    elif 'how are you' in user_input:
        return "I am doing great! Ready to help you!"
    
    elif 'joke' in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the AI go to school? To improve its learning!",
            "What do you call a robot that always tells the truth? An honest-bot!"
        ]
        return random.choice(jokes)
    
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I am still learning! Try asking about time, date, or ask for a joke!"

try:
    print("=" * 50)
    print("     🤖 AI VOICE ASSISTANT - ANA - DAY 13")
    print("=" * 50)
    print("1 = Speak to Ana 🎤")
    print("2 = Type to Ana ⌨️")
    print("Type 'bye' to exit")
    print("=" * 50)

    speak("Hello! I am Arjun, your AI Assistant. How can I help you today?")

    while True:
        print("\nChoose: 1 = Speak  |  2 = Type")
        choice = input("Your choice: ").strip()
        
        if choice == "1":
            user_input = listen()
        elif choice == "2":
            user_input = input("👤 You: ")
        else:
            print("Please enter 1 or 2!")
            continue
        
        if not user_input:
            continue
        
        response = get_response(user_input)
        speak(response)
        
        if 'bye' in user_input.lower() or 'exit' in user_input.lower():
            break

    print("\n✅ Arjun Session Complete!")

except Exception as e:
    print(f"❌ Error: {e}")
    input("Press Enter to exit...")