def get_cats_info(path: str):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                try:
                    cat_id, name, age = line.split(",")
                except ValueError:
                    print(f"Некоректний рядок: {line}")
                    continue

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

        return cats

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
cats_info = get_cats_info("cats.txt")
print(cats_info)
