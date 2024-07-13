def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(",")
            try:
                cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
                cats_list.append(cat_info)
            except IndexError as e:
                raise ValueError(f"Помилка: Неправильний формат даних '{line.strip()}'") from e
    except FileNotFoundError as e:
        raise FileNotFoundError("Помилка: Файл не знайдено.") from e
    return cats_list


cats_info = get_cats_info("cats.txt")
print(cats_info)
