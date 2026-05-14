import pandas as pd
import random
import numpy as np
from utils.priority import assign_priority
from utils.topic_extractor import extract_topic
from utils.emotion_detector import detect_emotion


def load_data():

    # FIX RANDOMNESS

    random.seed(42)
    np.random.seed(42)

    # LOAD DATASET

    df = pd.read_csv(
        "data/Restaurant_Reviews.tsv",
        delimiter="\t"
    )

    df.columns = ["review", "liked"]

    # SENTIMENT

    df["sentiment"] = df["liked"].map({
        1: "Positive",
        0: "Negative"
    })

    # DISTRIBUTION

    positive_df = df[df["liked"] == 1].sample(
        700,
        replace=True
    )

    negative_df = df[df["liked"] == 0].sample(
        300,
        replace=True
    )

    df = pd.concat([positive_df, negative_df])


    df = df.sample(frac=1).reset_index(drop=True)

    # MOCK BUSINESSES

    businesses = [
        "Spice Garden",
        "Bombay Canteen",
        "Royal Dine",
        "Urban Tadka"
    ]

    df["business_name"] = [
        businesses[i % len(businesses)]
        for i in range(len(df))
    ]

    # MOCK CITIES
    city_map = {
        "Spice Garden": "Mumbai",
        "Bombay Canteen": "Pune",
        "Royal Dine": "Delhi",
        "Urban Tadka": "Bangalore"
    }

    # MOCK WEBSITES

    website_map = {
    "Spice Garden": "https://spicegarden.com",
    "Bombay Canteen": "https://bombaycanteen.com",
    "Royal Dine": "https://royaldine.com",
    "Urban Tadka": "https://urbantadka.com"
    }

    business_details = {
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


    # SOURCES

    sources = [
        "Google",
        "Zomato",
        "Swiggy",
        "TripAdvisor"
    ]

    df["source"] = [
        random.choice(sources)
        for _ in range(len(df))
    ]

    # RATINGS

    df["rating"] = df["liked"].apply(
        lambda x: 5 if x == 1 else 2
    )

    # NEUTRAL REVIEWS

    neutral_indexes = df.sample(
        frac=0.15,
        random_state=42
    ).index

    df.loc[neutral_indexes, "sentiment"] = "Neutral"

    df.loc[neutral_indexes, "rating"] = 3

    # MEDIUM NEGATIVE RATINGS

    medium_indexes = df[
        (df["rating"] == 2)
        & (df["sentiment"] == "Negative")
    ].sample(
        frac=0.30,
        random_state=42
    ).index

    df.loc[medium_indexes, "rating"] = 3

    # NLP FEATURES

    df["priority"] = df["rating"].apply(
        assign_priority
    )

    df["topic"] = df["review"].apply(
        extract_topic
    )

    df["emotion"] = df["review"].apply(
        detect_emotion
    )

    df["city"] = df["business_name"].apply(
    lambda x: business_details[x]["city"]
    )

    df["website"] = df["business_name"].apply(
    lambda x: business_details[x]["website"]
    )

    return df