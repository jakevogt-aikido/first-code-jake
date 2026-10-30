import random
import time
from dataclasses import dataclass
from tkinter import END, Button, Frame, Label, Listbox, Tk


@dataclass
class Bird:
    name: str
    species: str
    color: str
    sound: str
    habitat: str
    fact: str
    art: str


BIRD_LIBRARY = [
    Bird(
        "Sunny",
        "Robin",
        "Red breast",
        "Cheerily!",
        "Backyards and gardens",
        "Robins hop across lawns and listen for worms under the soil.",
        '''           __
        .-"""-.   
      .'  _  '.
     /   ( )  \\
     |  .-.-. |
      '.___.'
         ||
         ||
      .-'''-. 
     /  _ _  \\
    |  ( ) (  |
     '.___.'
        ''',
    ),
    Bird(
        "Sky",
        "Blue Jay",
        "Blue and white",
        "Jay! Jay!",
        "Woodlands and parks",
        "Blue jays can mimic hawks and other birds to scare away trouble.",
        '''         ___
      .-"   "-.
     /  .-. . \\
     |  | | | |
     |  '-' '-'|
      '.___.'
         / \\
        /   \\
       /____\\
        ''',
    ),
    Bird(
        "Misty",
        "Owl",
        "Brown and gold",
        "Hoo hoo!",
        "Forests and quiet groves",
        "Owls can rotate their heads in a nearly full circle.",
        '''       ___
     .-"   "-.
    /  o o  \\
    |  ^  ^  |
    |  \\_/  |
     '.___.'
      / \\
     /   \\
    ''',
    ),
    Bird(
        "Pip",
        "Sparrow",
        "Brown and gray",
        "Chirp chirp!",
        "Urban gardens and grasslands",
        "Sparrows are tiny but full of energy and often travel in groups.",
        '''         __
        (o )
       /|\\\\
       / \\
      /   \\
      \\___/ 
        ''',
    ),
    Bird(
        "Luna",
        "Hummingbird",
        "Green and iridescent",
        "Buzz!",
        "Flower gardens",
        "Hummingbirds can flap their wings so quickly they seem to hover in place.",
        '''      .-""-. 
     .'  _  '.
    /  ( )  \\
    |  .-.  |
     '.___.'
        ''',
    ),
    Bird(
        "Dart",
        "Falcon",
        "Brown and cream",
        "Kreeee!",
        "Open skies and cliffs",
        "Falcons are among the fastest animals on Earth.",
        '''       __
     __/  \\
   / o  o \\
   \\  ^  /
    `-._.-'
       /|\\
        ''',
    ),
    Bird(
        "Wren",
        "Wren",
        "Warm brown",
        "Tweedle-dee!",
        "Shrubbery and wood edges",
        "Wrens are small, noisy, and surprisingly bold for their size.",
        '''       ___
     .-( )-.
    /  .-.  \\
    |  | |  |
     '.___.'
        ''',
    ),
    Bird(
        "Flora",
        "Peacock",
        "Blue and green",
        "Aaaah!",
        "Gardens and open forests",
        "Peacocks fan their colorful tails to attract a mate.",
        '''       __
     .-"  "-.
    /  o o  \\
    |  .-.  |
    |  `-'  |
     '.___.'
        ''',
    ),
]


def clear_screen():
    print("\033[H\033[J", end="")


def print_header(title):
    print(f"\n{'=' * 30}")
    print(title)
    print(f"{'=' * 30}")


def show_bird_profile(bird):
    print(bird.art)
    print(f"Name: {bird.name}")
    print(f"Species: {bird.species}")
    print(f"Color: {bird.color}")
    print(f"Sound: {bird.sound}")
    print(f"Habitat: {bird.habitat}")
    print(f"Fact: {bird.fact}")


def animate_bird_preview(bird, loops=2):
    for _ in range(loops):
        clear_screen()
        print(bird.art)
        time.sleep(0.25)


def bird_explorer():
    while True:
        print_header("Bird Explorer")
        for index, bird in enumerate(BIRD_LIBRARY, start=1):
            print(f"{index}. {bird.name} the {bird.species}")
        print("0. Back")

        choice = input("Choose a bird: ").strip()
        if choice == "0":
            return

        try:
            bird = BIRD_LIBRARY[int(choice) - 1]
            show_bird_profile(bird)
            animate_bird_preview(bird, loops=1)
        except (ValueError, IndexError):
            print("Please pick a valid bird number.")


def bird_quiz():
    print_header("Bird Quiz")
    total_rounds = 5
    score = 0

    for round_number in range(1, total_rounds + 1):
        bird = random.choice(BIRD_LIBRARY)
        options = [bird.species]
        while len(options) < 4:
            candidate = random.choice(BIRD_LIBRARY).species
            if candidate not in options:
                options.append(candidate)
        random.shuffle(options)

        print(f"\nRound {round_number}: Which species is {bird.name}?")
        print(bird.art)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        answer = input("Enter your choice (number): ").strip()
        try:
            selected = options[int(answer) - 1]
        except (ValueError, IndexError):
            print("Invalid input. No points awarded.")
            continue

        if selected == bird.species:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The correct answer was {bird.species}.")

    print(f"\nFinal score: {score}/{total_rounds}")
    if score == total_rounds:
        print("Perfect score! You are a bird champion!")
    elif score >= total_rounds * 0.7:
        print("Nice job! Your bird instincts are strong.")
    else:
        print("Keep practicing — the birds are waiting for you.")


def bird_match_challenge():
    print_header("Bird Match Challenge")
    total_rounds = 4
    score = 0

    for round_number in range(1, total_rounds + 1):
        bird = random.choice(BIRD_LIBRARY)
        clue = random.choice([
            f"This bird lives in {bird.habitat}.",
            f"This bird is known for its {bird.color.lower()} colors.",
            f"This bird makes a {bird.sound.lower()} sound.",
            f"Fun fact: {bird.fact}",
        ])

        print(f"\nRound {round_number}: {clue}")
        choices = [bird.name]
        while len(choices) < 4:
            candidate = random.choice(BIRD_LIBRARY).name
            if candidate not in choices:
                choices.append(candidate)
        random.shuffle(choices)

        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice}")

        answer = input("Who matches this clue? (number): ").strip()
        try:
            guessed = choices[int(answer) - 1]
        except (ValueError, IndexError):
            print("Invalid input. No points awarded.")
            continue

        if guessed == bird.name:
            print("Correct match!")
            score += 1
        else:
            print(f"Wrong answer. It was {bird.name}.")

    print(f"\nFinal score: {score}/{total_rounds}")
    if score == total_rounds:
        print("You aced the challenge!")
    elif score >= total_rounds * 0.7:
        print("You won the challenge! Great work.")
    else:
        print("You lost this round, but the birds still respect your curiosity.")


class BirdAdventureGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.max_levels = 5

    def run(self):
        print_header("Bird Adventure")
        print("Welcome to Bird Adventure!")
        print("Answer the bird questions correctly to earn points.")
        print("Take care: you have 3 lives. Lose them all and the game ends.")
        input("Press Enter to begin...\n")

        while self.level <= self.max_levels and self.lives > 0:
            bird = random.choice(BIRD_LIBRARY)
            print(f"\nLevel {self.level} | Score: {self.score} | Lives: {self.lives}")
            print(bird.art)
            print(f"Which bird is this? Choose the matching species.")

            options = [bird.species]
            while len(options) < 4:
                candidate = random.choice(BIRD_LIBRARY).species
                if candidate not in options:
                    options.append(candidate)
            random.shuffle(options)

            for index, option in enumerate(options, start=1):
                print(f"{index}. {option}")

            answer = input("Your answer (number): ").strip()
            try:
                choice = options[int(answer) - 1]
            except (ValueError, IndexError):
                print("Invalid answer. You lose a life.")
                self.lives -= 1
                continue

            if choice == bird.species:
                self.score += 10 + self.level * 5
                print("Correct! You earn points.")
                self.level += 1
            else:
                self.lives -= 1
                print(f"Not quite. The correct answer was {bird.species}.")

        if self.lives <= 0:
            print("\nGame over! The birds won this round.")
        else:
            print(f"\nYou won Bird Adventure! Final score: {self.score}")
        print("Thanks for playing!")


def bird_cli():
    while True:
        print_header("Bird App Deluxe")
        print("1. Bird Adventure Game")
        print("2. Explore birds")
        print("3. Bird quiz")
        print("4. Bird match challenge")
        print("5. Open bird GUI")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            BirdAdventureGame().run()
        elif choice == "2":
            bird_explorer()
        elif choice == "3":
            bird_quiz()
        elif choice == "4":
            bird_match_challenge()
        elif choice == "5":
            open_gui()
        elif choice == "6":
            print("Thanks for visiting the birds. Fly safe!")
            break
        else:
            print("Please choose a valid menu option.")


class BirdAppGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Bird App Deluxe")
        self.root.geometry("720x540")

        left = Frame(root)
        left.pack(side="left", fill="y", padx=10, pady=10)

        Label(left, text="Birds", font=("Arial", 12, "bold")).pack(pady=(0, 8))
        self.listbox = Listbox(left, width=24, height=18)
        for bird in BIRD_LIBRARY:
            self.listbox.insert(END, bird.name)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.show_selected_bird)

        right = Frame(root)
        right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.info = Label(
            right,
            text="Select a bird",
            justify="left",
            font=("Arial", 10),
            wraplength=350,
        )
        self.info.pack(anchor="w", padx=4, pady=8)

        Button(root, text="Random Bird", command=self.random_bird).pack(side="bottom", pady=8)

    def show_selected_bird(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return

        bird = BIRD_LIBRARY[selection[0]]
        self.info.config(
            text=(
                f"{bird.art}\n\n"
                f"Name: {bird.name}\n"
                f"Species: {bird.species}\n"
                f"Color: {bird.color}\n"
                f"Habitat: {bird.habitat}\n"
                f"Sound: {bird.sound}\n"
                f"Fun fact: {bird.fact}"
            ),
            justify="left",
            font=("Courier", 9),
            wraplength=330,
        )

    def random_bird(self):
        bird = random.choice(BIRD_LIBRARY)
        self.listbox.selection_clear(0, END)
        idx = BIRD_LIBRARY.index(bird)
        self.listbox.selection_set(idx)
        self.show_selected_bird(None)


def open_gui():
    root = Tk()
    BirdAppGui(root)
    root.mainloop()


if __name__ == "__main__":
    bird_cli()

# Bird App Deluxe: a small game-like bird experience with exploration, challenge modes,
# life-based progression, and a simple GUI for browsing your feathered friends.
