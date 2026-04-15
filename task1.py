def total_salary(path: str):
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                try:
                    name, salary_str = line.split(",")
                    salary = float(salary_str)
                except ValueError:
                    # якщо рядок пошкоджений або не містить зарплату
                    print(f"Помилка у рядку: {line}")
                    continue

                total += salary
                count += 1

        if count == 0:
            return 0, 0  # якщо файл порожній або всі рядки некоректні

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
