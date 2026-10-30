import random
import time
from dataclasses import dataclass, field
from tkinter import Tk, Label, Button, Listbox, StringVar, Scrollbar, Frame, END


@dataclass
class Bird:
    name: str
    species: str
    color: str
    sound: str
    habitat: str
    fact: str
    ascii_frames: list[str] = field(default_factory=list)

    def display(self):
        print(f"\n{self.name} the {self.species}")
        print(f"Color: {self.color}")
        print(f"Habitat: {self.habitat}")
        print(f"Sound: {self.sound}")
        print(f"Fun fact: {self.fact}")
        self.animate()

    def animate(self, repeats: int = 2):
        for _ in range(repeats):
            for frame in self.ascii_frames:
                print(frame)
                time.sleep(0.15)
                print("\033[H\033[J", end="")


BIRDS = [
    Bird(
        name="Sunny",
        species="Robin",
        color="Red breast",
        sound="Cheerily!",
        habitat="Backyards and forests",
        fact="Robins are known for listening for worms beneath the soil.",
        ascii_frames=[
            """      __\n     (o )\n    /|\\\\  \n    / \\\n___/_  \\___\n""",
            """      __\n     (o )\n    /|\\\\  \n   / \\\n___/  \\___\n""",
            """      __\n     (o )\n    /|\\\\  \n    / \\\n___/_  \\___\n""",
        ],
    ),
    Bird(
        name="Sky",
        species="Blue Jay",
        color="Blue and white",
        sound="Jay! Jay!",
        habitat="Woodlands and parks",
        fact="Blue jays can mimic hawks and other birds to scare predators.",
        ascii_frames=[
            """      __\n   __(o)\n  /|\\\\   \n  / \\\n  /  \\\n___/____\\___\n""",
            """      __\n   __(o)\n  /|\\\\   \n  / \\\n  /  \\\n___/____\\___\n""",
            """      __\n   __(o)\n  /|\\\\   \n  / \\\n  /  \\\n___/____\\___\n""",
        ],
    ),
    Bird(
        name="Misty",
        species="Owl",
        color="Brown and gold",
        sound="Hoo hoo!",
        habitat="Forests and quiet tree hollows",
        fact="Owls can rotate their heads almost a full circle.",
        ascii_frames=[
            """      ___\n   .-" "-.\n  / 0 0 \\\n  |  ^  |\n  |  _  |\n   `-._.-'\n""",
            """      ___\n   .-" "-.\n  / 0 0 \\\n  |  ^  |\n  |  _  |\n   `-._.-'\n""",
            """      ___\n   .-" "-.\n  / 0 0 \\\n  |  ^  |\n  |  _  |\n   `-._.-'\n""",
        ],
    ),
    Bird(
        name="Pip",
        species="Sparrow",
        color="Brown and gray",
        sound="Chirp chirp!",
        habitat="Urban gardens and grasslands",
        fact="Sparrows are social birds and often travel in flocks.",
        ascii_frames=[
            """     __\n   (o )\n  /|\\\\  \n  / \\\n   /  \\\n___/____\\___\n""",
            """     __\n   (o )\n  /|\\\\  \n  / \\\n   /  \\\n___/____\\___\n""",
            """     __\n   (o )\n  /|\\\\  \n  / \\\n   /  \\\n___/____\\___\n""",
        ],
    ),
    Bird(
        name="Luna",
        species="Hummingbird",
        color="Green and iridescent",
        sound="Buzz!",
        habitat="Flower gardens and forests",
        fact="Hummingbirds can flap their wings more than 50 times per second.",
        ascii_frames=[
            """    .-""-.\n   / 0 0 \\\n  |  ^  |\n   `-._.-'\n""",
            """    .-""-.\n   / 0 0 \\\n  |  ^  |\n   `-._.-'\n""",
            """    .-""-.\n   / 0 0 \\\n  |  ^  |\n   `-._.-'\n""",
        ],
    ),
    Bird(
        name="Dart",
        species="Falcon",
        color="Brown and cream",
        sound="Kreeee!",
        habitat="Mountains and open skies",
        fact="Falcons are among the fastest animals in the world.",
        ascii_frames=[
            """       __\n   ___/  \\\n  / o  o \\\n  \\  ^  /\n   `-._.-'\n  /| |\\\n""",
            """       __\n   ___/  \\\n  / o  o \\\n  \\  ^  /\n   `-._.-'\n  /| |\\\n""",
            """       __\n   ___/  \\\n  / o  o \\\n  \\  ^  /\n   `-._.-'\n  /| |\\\n""",
        ],
    ),
    Bird(
        name="Wren",
        species="Wren",
        color="Warm brown",
        sound="Tweedle-dee!",
        habitat="Shrubbery and woodland edges",
        fact="Wrens are tiny but incredibly energetic and territorial.",
        ascii_frames=[
            """      __\n   __( )\n  /| \\ \\  \n  / \\\n  /  \\\n___/____\\___\n""",
            """      __\n   __( )\n  /| \\ \\  \n  / \\\n  /  \\\n___/____\\___\n""",
            """      __\n   __( )\n  /| \\ \\  \n  / \\\n  /  \\\n___/____\\___\n""",
        ],
    ),
    Bird(
        name="Flora",
        species="Peacock",
        color="Blue and green",
        sound="Aaaah!",
        habitat="Forests and gardens",
        fact="Peacocks display their feathers to attract mates and impress others.",
        ascii_frames=[
            """  ___\n (o o)\n /| |\\\n /| |\\\n  / \\\n   / \\\n""",
            """  ___\n (o o)\n /| |\\\n /| |\\\n  / \\\n   / \\\n""",
            """  ___\n (o o)\n /| |\\\n /| |\\\n  / \\\n   / \\\n""",
        ],
    ),
]


def show_bird_menu():
    print("\n=== Bird Explorer ===")
    for index, bird in enumerate(BIRDS, start=1):
        print(f"{index}. {bird.name} the {bird.species}")
    print("0. Back")


def show_all_birds():
    for bird in BIRDS:
        bird.display()


def quiz_round():
    score = 0
    total = 3
    print("\n=== Bird Quiz ===")

    for _ in range(total):
        bird = random.choice(BIRDS)
        options = [bird.species]
        while len(options) < 4:
            candidate = random.choice(BIRDS).species
            if candidate not in options:
                options.append(candidate)
        random.shuffle(options)

        print(f"\nWhich species is {bird.name}?")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        answer = input("Your answer (number): ").strip()
        try:
            choice_index = int(answer) - 1
            selected = options[choice_index]
        except (ValueError, IndexError):
            print("Invalid choice. No points awarded.")
            continue

        if selected == bird.species:
            print("Correct! Great job.")
            score += 1
        else:
            print(f"Not quite. The correct answer was {bird.species}.")

    print(f"\nFinal score: {score}/{total}")
    if score == total:
        print("Amazing! You know your birds!")
    elif score >= 2:
        print("Nice work! You are a bird expert in training.")
    else:
        print("Keep practicing — the birds will be waiting.")


def bird_cli():
    while True:
        print("\n=== Bird App Menu ===")
        print("1. Explore birds")
        print("2. Bird quiz")
        print("3. Animated bird preview")
        print("4. Open simple GUI")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_bird_menu()
            bird_choice = input("Pick a bird number: ").strip()
            try:
                selected = BIRDS[int(bird_choice) - 1]
                selected.display()
            except (ValueError, IndexError):
                print("That was not a valid bird selection.")
        elif choice == "2":
            quiz_round()
        elif choice == "3":
            bird = random.choice(BIRDS)
            print(f"\nPreviewing: {bird.name} the {bird.species}")
            bird.display()
        elif choice == "4":
            open_gui()
        elif choice == "5":
            print("Goodbye! Thanks for visiting the birds.")
            break
        else:
            print("Please choose a valid menu option.")


class BirdGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Bird App")
        self.root.geometry("480x420")

        self.birds = BIRDS
        self.current_selection = StringVar()

        left = Frame(root)
        left.pack(side="left", fill="y", padx=10, pady=10)

        Label(left, text="Birds", font=("Arial", 12, "bold")).pack()
        self.listbox = Listbox(left, width=25, height=15)
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
            wraplength=220,
        )
        self.info.pack(anchor="w", pady=10)

        self.random_btn = Button(root, text="Random Bird", command=self.random_bird)
        self.random_btn.pack(side="bottom", pady=12)

    def show_selected_bird(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        bird = self.birds[selection[0]]
        self.info.config(
            text=(
                f"Name: {bird.name}\n"
                f"Species: {bird.species}\n"
                f"Color: {bird.color}\n"
                f"Habitat: {bird.habitat}\n"
                f"Sound: {bird.sound}\n"
                f"Fact: {bird.fact}"
            )
        )

    def random_bird(self):
        bird = random.choice(self.birds)
        self.listbox.selection_clear(0, END)
        index = self.birds.index(bird)
        self.listbox.selection_set(index)
        self.show_selected_bird(None)


def open_gui():
    root = Tk()
    app = BirdGui(root)
    root.mainloop()


if __name__ == "__main__":
    bird_cli()


# Future idea: you could also refactor this into separate files for CLI, quiz, and GUI.
# For now, everything is in one easy-to-learn script.
"}]}jspb to=functions.push_files ൨{