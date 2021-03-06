
from datetime import datetime


data_list = [
    {
        'time': datetime.now(),
        'name': 'Nicolas',
        'mail': 'nicolas@gmail.com',
    },
    {
        'time': datetime.now(),
        'name': 'Leonor',
        'mail': 'leonor@gmail.com',
    },
    {
        'time': datetime.now(),
        'name': 'Rafael',
        'mail': 'rafael@gmail.com',
    },
]



def detect_command(command: str) -> None:
    global status
    
    command = command.lower()
    if command == 'exit':
        status = False
    elif command == 'create':
        create_data()
    elif command == 'list':
        list_data()
    elif command == 'edit':
        edit_data()
    elif command == 'delete':
        delete_data()



def create_data():
    global data_list
    
    print('\n +++++ Create Data +++++')
    
    new_data = {
        'time': _get_cliet_field('time'),
        'name': _get_cliet_field('name'),
        'mail': _get_cliet_field('mail'),
    }
    
    if not _verify_name_existence(new_data):
        data_list.append(new_data)
    else:
        print('That name exist')



def _get_cliet_field(field_name: str) -> str:
    field = None
    
    if field_name == 'time':
        return datetime.now()
    
    while not field:
        field = input(f'What is the client {field_name}?')
        
    return field



def _verify_name_existence(new_data: dict) -> bool:
    global data_list
    
    for data in data_list: 
        if data['name'] == new_data['name']:
            return True
         
    return False



def list_data():
    global data_list
    
    element = 1
    for data in data_list:
        print('{}> {} -- {} -- {} '.format(element, data['time'], data['name'], data['mail']))
        element += 1



def edit_data(name: str = None) -> None:
    global data_list
    
    print('\n+++++ Edit Data +++++')
    
    if not name:
        name = input('What person do you whant to change? \n >>> ').capitalize()
    
    position = None
    for i in range(len(data_list)):
        if data_list[i]['name'] == name:
            position = i

    if not position and position != 0:
        return print('That person dosn\'t exist')
    else:
        to_edit = input('What value do you want to change?')
        
    key_state = False
    for keys in data_list[position].keys():
        if keys == to_edit:
            key_state = True
    
    if key_state:
        data_list[position][to_edit] = _get_cliet_field(to_edit)
    else:
        print(f'{to_edit} is not a correct key')



def delete_data():
    global names_list, dates_list
    
    print('\n +++++ Delete Data +++++')
    
    name = input('What person do you whant to delete? \n >>> ').capitalize()
    
    if name in names_list:
        position = names_list.index(name)
        names_list.pop(position)
        dates_list.pop(position)
        print(f'---- {name.upper()} was eliminated ----')
    else:
        print(f'-!- {name.upper()} doesn\'t exist -!-')



def start_program():    
    print(
        '''
        <------------------------------->
                Starting Programa
        <------------------------------->
        Comands: ------------------------
        -------> list
        -------> create
        -------> edit
        -------> delete
        -------> exit
        ---------------------------------
        '''
    )
        


if __name__ == '__main__':
    
    status = True
    start_program()
    while status == True:
        start_comand = input('\n \n>>> ')
        detect_command(start_comand)
    
    