from flask import Flask, request, jsonify, session, render_template
from flask_session import Session
from openai import OpenAI
import os
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    chat_id = data.get('chatId')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    if 'chats' not in session:
        session['chats'] = {}

    if chat_id not in session['chats']:
        session['chats'][chat_id] = {
            'title': user_message[:30] + '...' if len(user_message) > 30 else user_message,
            'messages': [
                {"role": "system", "content": "You are a helpful healthcare assistant. Provide accurate and helpful information, but always advise the user to consult with a healthcare professional for medical advice."}
            ]
        }

    # Add the user's message to the conversation history
    session['chats'][chat_id]['messages'].append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session['chats'][chat_id]['messages'],
            max_tokens=150
        )
        
        ai_response = response.choices[0].message.content

        # Add the AI's response to the conversation history
        session['chats'][chat_id]['messages'].append({"role": "assistant", "content": ai_response})

        # Limit the conversation history to the last 10 messages to manage token usage
        if len(session['chats'][chat_id]['messages']) > 11:  # 10 messages + 1 system message
            session['chats'][chat_id]['messages'] = session['chats'][chat_id]['messages'][:1] + session['chats'][chat_id]['messages'][-10:]

        session.modified = True

        return jsonify({"response": ai_response, "chatId": chat_id})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chats', methods=['GET'])
def get_chats():
    chats = session.get('chats', {})
    return jsonify({
        "chats": [
            {"id": chat_id, "title": chat_info['title']}
            for chat_id, chat_info in chats.items()
        ]
    })

@app.route('/chat/<chat_id>', methods=['GET'])
def get_chat(chat_id):
    chats = session.get('chats', {})
    if chat_id in chats:
        return jsonify({"messages": chats[chat_id]['messages'][1:]})  # Exclude system message
    return jsonify({"error": "Chat not found"}), 404

@app.route('/new-chat', methods=['POST'])
def new_chat():
    chat_id = str(uuid4())
    return jsonify({"chatId": chat_id})

@app.route('/reset', methods=['POST'])
def reset_conversation():
    session.pop('chats', None)
    return jsonify({"message": "All conversations reset successfully"})

if __name__ == '__main__':
    app.run(debug=True)