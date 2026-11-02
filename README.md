# SkillPilot AI

SkillPilot AI is a beginner-friendly learning assistant built with Streamlit and Gemini that helps users explore emerging technologies, practice coding, and build a daily learning routine.

It provides:
- a personalized 90-minute study plan
- AI-powered answers for learning questions
- practical explanations using simple English
- technology guidance across AI, software development, cybersecurity, cloud, and data science

## Features

- Daily learning plan generator
- Ask-your-AI-mentor chat experience
- Beginner-focused explanations
- Real-world examples and practical guidance
- Streamed responses for a smoother interactive experience

## Tech Stack

- Python
- Streamlit
- Google Gemini AI
- python-dotenv

## Project Structure

```text
skill-pilot-ai/
├── app.py
├── requirements.txt
├── .env.example
├── core/
│   └── llm.py
├── prompts/
│   └── agent_prompts.py
└── README.md
```

## How it Works

The app loads a Gemini model through the `core/llm.py` module and uses prompt templates from `prompts/agent_prompts.py` to generate:

- a daily learning plan
- beginner-friendly technology explanations
- practical examples and follow-up guidance

## Setup

1. Clone the repository

```bash
git clone https://github.com/manoharNelakurthi/skill-pilot-ai.git
cd skill-pilot-ai
```

2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure your Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

5. Run the app

```bash
streamlit run app.py
```

## Usage

After starting the app:

- open the app in your browser
- go to the "Daily Learning Plan" tab to generate a study plan
- use the chat interface to ask questions about technology topics
- follow the suggested learning path and practice exercises

## Example Learning Categories

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Generative AI
- Agentic AI
- Software Development
- Cybersecurity
- Cloud Computing
- Data Science
- Robotics
- Emerging Technologies

## Notes

This project is designed for beginners and aims to make complex technology topics easier to understand through simple explanations and hands-on learning.

## License

This project is currently unlicensed unless otherwise specified.
