# 🩺 Healthcare AI Chatbot

## 🎯 Aim

The Healthcare AI Chatbot is designed to provide users with a conversational interface for accessing healthcare information and advice. It aims to offer a user-friendly platform where individuals can ask health-related questions and receive informative responses powered by AI technology. The chatbot is not intended to replace professional medical advice but rather to serve as an initial point of reference for general health inquiries.

## 🚀 Features

- 💬 Interactive chat interface for health-related queries
- 🤖 AI-powered responses using advanced language models
- 📚 Multiple chat sessions for organizing different health topics
- 🔍 Preset prompts for quick access to common health questions
- 🌓 Dark mode toggle for comfortable viewing in any lighting
- 📱 Responsive design for seamless use on desktop and mobile devices
- 🔒 Server-side session management for data persistence
- 🏷️ Automatic chat titling based on conversation content
- ⚡ Real-time thinking animation for improved user experience

## 🛠️ Technologies Used

- **Backend:**
  - 🐍 Python 3.9+
  - 🌶️ Flask: Web framework for the backend API
  - 🧠 OpenAI API: For generating AI responses
  - 🍪 Flask-Session: For server-side session management

- **Frontend:**
  - 🌐 HTML5
  - 🎨 CSS3
  - 💻 JavaScript (ES6+)
  - 🅱️ Bootstrap 5: For responsive design and UI components

- **Containerization:**
  - 🐳 Docker: For creating a consistent and portable runtime environment

## 🔄 Application Flow

1. **User Interface:**
   - Users interact with a web-based chat interface.
   - The interface includes a sidebar for managing multiple conversations and a main chat area.

2. **Chat Initiation:**
   - Users can start a new chat or select an existing one from the sidebar.
   - Each chat is assigned a unique identifier and title.

3. **Message Exchange:**
   - Users type messages or select preset prompts to communicate with the AI.
   - Messages are sent to the backend server via API calls.

4. **AI Processing:**
   - The backend receives the user's message and the current chat context.
   - It then sends this information to the OpenAI API for processing.
   - The AI generates a response based on the input and context.

5. **Response Display:**
   - The AI's response is sent back to the frontend and displayed in the chat interface.
   - The conversation history is updated and stored server-side.

6. **Session Management:**
   - User sessions are managed server-side, allowing for persistence of chat histories across page reloads.

7. **Multiple Chats:**
   - Users can switch between different chat sessions, with each maintaining its own context and history.

## 🛠️ Setup and Running the Application

### Prerequisites

- 🐍 Python 3.9 or higher
- 📦 pip (Python package manager)
- 🐳 Docker (for containerized deployment)

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/Dwij1704/Healthcare-AI-Chatbot.git
   cd healthcare-ai-chatbot
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. Run the Flask application:
   ```
   flask run
   ```

6. Open a web browser and navigate to `http://localhost:5000`

### 🐳 Docker Setup

1. Build the Docker image:
   ```
   docker build -t healthcare-ai-chatbot .
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:5000 -e OPENAI_API_KEY=your_openai_api_key_here 
   healthcare-ai-chatbot
   ```

3. Open a web browser and navigate to `http://localhost:5000`

## 🖥️ Usage

1. Upon opening the application, you'll see the chat interface with a sidebar for managing chats.
2. Click "New Chat" to start a new conversation or select an existing chat from the sidebar.
3. Type your health-related questions in the input field at the bottom of the chat area.
4. You can also use the preset prompts for quick access to common topics.
5. The AI will process your question and provide a response, which will appear in the chat area.
6. You can switch between different chats using the sidebar, allowing you to manage multiple health-related conversations.

🚨 Remember, while this chatbot can provide general health information, it should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.
