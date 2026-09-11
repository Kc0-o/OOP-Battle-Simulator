from goblin import Goblin


ARENA_NAME = "THE BASEMENT"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    goblin2= Goblin("Andrew")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} Enters the Arena from claires house with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
