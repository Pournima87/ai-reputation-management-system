def detect_emotion(review):

    review = str(review).lower()

    if any(word in review for word in [
        "amazing", "great", "awesome", "good",
        "excellent", "loved", "fantastic",
        "perfect", "delicious"
    ]):
        return "Happy"

    elif any(word in review for word in [
        "worst", "terrible", "awful", "slow",
        "bad", "hate", "cold", "rude",
        "dirty", "late"
    ]):
        return "Frustrated"

    elif any(word in review for word in [
        "disappointed", "average", "poor",
        "boring", "mediocre"
    ]):
        return "Disappointed"

    else:
        return "Neutral"