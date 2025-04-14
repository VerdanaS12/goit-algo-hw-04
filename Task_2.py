def get_cats_info(path):
    try:
        cats_list = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats_list.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
        return cats_list
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return []
    

cats_info = get_cats_info("cats.txt")
print(cats_info)