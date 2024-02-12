import os

def create_contact(last_name, first_name, patronymic, organization, work_phone, personal_phone):
    """
    Создает строку с информацией о контакте в формате CSV.

    Parameters:
    - last_name (str): Фамилия контакта.
    - first_name (str): Имя контакта.
    - patronymic (str): Отчество контакта.
    - organization (str): Название организации контакта.
    - work_phone (str): Рабочий номер телефона контакта.
    - personal_phone (str): Личный (сотовый) номер телефона контакта.

    Returns:
    str: Строка с информацией о контакте в формате CSV.
    """
    return f"{last_name},{first_name},{patronymic},{organization},{work_phone},{personal_phone}\n"

def save_contacts(contacts: list, file_path: str) -> None:
    """
    Сохраняет список контактов в текстовый файл.

    Parameters:
    - contacts (list): Список контактов.
    - file_path (str): Путь к файлу для сохранения.

    Returns:
    None
    """
    with open(file_path, 'w') as file:
        file.writelines(contacts)

def read_contacts(file_path: str) -> list:
    """
    Считывает контакты из текстового файла.

    Parameters:
    - file_path (str): Путь к файлу с контактами.

    Returns:
    list: Список контактов.
    """
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, 'r') as file:
        return file.readlines()

def display_contacts(contacts: list, page_size: int) -> None:
    """
    Выводит контакты постранично.

    Parameters:
    - contacts (list): Список контактов.
    - page_size (int): Количество контактов на одной странице.

    Returns:
    None
    """
    if not contacts:
        print("Телефонная книга пуста.")
    else:
        print("Контакты:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact.strip()}")
            if i % page_size == 0:
                input("Нажмите Enter для продолжения...")

def add_contact(contacts: list, file_path: str) -> None:
    """
    Добавляет новый контакт в телефонную книгу.

    Parameters:
    - contacts (list): Список контактов.
    - file_path (str): Путь к файлу для сохранения.

    Returns:
    None
    """
    last_name = input("Введите фамилию (обязательно): ")
    first_name = input("Введите имя (обязательно): ")
    patronymic = input("Введите отчество: ")
    organization = input("Введите название организации (оставьте пустым если нету организации): ")

    # Ввод и проверка формата сотового телефона
    while True:
        personal_phone = input("Введите номер сотового телефона (+7 (999) 999 99 99): ")
        personal_phone = ''.join(filter(str.isdigit, personal_phone))  # Оставляем только цифры

        # Удаление +7 или 8 в начале номера
        if personal_phone.startswith('8'):
            personal_phone = personal_phone[1:]
        elif personal_phone.startswith('+7'):
            personal_phone = personal_phone[2:]

        if len(personal_phone) == 10:
            personal_phone = "+7" + personal_phone
            break
        else:
            print("Некорректный формат сотового телефона. Повторите ввод.")

    # Ввод и проверка формата городского телефона, если организация введена
    if organization:
        while True:
            work_phone = input("Введите номер рабочего телефона (городской, не более 10 цифр): ")

            # Удаление +7 или 8 в начале номера
            if work_phone.startswith('8'):
                work_phone = work_phone[1:]
            elif work_phone.startswith('+7'):
                work_phone = work_phone[2:]

            work_phone = ''.join(filter(str.isdigit, work_phone))  # Оставляем только цифры

            if 5 <= len(work_phone) <= 10:
                break
            else:
                print("Некорректный формат городского телефона. Повторите ввод.")
    else:
        work_phone = ""

    new_contact = create_contact(last_name, first_name, patronymic, organization, work_phone, personal_phone)
    contacts.append(new_contact)
    save_contacts(contacts, file_path)
    print(f"Контакт {first_name} {last_name} добавлен.")




def edit_contact(contacts: list, file_path: str) -> None:
    """
    Редактирует контакт в телефонной книге.

    Parameters:
    - contacts (list): Список контактов.
    - file_path (str): Путь к файлу для сохранения.

    Returns:
    None
    """
    display_contacts(contacts, 5)
    try:
        index = int(input("Введите номер контакта для редактирования: ")) - 1
        if 0 <= index < len(contacts):
            last_name = input("Введите новую фамилию (оставьте пустым, чтобы оставить без изменения): ")
            first_name = input("Введите новое имя (оставьте пустым, чтобы оставить без изменения): ")
            patronymic = input("Введите новое отчество (оставьте пустым, чтобы оставить без изменения): ")
            organization = input("Введите новое название организации (оставьте пустым, чтобы оставить без изменения): ")

            # Ввод и проверка формата сотового телефона
            while True:
                personal_phone = input("Введите новый номер сотового телефона (+7 (999) 999 99 99, оставьте пустым, чтобы оставить без изменения): ")
                if not personal_phone:
                    break

                personal_phone = ''.join(filter(str.isdigit, personal_phone))  # Оставляем только цифры

                # Удаление +7 или 8 в начале номера
                if personal_phone.startswith('8'):
                    personal_phone = personal_phone[1:]
                elif personal_phone.startswith('+7'):
                    personal_phone = personal_phone[2:]

                if len(personal_phone) == 10:
                    personal_phone = "+7" + personal_phone
                    break
                else:
                    print("Некорректный формат сотового телефона. Повторите ввод.")

            # Ввод и проверка формата городского телефона
            if organization:
                while True:
                    work_phone = input("Введите новый номер рабочего телефона (городской, не более 10 цифр, оставьте пустым, чтобы оставить без изменения): ")

                    if not work_phone:
                        break

                    # Удаление +7 или 8 в начале номера
                    if work_phone.startswith('8'):
                        work_phone = work_phone[1:]
                    elif work_phone.startswith('+7'):
                        work_phone = work_phone[2:]

                    work_phone = ''.join(filter(str.isdigit, work_phone))  # Оставляем только цифры

                    if 5 <= len(work_phone) <= 10:
                        break
                    else:
                        print("Некорректный формат городского телефона. Повторите ввод.")
            else:
                work_phone = ""
            contact_parts = contacts[index].split(',')
            contact_parts[0] = last_name if last_name else contact_parts[0]
            contact_parts[1] = first_name if first_name else contact_parts[1]
            contact_parts[2] = patronymic if patronymic else contact_parts[2]
            contact_parts[3] = organization if organization else contact_parts[3]
            contact_parts[4] = work_phone if work_phone else contact_parts[4]
            contact_parts[5] = personal_phone if personal_phone else contact_parts[5]

            contacts[index] = ','.join(contact_parts)
            save_contacts(contacts, file_path)
            print("Контакт отредактирован.")
        else:
            print("Неверный номер контакта.")
    except ValueError:
        print("Введите корректный номер.")

def search_contact(contacts: list) -> None:
    """
    Ищет контакт в телефонной книге по имени и фамилии, а также по номеру телефона.

    Parameters:
    - contacts (list): Список контактов.

    Returns:
    None
    """
    search_query = input("Введите имя, фамилию или номер телефона для поиска: ")
    found_contacts = []

    for contact in contacts:
        contact_parts = contact.split(',')
        if (
            search_query.lower() in contact_parts[0].lower() or  # Поиск по фамилии
            search_query.lower() in contact_parts[1].lower() or  # Поиск по имени
            search_query in contact_parts[5]  # Поиск по номеру телефона
        ):
            found_contacts.append(contact)

    if found_contacts:
        print("\nНайденные контакты:")
        for i, found_contact in enumerate(found_contacts, start=1):
            print(f"{i}. {found_contact.strip()}")

        view_choice = input("Введите номер контакта для просмотра (или Enter для продолжения): ")

        if view_choice.isdigit() and 1 <= int(view_choice) <= len(found_contacts):
            print("\nВыбранный контакт:")
            print(found_contacts[int(view_choice) - 1].strip())
    else:
        print("\nКонтакты не найдены.")



def main():
    file_path = "phone_book.txt"
    contacts = read_contacts(file_path)
    while True:
        print("\n1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Редактировать контакт")
        print("4. Поиск контакта")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_contacts(contacts, 1)
        elif choice == "2":
            add_contact(contacts, file_path)
        elif choice == "3":
            edit_contact(contacts, file_path)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == "__main__":
    main()
