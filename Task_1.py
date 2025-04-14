from pathlib import Path

def total_salary(path):
    try:
        salaries = []  
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                
                name_salary = line.strip().split(',')
                if len(name_salary) == 2:
                    name, salary = name_salary
                    salaries.append(float(salary))  

        total = sum(salaries)  
        average = total / len(salaries) if salaries else 0  
        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0

    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return 0, 0
    

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")