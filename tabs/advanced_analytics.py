import re
from collections import Counter

import plotly.express as px
import streamlit as st


# =========================================================
# ADVANCED ANALYTICS TAB
# =========================================================

def show_advanced_analytics(filtered_df):

    st.markdown("## Data Intelligence & NLP Analytics")
    st.caption(
    "Advanced NLP analysis of customer emotions, review topics, complaints, and compliments."
    )
    chart1, chart2 = st.columns(2)

    # =====================================================
    # EMOTION DISTRIBUTION
    # =====================================================

    with chart1:

        emotion_count = (
            filtered_df["emotion"]
            .value_counts()
        )

        fig_emotion = px.pie(
            values=emotion_count.values,
            names=emotion_count.index,
            title="Emotion Distribution",
            hole=0.45
        )

        fig_emotion.update_traces(
            textinfo="percent+label",
            pull=[0.03] * len(emotion_count)
        )

        fig_emotion.update_layout(
            paper_bgcolor="#0b1120",
            plot_bgcolor="#0b1120",

            font=dict(
                color="white",
                size=14
            ),

        title_font=dict(
            size=24
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            t=60,
            b=10,
            l=10,
            r=10
        )
    )

        st.plotly_chart(
            fig_emotion,
            use_container_width=True,
            config={
                "displayModeBar": False
            },
            key="emotion_chart"
        )

    # =====================================================
    # TOPIC DISTRIBUTION
    # =====================================================

    with chart2:

        topic_count = (
            filtered_df["topic"]
            .value_counts()
        )

        fig_topic = px.bar(
            x=topic_count.index,
            y=topic_count.values,
            color=topic_count.index,
            title="Topic Distribution",
            text_auto=True
        )
        fig_topic.update_traces(
            marker_line_width=0,
            opacity=0.9
        )

        fig_topic.update_layout(
            paper_bgcolor="#0b1120",
            plot_bgcolor="#0b1120",

            font=dict(
                color="white",
                size=14
            ),

            title_font=dict(
                size=24
            ),

            xaxis=dict(
                showgrid=False
            ),

            yaxis=dict(
                gridcolor="rgba(255,255,255,0.08)"
            ),

            legend=dict(
                bgcolor="rgba(0,0,0,0)"
            ),

            margin=dict(
                t=60,
                b=10,
                l=10,
                r=10
            )
        )

        st.plotly_chart(
            fig_topic,
            use_container_width=True,
            config={
                "displayModeBar": False
            },
            key="topic_chart"
        )

    # =====================================================
    # COMMON COMPLAINTS & COMPLIMENTS
    # =====================================================

    st.markdown("### Common Complaints & Compliments")

    # =====================================================
    # POSITIVE REVIEWS TEXT
    # =====================================================

    positive_text = " ".join(

        filtered_df[
            filtered_df["sentiment"] == "Positive"
        ]["review"]

    )

    # =====================================================
    # NEGATIVE REVIEWS TEXT
    # =====================================================

    negative_text = " ".join(

        filtered_df[
            filtered_df["sentiment"] == "Negative"
        ]["review"]

    )

    # =====================================================
    # EXTRACT WORDS
    # =====================================================

    positive_words = re.findall(
        r"\b[a-zA-Z]+\b",
        positive_text.lower()
    )

    negative_words = re.findall(
        r"\b[a-zA-Z]+\b",
        negative_text.lower()
    )

    # =====================================================
    # STOPWORDS
    # =====================================================

    stopwords = [
        "the",
        "and",
        "was",
        "were",
        "this",
        "that",
        "with",
        "have",
        "had",
        "food",
        "very",
        "from",
        "there"
    ]

    # =====================================================
    # CLEAN WORDS
    # =====================================================

    positive_words = [

        word for word in positive_words

        if word not in stopwords
        and len(word) > 3

    ]

    negative_words = [

        word for word in negative_words

        if word not in stopwords
        and len(word) > 3

    ]

    # =====================================================
    # MOST COMMON WORDS
    # =====================================================

    positive_common = Counter(
        positive_words
    ).most_common(5)

    negative_common = Counter(
        negative_words
    ).most_common(5)

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    col1, col2 = st.columns(2)

    # =====================================================
    # COMMON COMPLIMENTS
    # =====================================================

    with col1:

        st.markdown("##### 😊 Common Compliments")

        for word, count in positive_common:

            st.markdown(
                f"""
                <div class="keyword-positive">
                {word} ({count})
                </div>
                """,
                unsafe_allow_html=True
            )

    # =====================================================
    # COMMON COMPLAINTS
    # =====================================================

    with col2:

        st.markdown("##### 😠 Common Complaints")

        for word, count in negative_common:

            st.markdown(
                f"""
                <div class="keyword-negative">
                {word} ({count})
                </div>
                """,
                unsafe_allow_html=True
            )