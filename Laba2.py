import re
import unittest

def verify_ip(ip_value):
    error_string = ""
    the_name = "IPaddress"
    
    # Паттерн для валидации формата IP-адреса
    ip_pattern = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
    ip_match = ip_pattern.match(ip_value)

    # Проверка специальных IP-адресов
    if ip_value == "0.0.0.0":
        error_string += f"{the_name}: {ip_value} это специальный IP адрес и не может быть использован."
    elif ip_value == "255.255.255.255":
        error_string += f"{the_name}: {ip_value} это специальный IP адрес и не может быть использован."
    
    # Проверка формата и диапазона каждого сегмента
    if not ip_match:
        error_string += f"{the_name}: {ip_value} недопустимый IP адрес."
    else:
        for i in range(4):
            segment = int(ip_match.group(i + 1))
            if segment > 255:
                error_string += f"{the_name}: {ip_value} недопустимый IP адрес."
                break

    # Возвращаем результат
    return error_string if error_string else "Введенный IP адрес корректный!"

    #Чтение IP-адресов из файла и проверка каждого.
def process_file(file_path):
    
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                ip_value = line.strip()
                if ip_value:  # Пропускаем пустые строки
                    result = verify_ip(ip_value)
                    results.append(f"{ip_value}: {result}")
    except FileNotFoundError:
        return ["Ошибка: Файл не найден."]
    except Exception as e:
        return [f"Ошибка: {e}"]
    return results

def menu():
    print("1. Проверить IP вручную")
    print("2. Проверить IP из файла")
    choice = input("Выберите опцию (1/2): ")
    
    if choice == "1":
        ip_value = input("Введите IP адрес для проверки: ")
        print(verify_ip(ip_value))
    elif choice == "2":
        file_path = input("Введите путь к файлу: ")
        results = process_file(file_path)
        for result in results:
            print(result)
    else:
        print("Неверный выбор. Завершение программы.")

main = ''
while(main != '2' ):
    main = input("Напишите '1', если хотетите войти в главное меню, и '2', если хотите завершить работу: ")
    if main == '1':
        menu()
    elif main == '2':
        print('До свидания!')
    else:
        print('Неверный ввод.')

class TestVerifyIP(unittest.TestCase):
    def test_valid_ip(self):
        result = verify_ip("192.168.0.1")
        self.assertEqual(result, "Введенный IP адрес корректный!")

    def test_invalid_format(self):
        result = verify_ip("999.999.999.9999")
        self.assertIn("IPaddress: 999.999.999.9999 недопустимый IP адрес.", result)

    def test_special_ip_zero(self):
        result = verify_ip("0.0.0.0")
        self.assertIn("IPaddress: 0.0.0.0 это специальный IP адрес и не может быть использован.", result)

    def test_special_ip_broadcast(self):
        result = verify_ip("255.255.255.255")
        self.assertIn("IPaddress: 255.255.255.255 это специальный IP адрес и не может быть использован.", result)

    def test_out_of_range_segment(self):
        result = verify_ip("300.168.0.1")
        self.assertIn("IPaddress: 300.168.0.1 недопустимый IP адрес.", result)

    def test_empty_input(self):
        result = verify_ip("")
        self.assertIn("IPaddress:  недопустимый IP адрес.", result)

if __name__ == "__main__":
    unittest.main()