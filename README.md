
🌍 AI Travel Planner Agent

An intelligent travel planning application that leverages AI models and real-time data to generate personalized travel itineraries. Built with Flask, integrated with Groq LLaMA for decision-making, and Google Search API for live updates, this system makes trip planning smart, fast, and hassle-free.

✅ Features

✔ AI-Powered Recommendations – Uses Groq LLaMA for smart itinerary generation.
✔ Real-Time Data – Fetches the latest information on hotels, attractions, and more using Google Search API.
✔ Personalized Itineraries – Plans travel based on user preferences like budget, duration, and interests.
✔ Responsive Web App – Built using Flask for backend and modern frontend design for a smooth user experience.

🛠 Tech Stack

Backend: Python (Flask)

AI Model: Groq LLaMA (via Phi Framework)

API Integration: Google Search API for real-time data

Frontend: HTML, CSS, JavaScript (or your chosen framework)

📂 Project Structure
AI-Travel-Planner-Agent/
│
├── app.py              # Flask app entry point
├── templates/          # HTML templates
├── static/             # CSS, JS, Images
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/muzaffarhussain05/AI-Travel-Planner-Agent.git
cd AI-Travel-Planner-Agent

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Add API Keys

Create a .env file in the project root and add your credentials:

GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_search_api_key

5. Run the App
python app.py


Visit http://127.0.0.1:5000/
 in your browser.

🚀 Future Enhancements

✅ Add User Authentication (Sign up/Login)

✅ Implement Trip Cost Estimation

✅ Include Flight & Hotel Booking Links

✅ Deploy on Render/Heroku for public access
