# 🎵 VibeFinder 2.0 - Music Recommendation System

## Project Summary

VibeFinder 2.0 is a music recommendation system that suggest songs based on a user's music preferences. Users can choose their preferred genre, mood, energy, positivity, tempo, danceability, acousticness. They system then ranks songs using a content-based scoring algorithm and evaluates each recommendation with a separate matching score that shows how well the song matches the user's preference, along with explanations for each suggestion. This project matters because it demonstrates how recommendation systems can personalize music discovery by analyzing multiple user preferences rather than just relying on genre alone.

My original project, Music Recommender Simulation, was a command line music recommender that used user preferences and specific song characteristics to create recommendations. It compared seven features, each with a calculated weighted score for each song, and displayed the top five songs with explanations. This project extends my original Modules 1-3 project by adding a Streamlit web interface, a reliabilty evaluator, user input validation, logging, and automated tests. Adding these new elements makes the recommender easier for the user to use and provides an additonal way to identify recommendations that may not closely match a user's preference.

---

## Architecture Overview
- User Interface: Users enter their music preferences through the Streamlit app or command line interface
- Song Loader: The system reads song information from data/song.csv
- Recommendation Engine: The recommender compares each song with the user's preferences and ranks song uisng a weighted scoring algorithm
- Reliability Evaluator: Each recommendatio recieves a separate matching score from 0-100%. If the recommendation recieves below 60%, it will recieve a weak match warning
- Logging: The evaluation results are recorded in vibefinder.log
- Automated Tests: Tests check the recommendation and evaluation componenets, including inputs that are invalid
- The mermaid source diagram is avaliable in diagrams/architecture.mmd
- Users can review their results and change their preferences accordingly

---

## Setup Instructions

1. Clone the repository:
git clone https://github.com/cwu6/applied-ai-system-project.git
cd applied-ai-system-project

2. Create and activate a virtual environment
Mac:
python3 -m venv .venv
source .venv/bin/activate

Windows:
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the command-line application
python -m src.main

5. Run the Streamlit application
streamlit run src/app.py

6. Run the automated tests
python -m pytest

---

## Sample Interactions
The example show different user preferences. The recommendation score is out of 9, while the matching score is a separate percentage calculated by the evaluator.

Example 1: High Energy Pop
- Input:
Genre: pop
Mood: happy
Energy: 0.90
Valence: 0.90
Tempo: 130 BPM
Danceability: 0.90
Acousticness: 0.10

- Command:
python -m src.main

- Output:
High-Energy Pop

1. Sunrise City - Neon Echo
   Recommendation Score: 8.57/9.00
   Matching Score: 94.43%

2. Gym Hero - Max Pulse
   Recommendation Score: 7.25/9.00
   Matching Score: 82.29%

3. Golden Horizon - Sol Mariposa
   Recommendation Score: 6.83/9.00
   Matching Score: 83.71%

4. Rooftop Lights - Indigo Parade
   Recommendation Score: 6.34/9.00
   Matching Score: 77.29%

5. Afterglow Avenue - Noah Blue
   Recommendation Score: 5.20/9.00
   Matching Score: 67.86%


Example 2: Chill Lofi
- Input: 
Genre: lofi
Mood: chill
Energy: 0.40
Valence: 0.60
Tempo: 80 BPM
Danceability: 0.60
Acousticness: 0.75

- Command:
python -m src.main

- Output:
Chill Lofi

1. Midnight Coding - LoRoom
   Recommendation Score: 8.86/9.00
   Matching Score: 98.14%

2. Library Rain - Paper Lanterns
   Recommendation Score: 8.76/9.00
   Matching Score: 96.86%

3. Focus Flow - LoRoom
   Recommendation Score: 7.46/9.00
   Matching Score: 85.14%

4. Spacewalk Thoughts - Orbit Bloom
   Recommendation Score: 6.31/9.00
   Matching Score: 76.71%

5. Autumn Letters - Willow Creek
   Recommendation Score: 5.22/9.00
   Matching Score: 68.00%

Example 3: Conflicting Preferences. This specific example shows the role of the reliability evaluator. All five recommendations are ranked, but each recieves a weak match warning because the matching score is below 60%.
- Input:
Genre: lofi
Mood: intense
Energy: 0.95
Valence: 0.10
Tempo: 150 BPM
Danceability: 0.10
Acousticness: 0.95

- Command:
python -m src.main

- Output:
Conflicting Preferences

1. Focus Flow - LoRoom
   Recommendation Score: 5.16/9.00
   Matching Score: 56.29%
   Evaluation: Weak match

2. Storm Runner - Voltline
   Recommendation Score: 5.14/9.00
   Matching Score: 59.43%
   Evaluation: Weak match

3. Library Rain - Paper Lanterns
   Recommendation Score: 5.14/9.00
   Matching Score: 56.29%
   Evaluation: Weak match

4. Midnight Coding - LoRoom
   Recommendation Score: 5.12/9.00
   Matching Score: 55.57%
   Evaluation: Weak match

5. Gym Hero - Max Pulse
   Recommendation Score: 4.53/9.00
   Matching Score: 50.57%
   Evaluation: Weak match

---

## Design Decisions
- Content-based recommendations: I kept the original scoring method because it makes recommendations more understandable through user preferences and song features.
- Separate evaluator: I added a separate matching evaluator instead of changing the original recommendation ranking. This allows the system to identify weak recommendations without changing their ranking.
- Streamlit interface: I added a web interface with dropdowns and sliders to make the system easier to use.
- Logging and validation: I added logging and input validation to make the system easier to test and fix any issues there may be.
- Trade-offs: I kept the already existing dataset of the 18 songs rather than adding a much larger collection of songs. This made the project easier to manage and test, but it also limits the variety of songs available and may cause users with different music preferences to receive similar recommendations. I also kept the scoring weights fixed instead of allowing the system to adjust them for each individual user. This makes the recommendation process more consistent because the same preferences will produce the same scoring results. However, it limits personalization since the system cannot learn which features matter most to different users. Overall, I prioritized keeping the system simple and understandable rather than building a more complex recommendation model that would required more data and complex elements.

---

## Testing Summary
What Worked:
- The system was able to load song information from the CSV dataset and convert numerical values into the correct data types
- The recommendation algorithm was able to compare user preferences against song features and calculate weighted match scores
- Songs were ranked based on their scores, with the highest scoring recommendations appearing first
- The system was able to generate explanations describing why particular songs were recommended
-The automated tests passed, confirming that the recommendation functionality behaved as expected
- The system handled different preference profiles, including high-energy pop, chill lofi, and intense rock, and produced different recommendations depending on the selected preferences

What Didn't Work as Expected / Limitations:
- The small dataset sometimes limited the variety of recommendations available, especially for less common genres or a combination of preferences
- Fixed scoring weights meant that some preferences could influence recommendations more than others, even when users might value the specific features differently
- When users entered conflicting preferences, the system could still generate recommendations, but the resulting matching scores were usually lower because fewer songs matched the preferences
- The recommendation system could only evaluate the song features included in the dataset and could not account for factors such as listening history or likes

What I Learned:
Through testing, I learned how different song features can influence recommendation results and how changing scoring weights can affect the ranking of songs. I also learned the importance of testing different user preference profiles rather than only checking whether the program runs successfully. For instance, when testing the High-Energy Pop and Chill Lofi user profiles, I noticed that the system recommended different songs because each profile prioritized different characteristics, such as energy level, tempo, and mood. I also learned that when users have conflicting preferences, such as wanting both high energy and high acousticness, it can be harder for the system to find songs that match all their preferences, which results in lower match scores. Moreover, testing different scenarios helped me look for limitations in the dataset and scoring method and showed me why explanations and consistent results are significant when creating a recommendation system.

---

## Reflection
This project taught me that assistance with AI is more than simply giving a computer information and expecting it to give you the right answer. I learned that AI can use data, patterns, and different instructions to make decisions and generate results. Through VibeFinder 1.0 and VibeFinder 2.0, I gained a better understanding of how recommendation systems use information about user preferences to determine which results are most relevant. I also learned that AI decisions are influenced by the information and rules that I gave to guide it. AI does not automatically produce perfect results. Its effectiveness depends on the type of data it receives and the quality of it and how well it addresses these problem. Additionally, testing different inputs and examining the results helped me understand the importance of questioning AI outputs rather than assuming they are always correct. Overall, this project gave me a better understanding of how AI can be applied to real world problems and scenarios, how data influences AI decisions, and why individual thinking is still important when developing with AI.
---

