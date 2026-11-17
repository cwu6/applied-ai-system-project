
from math import isfinite
import logging
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent.parent / "vibefinder.log"

logger = logging.getLogger("vibefinder")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)


def evaluate_recommendation(
    user_prefs: dict,
    song: dict,
    threshold: float = 60.0
) -> dict:
    """
    Evaluates how closely a recommended song matches user preferences.

    Returns a quality score from 0 to 100 and a warning
    if the recommendation does not meet the threshold.
    """

    required_fields = [
        "genre", "mood", "energy", "valence",
        "tempo_bpm", "danceability", "acousticness"
    ]

    for field in required_fields:
        if field not in user_prefs or field not in song:
            raise ValueError(f"Missing required field: {field}")

    if (
        isinstance(threshold, bool)
        or not isinstance(threshold, (int, float))
        or not isfinite(threshold)
        or not 0 <= threshold <= 100
    ):
        raise ValueError("Threshold must be a number between 0 and 100.")

    numeric_fields = [
        "energy", "valence", "tempo_bpm",
        "danceability", "acousticness"
    ]

    for field in numeric_fields:
        user_value = user_prefs[field]
        song_value = song[field]

        if not isinstance(user_value, (int, float)) or isinstance(user_value, bool):
            raise ValueError(f"Invalid user preference: {field}")

        if not isinstance(song_value, (int, float)) or isinstance(song_value, bool):
            raise ValueError(f"Invalid song value: {field}")

        if not isfinite(user_value) or not isfinite(song_value):
            raise ValueError(f"{field} must be a finite number.")

        if field == "tempo_bpm":
            if not 0 <= user_value <= 200 or not 0 <= song_value <= 200:
                raise ValueError("Tempo must be between 0 and 200 BPM.")
        else:
            if not 0 <= user_value <= 1 or not 0 <= song_value <= 1:
                raise ValueError(f"{field} must be between 0 and 1.")

    for field in ["genre", "mood"]:
        if not isinstance(user_prefs[field], str) or not user_prefs[field].strip():
            raise ValueError(f"Invalid user preference: {field}")

        if not isinstance(song[field], str) or not song[field].strip():
            raise ValueError(f"Invalid song value: {field}")

    feature_scores = {
        "genre": 1.0 if song["genre"] == user_prefs["genre"] else 0.0,
        "mood": 1.0 if song["mood"] == user_prefs["mood"] else 0.0,
        "energy": 1 - abs(song["energy"] - user_prefs["energy"]),
        "valence": 1 - abs(song["valence"] - user_prefs["valence"]),
        "tempo": 1 - abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / 200,
        "danceability": 1 - abs(song["danceability"] - user_prefs["danceability"]),
        "acousticness": 1 - abs(song["acousticness"] - user_prefs["acousticness"])
    }

    quality_score = (
        sum(feature_scores.values()) / len(feature_scores)
    ) * 100

    quality_score = round(quality_score, 2)

    warning = quality_score < threshold

    if warning:
        message = "Weak match: this song may not closely match your preferences."
    else:
        message = "Good match: this song closely matches your preferences."

    logger.info(
    "Evaluated song='%s' quality_score=%.2f warning=%s",
    song.get("title", "Unknown"),
    quality_score,
    warning
    )
    
    return {
        "quality_score": quality_score,
        "feature_scores": feature_scores,
        "warning": warning,
        "message": message
    }
