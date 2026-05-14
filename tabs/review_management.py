import streamlit as st


# =========================================================
# REVIEW MANAGEMENT TAB
# =========================================================

def show_review_management(filtered_df, client):

    st.markdown("## Customer Support Dashboard")

    # =====================================================
    # SESSION STATE INITIALIZATION
    # =====================================================

    if "reply_output" not in st.session_state:
        st.session_state.reply_output = ""

    # =====================================================
    # PRIORITY FILTER
    # =====================================================

    priority_filter = st.selectbox(
        "Select Review Priority",
        ["High", "Medium", "Low"]
    )

    # =====================================================
    # FILTER REVIEWS BASED ON PRIORITY
    # =====================================================

    priority_reviews_df = filtered_df[
        filtered_df["priority"] == priority_filter
    ].copy()

    # =====================================================
    # CREATE DROPDOWN LABELS
    # =====================================================

    priority_reviews_df["dropdown_label"] = (
        "⭐ "
        + priority_reviews_df["rating"].astype(str)
        + " | "
        + priority_reviews_df["source"]
        + " | "
        + priority_reviews_df["review"].str.slice(0, 60)
        + "..."
    )

    # =====================================================
    # REVIEW SELECTOR
    # =====================================================

    selected_label = st.selectbox(
        "Select Review",
        priority_reviews_df["dropdown_label"].head(20)
    )

    # =====================================================
    # GET FULL REVIEW
    # =====================================================

    selected_review = priority_reviews_df[
        priority_reviews_df["dropdown_label"] == selected_label
    ]["review"].values[0]

       # =====================================================
    # AI REVIEW REPLY GENERATOR
    # =====================================================

    if st.button("Generate AI Reply"):

        # =================================================
        # DYNAMIC AI PROMPT BASED ON PRIORITY
        # =================================================

        if priority_filter == "High":

            tone_instruction = """
            The customer is highly dissatisfied.

            Be empathetic, apologetic,
            professional, and solution-oriented.
            """

        elif priority_filter == "Medium":

            tone_instruction = """
            The customer has moderate concerns.

            Be polite, understanding,
            and reassuring.
            """

        else:

            tone_instruction = """
            The customer had a positive experience.

            Be warm, appreciative,
            and friendly.
            """

        # =================================================
        # AI REPLY PROMPT
        # =================================================

        reply_prompt = f"""
        You are a professional restaurant owner replying
        to customer reviews publicly on Google, Zomato,
        and TripAdvisor.

        Review Priority:
        {priority_filter}

        Customer Review:
        {selected_review}

        Instructions:

        - Understand the actual issue or compliment.
        - Reply naturally like a real business owner.
        - Avoid generic robotic responses.
        - If review is negative:
            apologize sincerely,
            acknowledge the issue,
            mention improvement action.
        - If review is positive:
            appreciate the customer warmly.
        - If review is neutral:
            sound polite and professional.
        - Keep response under 80 words.
        - Make the response human-like.

        Generate only the reply.
        """

        with st.spinner("Generating Reply..."):

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": reply_prompt
                        }
                    ]
                )

                st.session_state.reply_output = (
                    response.choices[0].message.content
                )

            except Exception as error:

                st.error(f"Error generating reply: {error}")
    # =====================================================
    # DISPLAY AI REPLY
    # =====================================================

    if st.session_state.reply_output:

        with st.container(border=True):

            st.markdown("### 🤖 AI Generated Reply")
            st.write(st.session_state.reply_output)

    # =====================================================
    # HIGH PRIORITY REVIEWS
    # =====================================================

    st.markdown("#### 🔴 High Priority Reviews")

    high_priority = filtered_df[
        filtered_df["priority"] == "High"
    ].head(3)

    for _, row in high_priority.iterrows():

        st.markdown(
            f"""
        <div class="review-card high-priority">

        <div class="review-business">
        {row['business_name']}
        </div>

        <div class="review-meta">
        ⭐ {row['rating']} | 🌐 {row['source']}
        </div>

        <div class="review-text">
        {row['review']}
        </div>

        </div>
        """,
            unsafe_allow_html=True
    )

    # =====================================================
    # MEDIUM PRIORITY REVIEWS
    # =====================================================

    st.markdown("#### 🟠 Medium Priority Reviews")

    medium_priority = filtered_df[
        filtered_df["priority"] == "Medium"
    ].head(3)

    for _, row in medium_priority.iterrows():

        st.markdown(
            f"""
        <div class="review-card medium-priority">

        <div class="review-business">
        {row['business_name']}
        </div>

        <div class="review-meta">
        ⭐ {row['rating']} | 🌐 {row['source']}
        </div>

        <div class="review-text">
        {row['review']}
        </div>

        </div>
        """,
            unsafe_allow_html=True
    )

    # =====================================================
    # LOW PRIORITY REVIEWS
    # =====================================================

    st.markdown("#### 🟢 Low Priority Reviews")

    low_priority = filtered_df[
        filtered_df["priority"] == "Low"
    ].head(3)

    for _, row in low_priority.iterrows():

        st.markdown(
            f"""
        <div class="review-card low-priority">

        <div class="review-business">
        {row['business_name']}
        </div>

        <div class="review-meta">
        ⭐ {row['rating']} | 🌐 {row['source']}
        </div>

        <div class="review-text">
        {row['review']}
        </div>

        </div>
        """,
            unsafe_allow_html=True
    )

        