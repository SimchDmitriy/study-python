documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
def get_document_owner(doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    return None
def main():
    while True:
        command = input("Введите команду (p - поиск владельца, q - выход): ")
        
        if command == 'q':
            print("Выход из программы.")
            break
        elif command == 'p':
            doc_number = input("Введите номер документа: ")
            owner = get_document_owner(doc_number)
            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ не найден.")
        else:
            print("Неизвестная команда, попробуйте снова.")
main()