def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        result_total_salary = 0
        num_developers = 0

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 2:
                raise ValueError(f"Помилка: Неправильний формат даних '{line.strip()}'")
            try:
                salary = int(parts[1])
                result_total_salary += salary
                num_developers += 1
            except ValueError:
                raise ValueError(f"Помилка: Неправильний формат заробітної плати '{line.strip()}'")

        if num_developers > 0:
            average_salary = result_total_salary / num_developers
            return result_total_salary, average_salary
        else:
            raise ValueError("Помилка: Немає даних про заробітні плати розробників у файлі.")

    except FileNotFoundError as e:
        raise FileNotFoundError("Помилка: Файл не знайдено.") from e


try:
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except (ValueError, FileNotFoundError) as e:
    print(e)
