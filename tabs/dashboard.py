import streamlit as st
import plotly.express as px


def show_dashboard(filtered_df, selected_business):

    # =====================================================
    # KPI METRICS
    # =====================================================

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

    neutral_reviews = len(
        filtered_df[
            filtered_df["sentiment"] == "Neutral"
        ]
    )

    avg_rating = round(
        filtered_df["rating"].mean(),
        1
    )



    # =====================================================
    # KPI CARDS
    # =====================================================


    col1, col2, col3, col4, col5 = st.columns(5)

# =====================================================
# TOTAL REVIEWS
# =====================================================

    with col1:

        st.markdown(f"""
        <div class="kpi-card kpi-blue">

        <div class="kpi-icon-circle">
            📊
        </div>

        <div class="kpi-title">
            Total Reviews
        </div>

        <div class="kpi-value">
            {total_reviews}
        </div>

        <div class="kpi-subtitle">
            📈 All time reviews
        </div>

        </div>
        """, unsafe_allow_html=True)

# =====================================================
# POSITIVE
# =====================================================

    with col2:

        positive_percent = round(
        (positive_reviews / total_reviews) * 100,
        1
    )

        st.markdown(f"""
        <div class="kpi-card kpi-green">

        <div class="kpi-icon-circle">
            😊
        </div>

        <div class="kpi-title">
            Positive Reviews
        </div>

        <div class="kpi-value">
            {positive_reviews}
        </div>

        <div class="kpi-subtitle">
            ↗ {positive_percent}% of total
        </div>

        </div>
        """, unsafe_allow_html=True)

# =====================================================
# NEGATIVE
# =====================================================

    with col3:

        negative_percent = round(
        (negative_reviews / total_reviews) * 100,
        1
    )

        st.markdown(f"""
        <div class="kpi-card kpi-red">

        <div class="kpi-icon-circle">
            😠
        </div>

        <div class="kpi-title">
            Negative Reviews
        </div>

        <div class="kpi-value">
            {negative_reviews}
        </div>

        <div class="kpi-subtitle">
            ↘ {negative_percent}% of total
        </div>

        </div>
        """, unsafe_allow_html=True)

# =====================================================
# NEUTRAL
# =====================================================

    with col4:

        neutral_percent = round(
        (neutral_reviews / total_reviews) * 100,
        1
    )

        st.markdown(f"""
        <div class="kpi-card kpi-orange">

        <div class="kpi-icon-circle">
            😐
        </div>

        <div class="kpi-title">
            Neutral Reviews
        </div>

        <div class="kpi-value">
            {neutral_reviews}
        </div>

        <div class="kpi-subtitle">
            ↗ {neutral_percent}% of total
        </div>

        </div>
        """, unsafe_allow_html=True)

# =====================================================
# RATING
# =====================================================

    with col5:

        st.markdown(f"""
        <div class="kpi-card kpi-purple">

        <div class="kpi-icon-circle">
            ⭐
        </div>

        <div class="kpi-title">
            Average Rating
        </div>

        <div class="kpi-value">
            {avg_rating}
        </div>

        <div class="kpi-subtitle">
            ⭐ Out of 5
        </div>

        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # BUSINESS STATUS
    # =====================================================

    if avg_rating > 4.0:

        status = "Excellent"
        status_color = "#22c55e"
        status_icon = "🛡️"

        status_message = (
            "Great job! Your business is performing "
            "extremely well and customers are highly satisfied."
        )

    elif avg_rating >= 4.0:

        status = "Good"
        status_color = "#3b82f6"
        status_icon = "📈"

        status_message = (
            "Your reputation is stable and customers "
            "are generally happy with your services."
        )

    else:

        status = "Average"
        status_color = "#f59e0b"
        status_icon = "⚠️"

        status_message = (
            "Customer satisfaction needs improvement "
            "in some operational areas."
        )
    

    st.markdown(
        f"""
        <div
        class="business-status-card"
        style="
            border:1px solid {status_color}40;
        "
        >

        <div class="status-left">

        <div
        class="status-icon"
        style="
        background:{status_color}20;
        color:{status_color};
        "
        >
        {status_icon}
        </div>

        <div>

        <div
        class="status-title"
        style="color:{status_color};"
        >
        Business Reputation:
        {status}
        </div>

        <div class="status-message">
        {status_message}
        </div>

        </div>

        </div>

        <div
        class="status-badge"
        style="
        background:{status_color}15;
        color:{status_color};
        border:1px solid {status_color}35;
        "
        >
        ⭐ {avg_rating}/5
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # SENTIMENT DATA
    # =====================================================

    sentiment_count = (
        filtered_df["sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_count.columns = [
        "Sentiment",
        "Count"
    ]

    # =====================================================
    # SENTIMENT CHARTS
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    chart1, chart2 = st.columns(
    [1,1],
    gap="medium"
    )



# =====================================================
# PIE CHART
# =====================================================


    fig_pie = px.pie(
        sentiment_count,
        names="Sentiment",
        values="Count",
        color="Sentiment",

        color_discrete_map={
            "Positive": "#5B8CFF",
            "Negative": "#FF4D8D",
            "Neutral": "#B06CFF"
            }
    )

    fig_pie.update_traces(

        hole=0.60,
        textfont_size=14,
        textfont_color="white",
        textinfo="percent",
        pull=[0.02, 0.02, 0.02],
        marker=dict(

            line=dict(
                color="rgba(255,255,255,0.10)",
                width=2
            )
        )
    )

    fig_pie.update_layout(

        height=380,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            family="Inter"
        ),

        legend=dict(

            orientation="v",

            y=0.95,

            x=0.95,

            font=dict(
                size=13
            ),

            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            t=10,
            b=10,
            l=10,
            r=10
        )
    )


    with chart1:

        st.markdown("""

        <div class="chart-title">
            Sentiment Distribution
        </div>
        """, unsafe_allow_html=True)

    

        st.plotly_chart(
            fig_pie,
            use_container_width=True,
            config={"displayModeBar": False}
        )


# =====================================================
# BAR CHART
# =====================================================

    fig_bar = px.bar(
        sentiment_count,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        text_auto=True,

        color_discrete_map={
            "Positive": "#5B8CFF",
            "Negative": "#FF4D8D",
            "Neutral": "#B06CFF"
        }
    )

    fig_bar.update_traces(

        textfont_size=18,
        textfont_color="white",
        textposition="inside",
        marker_line_color="rgba(255,255,255,0.10)",
        marker_line_width=1.8,
        opacity=0.95
    )
        
    fig_bar.update_layout(
        paper_bgcolor="#0b1120",
        plot_bgcolor="#0b1120",
        height=380,

        font=dict(
            color="white",
            family="Inter"
        ),

        xaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=16)
        ),

        yaxis=dict(
            title="Count",
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False,
            tickfont=dict(size=15)
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            t=10,
            b=10,
            l=10,
            r=10
        )
    )

    with chart2:

        st.markdown("""
        <div class="chart-title">
            Sentiment Breakdown
        </div>
        """, unsafe_allow_html=True)


        st.plotly_chart(
            fig_bar,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # =====================================================
    # SOURCE-WISE ANALYTICS
    # =====================================================

    st.markdown("#### Source-wise Review Distribution")

    source_count = (
        filtered_df["source"]
        .value_counts()
        .reset_index()
    )

    source_count.columns = [
        "Source",
        "Count"
    ]

    fig_source = px.bar(
        source_count,
        x="Source",
        y="Count",
        color="Source",
        title="Reviews by Platform",
        text_auto=True,

        color_discrete_map={
            "Swiggy": "#6EC1FF",
            "Zomato": "#1D8FFF",
            "Google": "#F7A8B8",
            "TripAdvisor": "#FF3B4D"
        }
    )

    fig_source.update_traces(

        textfont_size=18,
        textfont_color="white",
        textposition="inside",

        marker_line_color="rgba(255,255,255,0.10)",
        marker_line_width=1.5,

        opacity=0.96,

        hovertemplate=
        "<b>%{x}</b><br>" +
        "Reviews: %{y}<extra></extra>"
    )

    fig_source.update_layout(

        height=520,

        paper_bgcolor="#070B1A",
        plot_bgcolor="#070B1A",

        font=dict(
            color="white",
            family="Arial"
        ),

        title=dict(
            text="Reviews by Platform",
            x=0.02,
            font=dict(
                size=20,
                color="white"
            )
        ),

        xaxis=dict(

            title="Source",

            showgrid=False,

            zeroline=False,

            tickfont=dict(
                size=16
            )
        ),

        yaxis=dict(

            title="Count",

            gridcolor="rgba(255,255,255,0.08)",

            tickfont=dict(
                size=15
            )
        ),

        legend=dict(

            title="Source",

            bgcolor="rgba(0,0,0,0)",

            font=dict(
                size=15
            ),

            y=0.82,
            x=1.02
        ),

        margin=dict(
            t=70,
            b=40,
            l=40,
            r=40
        )
    )

    st.plotly_chart(
            fig_source,
            use_container_width=True
    )

    # =====================================================
    # EXECUTIVE INSIGHTS
    # =====================================================

    st.markdown("### Executive Insights")
    st.markdown("""
    <div class="insight-box">

    <ul>
    <li>Total customer reviews analyzed: 1000</li>
    <li>Positive sentiment dominates customer feedback.</li>
    <li>Negative reviews mainly involve delays and waiting time.</li>
    <li>Most engagement comes from review platforms.</li>
    <li>Current average business rating is 4.0.</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # RECENT REVIEWS
    # =====================================================

    st.markdown("### Recent Reviews")

    recent_reviews = filtered_df.tail(10)

    recent_reviews_display = recent_reviews.copy()

    recent_reviews_display["review"] = (
        recent_reviews_display["review"]
        .astype(str)
        .str.slice(0, 70) + "..."
    )

    st.dataframe(
        recent_reviews[
            [
                "business_name",
                "source",
                "rating",
                "sentiment",
                "review"
            ]
        ],
        use_container_width=True,
        height=430
    )

    # =====================================================
    # DATASET PREVIEW
    # =====================================================

    with st.expander("View Dataset Preview"):

        st.dataframe(
            filtered_df.head(20),
            use_container_width=True
        )

    # =====================================================
    # DOWNLOAD BUTTON
    # =====================================================

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Review Data",
        data=csv,
        file_name=f"{selected_business}_reviews.csv",
        mime="text/csv"
    )