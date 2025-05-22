from flask import Flask, render_template, request, jsonify
import os
from phi.agent import Agent
from phi.model.groq import Groq
from googleapiclient.discovery import build

# Set environment vars
os.environ["GROQ_API_KEY"] = "your api key"
os.environ["GOOGLE_API_KEY"] = "your api key"
os.environ["SEARCH_ENGINE_ID"] = "search engine id"

google_api_key = os.environ["GOOGLE_API_KEY"]
search_engine_id = os.environ["SEARCH_ENGINE_ID"]

# Google search tool
def google_search(query):
    try:
        service = build("customsearch", "v1", developerKey=google_api_key)
        result = service.cse().list(q=query, cx=search_engine_id).execute()
        items = result.get("items", [])
        if not items:
            return "No search results found."

        # Return a markdown-formatted string
        markdown_results = "\n".join(
            [f"- [{item['title']}]({item['link']})" for item in items[:5]]
        )
        return markdown_results
    except Exception as e:
        return f"Google Search Error: {str(e)}"

# AI Agent
travel_agent = Agent(
    name="Travel Planner",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[google_search],
    instructions=[
        "You are a travel planning assistant.",
        "Provide links to hotels and places using Google Search.",
        "Verify info is current."
    ],
    show_tool_calls=True,
    markdown=True
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/generate-plan", methods=["POST"])
def generate_plan():
    try:
        data = request.json
        destination = data.get("destination", "").strip()
        duration = data.get("duration", "").strip()
        budget = data.get("budget", "").strip()
        travel_styles = ", ".join(data.get("travelStyles", []))

        # Basic validation
        if not destination or not duration or not budget:
            raise ValueError("Missing required travel information.")

        prompt = f"""Create a comprehensive travel plan for {destination} for {duration} days.

Travel Preferences:
- Budget Level: {budget}
- Travel Styles: {travel_styles}

Include:
- Best time to visit
- Hotel recommendations (with live links)
- transportation options
- Day-by-day itinerary
- Culinary highlights
- Travel tips
- Estimated cost


Format in Markdown.
"""

        response = travel_agent.run(prompt)
        content = response.content if hasattr(response, 'content') else str(response)
        return jsonify({"plan": content})

    except Exception as e:
        print("Error:", str(e))  # Optional: for debugging
        return jsonify({
            "error": "Something went wrong. Please try again with an accurate destination."
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
