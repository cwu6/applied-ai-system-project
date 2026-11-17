## Reliability and Evaluation
VibeFinder 2.0 uses automated testing, matching scoring, input validation, and logging to evaluate the reliability of its recommendations

- Automated Testing
I tested the project using: python -m pytest
The project has 7 automated tests and all 7 passed. The tests check:
- Whether the original recommendation system correctly loads songs and generates recommendations
- Whether strong recommendations receive high match quality scores
- Whether weak recommendations receive lower match quality scores (threshold of 60%)
- Whether matching scores stay within the expected range of 0–100%
- Whether invalid inputs, such as an energy value that is out of the range, are handled correctly

- Matching Scoring:
The evaluator calculates a matching percentage from 0–100% based on how closely a recommended song matches the user's preferences across seven features: genre, mood, energy, tempo, valence, danceability, and acousticness.

- Weak Match Warnings:
VibeFinder 2.0 uses a 60% threshold. Recommendations below 60% received a warning  that said that it may be a weak match. This helps users recognize when a song does not closely fit their preferences.

- Input Validation and Logging:
The evaluator checks user inputs and rejects invalid values, such as numerical preferences that may be out of the range or threshold. It also records successful evaluations in a log file, allowing evaluation results to be reviewed later on.

- Summary:
All 7 automated tests passed. The tests confirmed that the recommender and evaluator work for the tested cases, including strong matches, weak matches, and invalid inputs. Matching scoring and the 60% warning threshold provided an additional way to seek out the recommendations that may not fit a user's preferences. Furthermore, logging provides a record of the successful evaluations.

---