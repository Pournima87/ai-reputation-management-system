import streamlit as st


# =========================================================
# AI INSIGHTS TAB
# =========================================================

def show_ai_insights(filtered_df, client):

    st.markdown("## AI Business Consultant")

    # =====================================================
    # SESSION STATE INITIALIZATION
    # =====================================================

    if "summary_output" not in st.session_state:
        st.session_state.summary_output = ""

    if "recommendation_output" not in st.session_state:
        st.session_state.recommendation_output = ""

    # =====================================================
    # PREPARE REVIEW DATA
    # =====================================================

    reviews = filtered_df["review"].dropna().tolist()[:20]
    all_reviews = " ".join(reviews)

    # =====================================================
    # AI REPUTATION SUMMARY
    # =====================================================

    summary_prompt = f"""
    Analyze these restaurant reviews and provide:

    1. Overall customer sentiment
    2. Main compliments
    3. Main complaints
    4. Business improvement suggestions

    Reviews:
    {all_reviews}
    """

    if st.button("Generate AI Reputation Summary"):

        with st.spinner("Generating AI Insights..."):

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": summary_prompt
                        }
                    ]
                )

                st.session_state.summary_output = (
                    response.choices[0].message.content
                )

            except Exception as error:
                st.error(f"Error generating summary: {error}")

    # =====================================================
    # DISPLAY AI SUMMARY
    # =====================================================

    if st.session_state.summary_output:

        with st.container(border=True):

            st.markdown("### AI Reputation Summary")
            st.write(st.session_state.summary_output)

    # =====================================================
    # DYNAMIC POSITIVE SUMMARY
    # =====================================================

    positive_df = filtered_df[
        filtered_df["sentiment"] == "Positive"
    ]

    positive_topics = (
        positive_df["topic"]
        .value_counts()
        .head(3)
        .index.tolist()
    )

    positive_emotions = (
        positive_df["emotion"]
        .value_counts()
        .head(2)
        .index.tolist()
    )

    st.markdown(
        '<div class="ai-summary-card positive-card">',
        unsafe_allow_html=True
    )

    st.markdown("#### 🟢 Positive Review Summary")

    st.write(f"""
    Customers highly appreciate:

    • {positive_topics[0] if len(positive_topics) > 0 else "Food Quality"}

    • {positive_topics[1] if len(positive_topics) > 1 else "Service"}

    • {positive_topics[2] if len(positive_topics) > 2 else "Ambience"}

    Most customers feel:

    • {positive_emotions[0] if len(positive_emotions) > 0 else "Happy"}

    • {positive_emotions[1] if len(positive_emotions) > 1 else "Satisfied"}
    """)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # DYNAMIC NEGATIVE SUMMARY
    # =====================================================

    negative_df = filtered_df[
        filtered_df["sentiment"] == "Negative"
    ]

    negative_topics = (
        negative_df["topic"]
        .value_counts()
        .head(3)
        .index.tolist()
    )

    negative_emotions = (
        negative_df["emotion"]
        .value_counts()
        .head(2)
        .index.tolist()
    )

    st.markdown(
        '<div class="ai-summary-card negative-card">',
        unsafe_allow_html=True
    )

    st.markdown("#### 🔴 Negative Review Summary")

    st.write(f"""
    Main complaints are related to:

    • {negative_topics[0] if len(negative_topics) > 0 else "Service"}

    • {negative_topics[1] if len(negative_topics) > 1 else "Food Quality"}

    • {negative_topics[2] if len(negative_topics) > 2 else "Pricing"}

    Customers mostly feel:

    • {negative_emotions[0] if len(negative_emotions) > 0 else "Frustrated"}

    • {negative_emotions[1] if len(negative_emotions) > 1 else "Disappointed"}
    """)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # DYNAMIC NEUTRAL SUMMARY
    # =====================================================

    neutral_df = filtered_df[
        filtered_df["sentiment"] == "Neutral"
    ]

    neutral_topics = (
        neutral_df["topic"]
        .value_counts()
        .head(3)
        .index.tolist()
    )

    st.markdown(
        '<div class="ai-summary-card neutral-card">',
        unsafe_allow_html=True
    )

    st.markdown("#### 🟡 Neutral Review Summary")

    st.write(f"""
    Neutral reviews commonly mention:

    • {neutral_topics[0] if len(neutral_topics) > 0 else "Experience"}

    • {neutral_topics[1] if len(neutral_topics) > 1 else "Service"}

    • {neutral_topics[2] if len(neutral_topics) > 2 else "Food"}
    """)

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # AI RECOMMENDATIONS
    # =====================================================

    st.markdown("## AI Actionable Recommendations")

    recommendation_prompt = f"""
    Analyze these restaurant reviews and provide:

    1. Operational improvements
    2. Food quality suggestions
    3. Service improvements
    4. Customer retention ideas
    5. Reputation management strategy

    Reviews:
    {all_reviews}
    """

    if st.button("Generate AI Recommendations"):

        with st.spinner("Generating Recommendations..."):

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": recommendation_prompt
                        }
                    ]
                )

                st.session_state.recommendation_output = (
                    response.choices[0].message.content
                )

            except Exception as error:
                st.error(f"Error generating recommendations: {error}")

    # =====================================================
    # DISPLAY RECOMMENDATIONS
    # =====================================================

    if st.session_state.recommendation_output:

        with st.container(border=True):

            st.markdown("## AI Recommendations")
            st.write(st.session_state.recommendation_output)