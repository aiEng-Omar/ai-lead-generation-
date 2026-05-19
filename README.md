🚀 AI Lead Generation Dashboard

An advanced AI-powered lead generation platform that automatically discovers businesses, scrapes websites, extracts emails, analyzes companies using LLMs, scores leads, and generates personalized cold outreach emails.

Built with FastAPI, Streamlit, OpenRouter, and modern AI automation workflows.

✨ Features
🔍 AI Lead Discovery

Search businesses by:

Niche
Industry
Location

Automatically collect business websites and snippets.

🌐 Website Scraping

Extract website content and business information automatically using web scraping.

📧 Email Extraction

Detect and extract public business emails from websites.

🤖 AI Business Analysis

Uses Large Language Models (LLMs) to:

Analyze businesses
Identify services
Detect pain points
Evaluate lead quality
Generate insights
⭐ AI Lead Scoring

Automatically scores each lead based on:

Website quality
Business potential
AI analysis
Market fit
🚀 Personalized Cold Outreach Generation

Generate AI-powered personalized cold emails tailored for every business lead.

📁 CSV Export

Export generated leads and analyses into CSV format.

🎨 Modern Dashboard UI

Custom Streamlit dashboard featuring:

Glassmorphism UI
Green neon gradients
Interactive lead cards
Dynamic metrics
Responsive layout
Sidebar controls
🛠️ Tech Stack
Backend
FastAPI
Python
Uvicorn
Pydantic
Frontend
Streamlit
Custom CSS
HTML Components
AI / LLM
OpenRouter API
OpenAI SDK
Llama 3.1
Web Scraping
BeautifulSoup4
Requests
Data Processing
CSV
Pandas
📂 Project Structure
leadgen-agent/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── llm_service.py
│   ├── search_service.py
│   ├── scrape_service.py
│   ├── email_service.py
│   ├── scoring_service.py
│   ├── outreach_service.py
│   ├── export_service.py
│   └── storage_service.py
│
├── dashboard/
│   └── app.py
│
├── exports/
│   └── leads.csv
│
├── .env
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone Repository
git clone https://github.com/yourusername/leadgen-agent.git

cd leadgen-agent
2. Create Virtual Environment
Windows
python -m venv .venv

.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv

source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here

Get your API key from:

OpenRouter
▶️ Run Backend API
uvicorn app.main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs
▶️ Run Dashboard

Open another terminal:

streamlit run dashboard/app.py

Dashboard URL:

http://localhost:8501
📡 API Example
POST /generate-leads
Request
{
  "niche": "gyms",
  "location": "Dubai",
  "num_leads": 5
}
Response
{
  "results": [
    {
      "company_name": "Example Gym",
      "website": "https://example.com",
      "emails": ["info@example.com"],
      "snippet": "Business description...",
      "analysis": "AI business analysis...",
      "score": 8,
      "outreach": "Generated cold email..."
    }
  ]
}
🧠 AI Workflow

The platform automatically:

Searches businesses
Scrapes websites
Extracts emails
Analyzes businesses using AI
Scores lead quality
Generates personalized outreach
Exports results
📸 Dashboard Preview Features
AI lead cards
Dynamic scoring
Email extraction display
AI-generated analysis
Personalized outreach section
Export functionality
Responsive UI
🚀 Future Improvements
Authentication system
Multi-user support
Database integration
CRM integrations
Email automation
Docker deployment
LangChain agents
RAG pipelines
Vector database memory
AI analytics dashboard
💼 Use Cases

Perfect for:

AI Automation Agencies
Freelancers
Marketing Agencies
Sales Teams
Cold Outreach Campaigns
Startup Prospecting
AI SaaS Products
🔥 Portfolio Project

This project demonstrates:

Full-stack AI engineering
LLM integrations
FastAPI backend development
Streamlit dashboard design
AI automation systems
Web scraping
Prompt engineering
AI workflow orchestration

Excellent for:

GitHub portfolio
Upwork portfolio
Freelancer showcases
AI engineering resumes
📜 License

MIT License

👨‍💻 Author

Built using modern AI engineering and automation workflows with FastAPI, Streamlit, and Large Language Models.