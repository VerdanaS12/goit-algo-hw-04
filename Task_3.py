import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def explore_directory(path: Path, level: int = 0):
    try:
        for item in sorted(path.iterdir()):
            indent = '  ' * level
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                explore_directory(item, level + 1)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{Fore.RED}Доступ заборонено: {path}")

def main():
    if len(sys.argv) < 2:
        print("❌ Помилка: не вказано шлях до директорії.")
        print("Синтаксис: python hw03.py /шлях/до/директорії")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"❌ Шлях не існує: {directory_path}")
        return

    if not directory_path.is_dir():
        print(f"❌ Це не директорія: {directory_path}")
        return

    print(f"{Fore.CYAN}Структура директорії: {directory_path}\n")
    explore_directory(directory_path)

if __name__ == "__main__":
    main()
