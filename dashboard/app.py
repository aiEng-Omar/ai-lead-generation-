

import streamlit as st
import requests


st.set_page_config(
    page_title="AI Lead Generator",
    page_icon="🚀",
    layout="wide"

)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* MAIN APP */
.stApp {
    background: linear-gradient(135deg, #071b16, #0b2e26, #114d3b);
    color: white;
}

/* HEADER */
.main-header {
    background: radial-gradient(circle,rgba(0, 38, 0, 1) 0%, rgba(0, 23, 3, 1) 100%);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.3);
}

.main-header h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 10px;
}

.main-header p {
    color: white;
    font-size: 18px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #081c15, #0f3d2e);
    border-right: 1px solid rgba(255,255,255,0.1);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.eelgd2m10{
  display: none;

}

/* SIDEBAR TOGGLE BUTTON */
.toggle-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 999999;
    background: linear-gradient(90deg, #00c896, #00e6a7);
    color: white;
    border: none;
    padding: 12px 18px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
    transition: 0.3s;

}

.toggle-btn:hover {
    transform: scale(1.05);
}

/* SIDEBAR ANIMATION */
section[data-testid="stSidebar"] {
    transition: all 0.4s ease;
}


/* INPUTS */
.stTextInput input {
    background-color: rgba(255,255,255,0.08);
    color: white;
    border: 1px solid #00e6a7;
    border-radius: 10px;
}

.stNumberInput input {
    background-color: rgba(255,255,255,0.08);
    color: white;
    border: 1px solid #00e6a7;
    border-radius: 10px;
}

/* BUTTON */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #00c896, #00e6a7);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 15px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;

}

.stButton button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(0,230,167,0.5);
}

/* RESULT CARD */
.result-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 0px 20px rgba(0,0,0,0.2);
}

.metric-card {
    padding: 10px;
    background: radial-gradient(circle,rgba(0, 38, 0, 1) 0%, rgba(0, 23, 3, 1) 100%);
    border-radius: 18px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
    text-align: center;
}


/* TITLES */
.company-title {
    font-size: 28px;
    font-weight: bold;
    color: #00f5b4;
    margin-bottom: 15px;
}

/* SECTION TITLE */
.section-title {
    font-size: 18px;
    font-weight: bold;
    margin-top: 18px;
    margin-bottom: 10px;
    color: #7fffd4;
}

/* TEXT */
.result-text {
    background: rgba(255,255,255,0.03);
    padding: 15px;
    border-radius: 10px;
    line-height: 1.7;
    color: #e8fff7;
    white-space: pre-wrap;
}

/* WEBSITE LINK */
.website-link a {
    color: #00ffd0;
    text-decoration: none;
    font-weight: bold;
}

.website-link a:hover {
    text-decoration: underline;
}

/* EMAIL TAG */
.email-tag {
    display: inline-block;
    background: #1d6e52;
    color: white !important;
    padding: 8px 12px;
    border-radius: 10px;
    margin: 5px;
    font-size: 16px;
    text-decoration: none !important;
}

.email-tag a {
    color: white !important;
    text-decoration: none !important;
}


/* SCORE */
.score-box {
    background: linear-gradient(90deg, #00c896, #00e6a7);
    padding: 15px;
    border-radius: 12px;
    color: white;
    font-weight: bold;
    margin-top: 10px;
}

/* HIDE STREAMLIT HEADER */
header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="main-header">
    <h1>🚀 AI Lead Generation Dashboard</h1>
    <p>Find businesses, analyze leads, extract emails, and generate AI outreach automatically.</p>
</div>
""", unsafe_allow_html=True)

toggle = st.toggle("☰ Show / Hide Sidebar", value=True)

if toggle:
    st.sidebar.title("⚡ Lead Settings")

    niche = st.sidebar.text_input(
        "Business Niche",
        placeholder="e.g. gyms"
    )

    location = st.sidebar.text_input(
        "Location",
        placeholder="e.g. Dubai"
    )

    num_leads = st.sidebar.slider(
        "Number of Leads",
        1,
        20,
        5
    )

    generate_button = st.sidebar.button("🚀 Generate Leads")

else:
    niche = ""
    location = ""
    num_leads = 5
    generate_button = False

# =========================
# SIDEBAR
# =========================

# st.sidebar.title("⚡ Lead Settings")
#
# niche = st.sidebar.text_input(
#     "Business Niche",
#     placeholder="e.g. gyms"
# )
#
# location = st.sidebar.text_input(
#     "Location",
#     placeholder="e.g. Dubai"
# )
#
# num_leads = st.sidebar.slider(
#     "Number of Leads",
#     1,
#     20,
#     5
# )
#
# generate_button = st.sidebar.button("🚀 Generate Leads")
score = "0"
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
    st.markdown(f"""
    <div class="metric-card">
        <h3>⭐{score} </h3>
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

# =========================
# MAIN CONTENT
# =========================

if generate_button:

    if not niche or not location:
        st.error("Please enter niche and location.")
    else:

        with st.spinner("Generating AI leads..."):

            payload = {
                "niche": niche,
                "location": location,
                "num_leads": num_leads
            }

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/generate-leads",
                    json=payload
                )

                if response.status_code != 200:
                    st.error(f"Error {response.status_code}: {response.text}")

                else:

                    data = response.json()

                    results = data.get("results", [])

                    st.success(f"✅ Found {len(results)} leads")

                    for item in results:

                        company_name = item.get("company_name", "N/A")
                        website = item.get("website", "")
                        snippet = item.get("snippet", "")
                        emails = item.get("emails", [])
                        analysis = item.get("analysis", "")
                        score = item.get("score", "")
                        outreach = item.get("outreach", "")

                        st.markdown("""
                        <div class="result-card">
                        """, unsafe_allow_html=True)

                        st.markdown(
                            f"<div class='company-title'>🏢 {company_name}</div>",
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            "<div class='section-title'>🌐 Website</div>",
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f"<div class='website-link'><a href='{website}' target='_blank'>{website}</a></div>",
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            "<div class='section-title'>📝 Business Snippet</div>",
                            unsafe_allow_html=True
                        )

                        st.write(snippet)

                        st.markdown(
                            "<div class='section-title'>📧 Extracted Emails</div>",
                            unsafe_allow_html=True
                        )

                        if emails:
                            for email in emails:
                                st.markdown(
                                    f"<span class='email-tag'>{email}</span>",
                                    unsafe_allow_html=True
                                )
                        else:
                            st.write("No emails found")

                        st.markdown(
                            "<div class='section-title'>🤖 AI Analysis</div>",
                            unsafe_allow_html=True
                        )

                        st.write(analysis)

                        st.markdown(
                            "<div class='section-title'>⭐ Lead Score</div>",
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f"<div class='score-box'>{score}</div>",
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            "<div class='section-title'>🚀 Personalized Outreach</div>",
                            unsafe_allow_html=True
                        )

                        st.write(outreach)

                        st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Connection Error: {e}")