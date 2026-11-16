
import pytest

from src.evaluator import evaluate_recommendation
from src.recommender import load_songs


@pytest.fixture
def songs():
    return load_songs("data/songs.csv")


@pytest.fixture
def preferences():
    return {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.90,
        "valence": 0.90,
        "tempo_bpm": 130,
        "danceability": 0.90,
        "acousticness": 0.10
    }


def test_strong_match_has_high_quality_score(songs, preferences):
    result = evaluate_recommendation(preferences, songs[0])

    assert result["quality_score"] >= 60
    assert result["warning"] is False


def test_weak_match_triggers_warning(songs, preferences):
    result = evaluate_recommendation(preferences, songs[14])

    assert result["quality_score"] < 60
    assert result["warning"] is True


def test_quality_score_is_between_zero_and_100(songs, preferences):
    result = evaluate_recommendation(preferences, songs[0])

    assert 0 <= result["quality_score"] <= 100


def test_invalid_energy_is_rejected(songs, preferences):
    preferences["energy"] = 1.5

    with pytest.raises(ValueError):
        evaluate_recommendation(preferences, songs[0])


def test_invalid_threshold_is_rejected(songs, preferences):
    with pytest.raises(ValueError):
        evaluate_recommendation(preferences, songs[0], threshold=150)
