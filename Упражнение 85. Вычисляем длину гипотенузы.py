import time
client = {}
r = []
while True:
    try:
        while True:
            def add_client(name, room):
                client[name] = room
                r.append(client[name])
                for k, v in client.items():
                    print(k, v)
            def delete_client(name):
                a = client[name]
                r.remove(a)
                client.pop(name)
                print(f'Клиент с именем {name} удалён')
            def rooms():
                print(r)
            admin = input('Что Вы хотите сделать?\n1. Добавить клиента\n2. Удалить клиента\n3. Посмотреть список занятых комнат\n')
            if admin == '1':
                client_name = input('Имя клиента\n')
                client_room = int(input('Какой номер комнаты?\n'))
                add_client(client_name, client_room)
            elif admin == '2':
                del_client = input('Введите имя кого выселяем\n')
                delete_client(del_client)
            elif admin == '3':
                rooms()
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)