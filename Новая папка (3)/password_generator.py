import random
import string
import pyperclip  # Для копирования пароля в буфер обмена (установите библиотеку)

# Попробуйте установить библиотеку pyperclip, если она отсутствует
try:
    import pyperclip
except ImportError:
    pyperclip = None

def generate_password(length=16, use_uppercase=True, use_digits=True, use_specials=True):
    """Генератор сложных паролей"""
    if length < 8:
        raise ValueError("Пароль должен быть длиной не менее 8 символов.")
    
    # Базовые символы: буквы в нижнем регистре
    characters = string.ascii_lowercase
    
    # Добавляем опции
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation  # Все специальные символы
    
    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Добро пожаловать в Генератор паролей!")
    print("===================================")
    
    # Настройка длины
    try:
        length = int(input("Введите длину пароля (не менее 8): "))
    except ValueError:
        print("Введите число!")
        return
    
    # Вопросы о включении символов
    use_uppercase = input("Включить заглавные буквы? (y/n): ").strip().lower() == 'y'
    use_digits = input("Включить цифры? (y/n): ").strip().lower() == 'y'
    use_specials = input("Включить специальные символы? (y/n): ").strip().lower() == 'y'
    
    try:
        password = generate_password(length, use_uppercase, use_digits, use_specials)
        print("\nВаш сложный пароль:")
        print(password)
        
        # Копирование в буфер обмена (если возможно)
        if pyperclip:
            pyperclip.copy(password)
            print("\nПароль скопирован в буфер обмена!")
        else:
            print("\npyperclip не установлен. Пароль не был скопирован в буфер обмена.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
