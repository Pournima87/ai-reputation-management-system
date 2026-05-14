import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from utils.topic_extractor import extract_topic
from utils.emotion_detector import detect_emotion
from utils.priority import assign_priority
from utils.data_loader import load_data
from tabs.dashboard import show_dashboard
from tabs.ai_insights import show_ai_insights
from tabs.review_management import show_review_management
from tabs.advanced_analytics import show_advanced_analytics
from components.sidebar import render_sidebar

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Reputation Manager",
    page_icon="⭐",
    layout="wide"
)

# =========================================================
# LOAD CSS
# =========================================================

def load_css():

    with open("styles/main.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# =========================================================
# SESSION STATE
# =========================================================

if "summary_output" not in st.session_state:
    st.session_state.summary_output = ""

if "reply_output" not in st.session_state:
    st.session_state.reply_output = ""

if "recommendation_output" not in st.session_state:
    st.session_state.recommendation_output = ""

# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    """
<div style="
background: linear-gradient(135deg, #081028 0%, #0b1d4d 45%, #3b0ca3 100%);
padding: 28px 34px;
border-radius: 24px;
display: flex;
justify-content: space-between;
align-items: flex-start;
min-height: 160px;
margin-bottom: 18px;
">

<div>

<div style="
font-size: 42px;
margin-bottom: 10px;
">

</div>

<div style="
color: white;
font-size: 36px;
font-weight: 800;
line-height: 1.15;
margin-bottom: 10px;
letter-spacing: -1px;
">
⭐AI Reputation Intelligence Platform
</div>

<div style="
color: rgba(255,255,255,0.72);
font-size: 16px;
line-height: 1.7;
max-width: 760px;
">
AI-powered customer sentiment monitoring,
review intelligence, reputation analytics,
and business recommendation engine.
</div>

</div>

<div style="
display:flex;
gap:16px;
">


</div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# LOAD DATA
# =========================================================

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

filters = render_sidebar(df)

selected_business = filters["selected_business"]
selected_city = filters["selected_city"]
selected_website = filters["selected_website"]

# =========================================================
# FILTERING
# =========================================================

filtered_df = df.copy()

# BUSINESS FILTER

if selected_business != "All Businesses":

    filtered_df = filtered_df[
        filtered_df["business_name"]
        == selected_business
    ]

# CITY FILTER

if selected_city != "All Cities":

    filtered_df = filtered_df[
        filtered_df["city"]
        == selected_city
    ]

# WEBSITE FILTER

if selected_website != "All Websites":

    filtered_df = filtered_df[
        filtered_df["website"]
        == selected_website
    ]

# =========================================================
# EMPTY DATA CHECK
# =========================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No reviews found for selected filters."
    )

    st.stop()

# =========================================================
# KPI METRICS
# =========================================================

total_reviews = len(filtered_df)

positive_reviews = len(
    filtered_df[
        filtered_df["sentiment"] == "Positive"
    ]
)

negative_reviews = len(
    filtered_df[
        filtered_df["sentiment"] == "Negative"
    ]
)

avg_rating = round(
    filtered_df["rating"].mean(),
    1
)
neutral_reviews = len(
    filtered_df[
        filtered_df["sentiment"] == "Neutral"
    ]
)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4= st.tabs([
    "Dashboard",
    "AI Insights",
    "Review Management",
    "Advanced Analytics"
])

with tab1:
    show_dashboard(filtered_df, selected_business)

# =========================================================
# TAB 2 — AI INSIGHTS
# =========================================================

with tab2:
    show_ai_insights(filtered_df, client)   

# =========================================================
# TAB 3 — REVIEW MANAGEMENT
# =========================================================

with tab3:
    show_review_management(filtered_df, client)

# =========================================================
# TAB 4 — ADVANCED ANALYTICS
# =========================================================

with tab4:
    show_advanced_analytics(filtered_df)

# =========================================================
# FOOTER
# =========================================================


st.caption(
    "⭐ AI Reputation Management System | Built with Streamlit + OpenAI"
)