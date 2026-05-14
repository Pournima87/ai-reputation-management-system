import streamlit as st



# =========================================================
# SIDEBAR COMPONENT
# =========================================================

def render_sidebar(df):

    st.sidebar.header("Filters")

    # =====================================================
    # BUSINESS FILTER
    # =====================================================

    business_options = [
        "All Businesses",
        *sorted(df["business_name"].unique())
    ]

    selected_business = st.sidebar.selectbox(
        "Select Business",
        business_options
    )

    # =====================================================
    # BUSINESS INFO
    # =====================================================

    business_info = {
        "Spice Garden": {
            "city": "Pune",
            "website": "www.spicegarden.com"
        },
        "Bombay Canteen": {
            "city": "Mumbai",
            "website": "www.bombaycanteen.com"
        },
        "Royal Dine": {
            "city": "Delhi",
            "website": "www.royaldine.com"
        },
        "Urban Tadka": {
            "city": "Bangalore",
            "website": "www.urbantadka.com"
        }
    }

    # =====================================================
    # CITY FILTER
    # =====================================================

    if selected_business == "All Businesses":

        city_options = [
            "All Cities",
            *sorted(df["city"].unique())
        ]

    else:

        city_options = [
            "All Cities",
            business_info[selected_business]["city"]
        ]

    selected_city = st.sidebar.selectbox(
        "Select City",
        city_options
    )

    # =====================================================
    # WEBSITE FILTER
    # =====================================================

    if selected_business == "All Businesses":

        website_options = [
            "All Websites",
            *sorted(df["website"].unique())
        ]

    else:

        website_options = [
            "All Websites",
            business_info[selected_business]["website"]
        ]

    selected_website = st.sidebar.selectbox(
        "Select Website",
        website_options
    )

    # =====================================================
    # RETURN FILTERS
    # =====================================================

    return {
        "selected_business": selected_business,
        "selected_city": selected_city,
        "selected_website": selected_website
    }

    # =====================================================
    # SIDEBAR INFO
    # =====================================================

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
        Use filters to analyze customer sentiment,
        business reputation, and operational trends.
        """
    )

    # =====================================================
    # RETURN FILTER VALUES
    # =====================================================

    return {
        "selected_business": selected_business,
        "selected_city": selected_city,
        "selected_website": selected_website
    }