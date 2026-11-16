
from pathlib import Path

import streamlit as st

from recommender import load_songs, recommend_songs
from evaluator import evaluate_recommendation


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "songs.csv"
songs = load_songs(str(DATA_PATH))


st.set_page_config(
    page_title="MoodTunes 2.0",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 MoodTunes 2.0")
st.write(
    "Discover music based on your preferences. "
    "Each recommendation is also evaluated for match quality."
)

st.sidebar.header("Your Music Preferences")

genres = sorted(set(song["genre"] for song in songs))
moods = sorted(set(song["mood"] for song in songs))

genre = st.sidebar.selectbox("Favorite genre", genres)
mood = st.sidebar.selectbox("Favorite mood", moods)

energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.7, 0.05)
valence = st.sidebar.slider("Positivity", 0.0, 1.0, 0.7, 0.05)
tempo = st.sidebar.slider("Tempo (BPM)", 0, 200, 120)
danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.7, 0.05)
acousticness = st.sidebar.slider("Acousticness", 0.0, 1.0, 0.5, 0.05)

number_of_songs = st.sidebar.slider(
    "Number of recommendations", 1, 10, 5
)

if st.button("Find My Music", type="primary"):
    preferences = {
        "genre": genre,
        "mood": mood,
        "energy": energy,
        "valence": valence,
        "tempo_bpm": tempo,
        "danceability": danceability,
        "acousticness": acousticness
    }

    recommendations = recommend_songs(
        preferences, songs, k=number_of_songs
    )

    st.subheader("Your Recommendations")

    for index, recommendation in enumerate(recommendations, start=1):
        song, ranking_score, explanation = recommendation

        evaluation = evaluate_recommendation(preferences, song)

        with st.container(border=True):
            st.markdown(
                f"### {index}. {song['title']} - {song['artist']}"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Recommendation Score",
                    f"{ranking_score:.2f}/9.00"
                )

            with col2:
                st.metric(
                    "Match Quality",
                    f"{evaluation['quality_score']}%"
                )

            if evaluation["warning"]:
                st.warning(evaluation["message"])
            else:
                st.success(evaluation["message"])

            st.write("**Why this song was recommended:**")
            st.write(explanation)

            with st.expander("View detailed evaluation"):
                for feature, score in evaluation["feature_scores"].items():
                    st.write(f"{feature.title()}: {score * 100:.1f}%")
