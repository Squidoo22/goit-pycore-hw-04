import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def print_directory_item(item, indent):
    if item.is_dir():
        print(" " * indent + Fore.CYAN + f"📁 {item.name}/")
    elif item.is_file():
        print(" " * indent + Fore.GREEN + f"📄 {item.name}")


def display_directory_structure(directory_path, indent=0):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Шлях '{directory_path}' не існує або не є директорією.")
        return

    print(" " * indent + Fore.BLUE + f"📁 {path.name}/")

    for item in path.iterdir():
        print_directory_item(item, indent + 2)
        if item.is_dir():
            display_directory_structure(item, indent + 4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Потрібно вказати шлях до директорії.")
        sys.exit(1)

    display_directory_structure(sys.argv[1])
