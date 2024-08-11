```python
import json

class SmartBudgetTracker:
    def __init__(self):
        self.budget = 0
        self.expenses = []

    def set_budget(self, amount):
        self.budget = amount
        print(f"Бюджет установлен на: {self.budget} руб.")

    def add_expense(self, name, amount):
        if amount > self.budget:
            print("Ошибка: Сумма расходов превышает установленный бюджет!")
            return
        self.expenses.append({'name': name, 'amount': amount})
        self.budget -= amount
        print(f"Расход добавлен: {name} на сумму {amount} руб. Остаток бюджета: {self.budget} руб.")

    def view_expenses(self):
        print("Список расходов:")
        for expense in self.expenses:
            print(f"- {expense['name']}: {expense['amount']} руб.")

    def remaining_budget(self):
        print(f"Остаток бюджета: {self.budget} руб.")

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            data = {
                'budget': self.budget,
                'expenses': self.expenses
            }
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл: {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.budget = data['budget']
                self.expenses = data['expenses']
            print(f"Данные загружены из файла: {filename}")
        except FileNotFoundError:
            print("Ошибка: Файл не найден!")
        except json.JSONDecodeError:
            print("Ошибка: Неверный формат данных в файле!")

def main():
    tracker = SmartBudgetTracker()
    while True:
        print("\n1. Установить бюджет")
        print("2. Добавить расход")
        print("3. Просмотреть расходы")
        print("4. Остаток бюджета")
        print("5. Сохранить данные в файл")
        print("6. Загрузить данные из файла")
        print("7. Выход")

        choice = input("Выберите опцию: ")
        
        if choice == '1':
            amount = float(input("Введите сумму бюджета: "))
            tracker.set_budget(amount)
        elif choice == '2':
            name = input("Введите название расхода: ")
            amount = float(input("Введите сумму расхода: "))
            tracker.add_expense(name, amount)
        elif choice == '3':
            tracker.view_expenses()
        elif choice == '4':
            tracker.remaining_budget()
        elif choice == '5':
            filename = input("Введите имя файла для сохранения: ")
            tracker.save_to_file(filename)
        elif choice == '6':
            filename = input("Введите имя файла для загрузки: ")
            tracker.load_from_file(filename)
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
```