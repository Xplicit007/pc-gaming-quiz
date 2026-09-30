# PC Gaming Quiz
# A simple multiple-choice quiz about popular PC games.

questions = (
    "In Elden Ring, which boss is famously fought on horseback in a massive open battlefield?",
    "In Valorant, which agent can place a 'Turret' that automatically attacks enemies?",
    "In Cyberpunk 2077, what is the name of V's digital companion?",
    "In Minecraft, which dimension contains End Cities?",
    "In Red Dead Redemption 2, what is the name of Arthur Morgan's gang?",
    "In Counter-Strike 2, what does the 'CT' side stand for?",
    "In The Witcher 3, what is Geralt's horse named?",
    "In Wuthering Waves, what is the main character commonly called?",
    "In Baldur's Gate 3, which class is associated with the ability to rage?",
    "In Clair Obscur: Expedition 33, what number is associated with the Expedition?"
)

options = (
    ("A. Margit", "B. Radahn", "C. Godrick", "D. Morgott"),
    ("A. Killjoy", "B. Cypher", "C. Sage", "D. Viper"),
    ("A. Johnny Silverhand", "B. Jackie Welles", "C. Viktor Vektor", "D. Adam Smasher"),
    ("A. Nether", "B. Aether", "C. End", "D. Deep Dark"),
    ("A. The Van der Linde Gang", "B. The O'Driscoll Gang", "C. The Lemoyne Raiders", "D. The Murfree Brood"),
    ("A. Counter Terrorists", "B. Combat Team", "C. Central Terrorists", "D. Counter Troopers"),
    ("A. Roach", "B. Shadowmere", "C. Torrent", "D. Dandelion"),
    ("A. Rover", "B. Wanderer", "C. Traveler", "D. Drifter"),
    ("A. Barbarian", "B. Paladin", "C. Bard", "D. Warlock"),
    ("A. 13", "B. 27", "C. 33", "D. 42")
)

answers = (
    "B",
    "A",
    "A",
    "C",
    "A",
    "A",
    "A",
    "A",
    "A",
    "C"
)
guesses = []
score = 0
question_num = 0

for x in questions:
    print("--------------------")
    print(x)
    for y in options[question_num]:
        print(y)
    guess = input("Your answer(q to quit): ").upper()
    if guess == "Q":
        print("--------------------")
        print("Have a nice day!")
        print("--------------------")
        exit()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer!")
        print(f"Correect answer: {answers[question_num]}")
    question_num += 1

print()
print("--------------------")
print(f"Your final score = {score}/len(questions)")
print(f"accuracy: {(score * 100)/len(questions)}")
print("--------------------")

