from animal import Animal


def main() -> None:
    cow = Animal("Cow", "white", "my")
    cat = Animal("Cat", "black", "may")
    dog = Animal("Dog", "coffee-colored", "gav")
    print(f"{cow.name} is {cow.color}. " + cow.get_voice())
    print(f"{cat.name} is {cat.color}. " + cat.get_voice())
    print(f"{dog.name} is {dog.color}. " + dog.get_voice())


if __name__ == '__main__':
    main()
