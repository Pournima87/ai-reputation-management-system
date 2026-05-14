# =========================================================
# FUNCTIONS
# =========================================================

def extract_topic(review):

    review = str(review).lower()

    if any(word in review for word in [
        "food", "taste", "dish", "meal", "burger",
        "pizza", "fries", "chicken", "rice",
        "pasta", "drink", "menu", "flavor",
        "spicy", "sweet", "delicious", "quality"
    ]):
        return "Food Quality"

    elif any(word in review for word in [
        "service", "staff", "waiter", "manager",
        "slow", "friendly", "rude", "server",
        "customer", "employees"
    ]):
        return "Service"

    elif any(word in review for word in [
        "price", "cost", "expensive", "cheap",
        "value", "money", "discount"
    ]):
        return "Pricing"

    elif any(word in review for word in [
        "ambience", "music", "atmosphere",
        "decor", "vibe", "lighting"
    ]):
        return "Ambience"

    else:
        return "General"