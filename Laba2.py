import re
import unittest

def verify_ip(ip_value):
    error_string = ""
    the_name = "IPaddress"
    
    # Паттерн для валидации формата IP-адреса
    ip_pattern = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
    ip_match = ip_pattern.match(ip_value)
    
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