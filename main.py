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
        "Robins are famous for hopping and listening for worms under the soil.",
        """           __
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
        """,
    ),
    Bird(
        "Sky",
        "Blue Jay",
        "Blue and white",
        "Jay! Jay!",
        "Woodlands and parks",
        "Blue jays can copy the calls of hawks and other birds to scare away trouble.",
        """         ___
      .-"   "-.
     /  .-. . \\
     |  | | | |
     |  '-' '-'|
      '.___.'
         / \\
        /   \\
       /____\\
        """,
    ),
    Bird(
        "Misty",
        "Owl",
        "Brown and gold",
        "Hoo hoo!",
        "Forests and quiet groves",
        "Owls can rotate their heads in a nearly full circle.",
        """       ___
     .-"   "-.
    /  o o  \\
    |  ^  ^  |
    |  \_/  |
     '.___.'
      / \\
     /   \\
    """,
    ),
    Bird(
        "Pip",
        "Sparrow",
        "Brown and gray",
        "Chirp chirp!",
        "Urban gardens and grasslands",
        "Sparrows are tiny but full of energy and often travel in groups.",
        """         __
       (o )
      /|\\\\
      / \\\n     /   \\
     \\___/ 
        """,
    ),
    Bird(
        "Luna",
        "Hummingbird",
        "Green and iridescent",
        "Buzz!",
        "Flower gardens",
        "Hummingbirds can flap their wings so quickly they seem to hover in place.",
        """      .-""-. 
     .'  _  '.
    /  ( )  \\
    |  .-.  |
     '.___.'
        """,
    ),
    Bird(
        "Dart",
        "Falcon",
        "Brown and cream",
        "Kreeee!",
        "Open skies and cliffs",
        "Falcons are among the fastest animals on Earth.",
        """       __
     __/  \\
   / o  o \\
   \\  ^  /
    `-._.-'
       /|\\
        """,
    ),
    Bird(
        "Wren",
        "Wren",
        "Warm brown",
        "Tweedle-dee!",
        "Shrubbery and wood edges",
        "Wrens are small, noisy, and surprisingly bold for their size.",
        """       ___
     .-( )-.
    /  .-.  \\
    |  | |  |
     '.___.'
        """,
    ),
    Bird(
        "Flora",
        "Peacock",
        "Blue and green",
        "Aaaah!",
        "Gardens and open forests",
        "Peacocks fan their colorful tails to attract a mate.",
        """       __
     .-"  "-.
    /  o o  \\
    |  .-.  |
    |  `-'  |
     '.___.'
        """,
    ),
]


def print_header(title):
    print(f"\n=== {title} ===")


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
        print("\n" + bird.art)
        time.sleep(0.3)
        print("\033[H\033[J", end="")


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


def show_result(score, total, challenge_name):
    print(f"\n{challenge_name} score: {score}/{total}")
    if score == total:
        print("Perfect score! You are a true bird champion!")
    elif score >= total * 0.7:
        print("You won! Great job — your bird instincts are strong.")
    else:
        print("You lost this round, but the birds still admire your curiosity.")


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

    show_result(score, total_rounds, "Bird Quiz")


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

    show_result(score, total_rounds, "Bird Match Challenge")


def bird_cli():
    while True:
        print_header("Bird App Deluxe")
        print("1. Explore birds")
        print("2. Bird quiz")
        print("3. Bird match challenge")
        print("4. Open bird GUI")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            bird_explorer()
        elif choice == "2":
            bird_quiz()
        elif choice == "3":
            bird_match_challenge()
        elif choice == "4":
            open_gui()
        elif choice == "5":
            print("Thanks for visiting the birds. Fly safe!")
            break
        else:
            print("Please choose a valid menu option.")


class BirdAppGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Bird App Deluxe")
        self.root.geometry("700x520")

        self.birds = BIRD_LIBRARY

        left = Frame(root)
        left.pack(side="left", fill="y", padx=10, pady=10)

        Label(left, text="Birds", font=("Arial", 12, "bold")).pack(pady=(0, 8))
        self.listbox = Listbox(left, width=24, height=18)
        for bird in self.birds:
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
            wraplength=320,
        )
        self.info.pack(anchor="w", padx=3, pady=8)

        self.random_btn = Button(root, text="Random Bird", command=self.random_bird)
        self.random_btn.pack(side="bottom", pady=10)

    def show_selected_bird(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return

        bird = self.birds[selection[0]]
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
        bird = random.choice(self.birds)
        self.listbox.selection_clear(0, END)
        idx = self.birds.index(bird)
        self.listbox.selection_set(idx)
        self.show_selected_bird(None)


def open_gui():
    root = Tk()
    app = BirdAppGui(root)
    root.mainloop()


if __name__ == "__main__":
    bird_cli()

# A refined bird app with a CLI, quiz system, challenge mode, and a lightweight GUI.
# This version is built to be easy to extend with more birds or richer visual effects.


"}]} ivoq to=functions.push_files ൨{