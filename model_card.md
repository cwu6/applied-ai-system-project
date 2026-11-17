## Limitation and Biases
VibeFinder 2.0 has several limitations and biases. For instance, the system currently uses only 18 songs, which limits the variety of music that can be recommended and some genres have fewer songs than others, causing some genres to appear less. It also uses  set scoring weights for each song feature, which may not reflect every user's preferences. In addition, this system compares features such as genre, mood, energy, and tempo but does not take into account an individual's deeper connection to a song, such as through their listening history. Because recommendations depend on the given dataset and scoring rules, songs that fit the system's preferred feature combinations may rank higher than songs a user actually enjoy.

---

## AI Misuses and Prevention
VibeFinder 2.0 is created to help users discover new music they may enjoy, but its recommendations could be misunderstood as something guaranteed of what someone will enjoy. Users might also assume that a high matching score means a song is objectively better, even though the score only represents how closely its features match their preferences. To prevent this, the system provides explanations and matching percentages so that the users can understand why songs are recommended. It also displays warnings for recommendations below 60%. Furthermore, users should treat the recommendations as suggestions rather than definitive answers for their music taste. Being transparent about my system's limited dataset and scoring approach ensures that users understand how recommendations are generated and the realisiticness of the results.

---

## Surprises During AI Reliability Testing
One thing that surprised me was that some songs appeared in multiple recommendation lists. For example, Gym Hero appeared in several different profiles because its music features matched different combinations of user preferences. I was also surprised that Focus Flow ranked first for the Conflicting Preferences profile, even though the profile had preferences that were difficult to match together. Its matching score was only 56.29%, which gave it the weak match warning. This showed me that a song can rank first out of the given options without necessarily being a strong match. It also helped me understand why having a separate evaluator is important. It is importnat because ranking alone does not always show how well a recommendation matches the user's preferences.

---

## AI Colloboration
I used AI throughout this project to assist in developing the recommendation evaluator, improve the reliability features, debug code, and write tests. I used its suggestions as guidance, but I also ran the code and tests myself to check that the changes worked. One AI suggestion I accepted was to create a separate reliability evaluator that calculates a matching percentage for each recommendation. I also added a 60% threshold for weak match warnings, logging, and automated tests. I chose this because it gave me a way to evaluate the recommendations beyond just their original ranking scores. On the other hand, one AI suggestion I changed was adding more advanced reliability measurements to the project. However, I decided to keep the evaluation system simpler by using matching percentages, a 60% warning threshold, input validation, logging, and automated tests. I chose this way because these features were enough for my recommendation system without adding unnecessary complex elements or making the project harder to understand.

---


