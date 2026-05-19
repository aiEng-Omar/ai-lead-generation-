import streamlit as st
import requests
import pandas as pd
import time

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Lead Generation Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1e293b);
}

h1, h2, h3, h4 {
    color: white !important;
}

.stTextInput input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    border: 1px solid #334155;
}

.stNumberInput input {
    background-color: #1e293b;
    color: white;
}

.stButton button {
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
    width: 100%;
}

.stButton button:hover {
    background: linear-gradient(90deg, #06b6d4, #7c3aed);
    transform: scale(1.02);
}

.metric-card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
    text-align: center;
}

.lead-card {
    background: #111827;
    padding: 20px;
    border-radius: 18px;
    border-left: 5px solid #06b6d4;
    margin-bottom: 20px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

.score-high {
    color: #22c55e;
    font-weight: bold;
}

.score-medium {
    color: #facc15;
    font-weight: bold;
}

.score-low {
    color: #ef4444;
    font-weight: bold;
}

hr {
    border: 1px solid #1e293b;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown("""
# 🚀 AI Lead Generation Platform

### Find leads, analyze businesses, generate AI outreach, and export everything automatically.
""")

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("⚙️ Control Panel")

backend_url = st.sidebar.text_input(
    "Backend API",
    value="http://127.0.0.1:8000"
)

st.sidebar.markdown("---")

niche = st.sidebar.text_input(
    "Business Niche",
    placeholder="Dentists"
)

location = st.sidebar.text_input(
    "Location",
    placeholder="Dubai"
)

num_leads = st.sidebar.slider(
    "Number of Leads",
    1,
    20,
    5
)

generate = st.sidebar.button("🚀 Generate Leads")

st.sidebar.markdown("---")

st.sidebar.info("""
### Features
✅ AI Analysis  
✅ Lead Scoring  
✅ Personalized Emails  
✅ CSV Export  
✅ Business Scraping  
""")

# =========================================
# TOP METRICS
# =========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>🤖 AI Powered</h3>
        <p>GPT Business Analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>📧 Outreach</h3>
        <p>Cold Email Generation</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>⭐ Scoring</h3>
        <p>Lead Qualification</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>📁 Export</h3>
        <p>CSV Downloads</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# GENERATE LEADS
# =========================================

if generate:

    if not niche or not location:
        st.warning("Please fill all fields.")

    else:

        payload = {
            "niche": niche,
            "location": location,
            "num_leads": num_leads
        }

        progress = st.progress(0)

        with st.spinner("AI is generating leads..."):

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            try:

                response = requests.post(
                    f"{backend_url}/generate-leads",
                    json=payload
                )

                if response.status_code == 200:

                    data = response.json()
                    results = data["results"]

                    st.success(f"✅ Generated {len(results)} leads successfully!")

                    # =========================================
                    # STATS
                    # =========================================

                    total = len(results)

                    high_scores = 0

                    for lead in results:
                        try:
                            if int(lead["score"]) >= 8:
                                high_scores += 1
                        except:
                            pass

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric("Total Leads", total)

                    with col2:
                        st.metric("High Quality Leads", high_scores)

                    with col3:
                        st.metric("AI Emails Generated", total)

                    st.markdown("---")

                    # =========================================
                    # LEADS DISPLAY
                    # =========================================

                    for idx, lead in enumerate(results, start=1):

                        score = str(lead["score"])

                        score_class = "score-medium"

                        try:
                            numeric_score = int(score)

                            if numeric_score >= 8:
                                score_class = "score-high"

                            elif numeric_score <= 4:
                                score_class = "score-low"

                        except:
                            pass

                        st.markdown(f"""
                        <div class="lead-card">

                        <h2>🏢 {lead['company_name']}</h2>

                        <p><b>🌐 Website:</b> {lead['website']}</p>

                        <p><b>📝 Snippet:</b><br>
                        {lead['snippet']}</p>

                        <p><b>🤖 AI Analysis:</b><br>
                        {lead['analysis']}</p>

                        <p><b>⭐ Lead Score:</b>
                        <span class="{score_class}">
                        {lead['score']}
                        </span></p>

                        <p><b>📧 Personalized Outreach:</b><br>
                        {lead['outreach']}</p>

                        </div>
                        """, unsafe_allow_html=True)

                    # =========================================
                    # EXPORT CSV
                    # =========================================

                    df = pd.DataFrame(results)

                    csv = df.to_csv(index=False).encode("utf-8")

                    st.download_button(
                        label="📁 Download Leads CSV",
                        data=csv,
                        file_name="ai_leads.csv",
                        mime="text/csv"
                    )

                else:
                    st.error(f"Backend Error: {response.text}")

            except Exception as e:
                st.error(f"Connection Error: {e}")