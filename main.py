# Bird App

A simple Python program for exploring different kinds of birds.

from dataclasses import dataclass


@dataclass
class Bird:
    name: str
    species: str
    color: str
    sound: str
    habitat: str
    fact: str

    def display(self):
        print(f"\n{self.name} the {self.species}")
        print(f"Color: {self.color}")
        print(f"Habitat: {self.habitat}")
        print(f"Sound: {self.sound}")
        print(f"Fun fact: {self.fact}")
        print(self.ascii_art())

    def ascii_art(self):
        return """
             __
           (o  )
          /|\\  
          / \\\n        _/   \\_
       (______) 
        """


BIRDS = [
    Bird(
        name="Sunny",
        species="Robin",
        color="Red breast",
        sound="Cheerily!",
        habitat="Backyards and forests",
        fact="Robins are known for hopping across lawns and listening for worms."
    ),
    Bird(
        name="Sky",
        species="Blue Jay",
        color="Blue and white",
        sound="Jay! Jay!",
        habitat="Woodlands and parks",
        fact="Blue jays are very intelligent and can mimic other bird calls."
    ),
    Bird(
        name="Misty",
        species="Owl",
        color="Brown and gold",
        sound="Hoo hoo!",
        habitat="Forests and quiet tree hollows",
        fact="Owls can turn their heads almost all the way around."
    ),
]


def show_menu():
    print("\n=== Bird App ===")
    print("Choose a bird to learn about:")
    for index, bird in enumerate(BIRDS, start=1):
        print(f"{index}. {bird.name} the {bird.species}")
    print("0. Exit")


def main():
    print("Welcome to the Bird App!")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Goodbye! Thanks for visiting the birds.")
            break

        try:
            selected = BIRDS[int(choice) - 1]
            selected.display()
        except (ValueError, IndexError):
            print("That is not a valid bird choice. Please try again.")


if __name__ == "__main__":
    main()
