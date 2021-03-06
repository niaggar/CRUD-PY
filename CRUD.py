
from datetime import datetime


names_list = []
dates_list = []


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
    global names_list, dates_list
    
    print('\n +++++ Create Data +++++')
    
    new_time = datetime.now()
    new_name = input('Enter the name \n >>> ').capitalize()
    
    if new_name in names_list:
        answer = input('The person already exist on the list. Do you want to modify? (y/n) \n >>> ')
        answer = _to_boolean(answer)
        
        if answer:
            return edit_data(new_name)
        else:
            return None
          
    names_list.append(new_name)
    dates_list.append(new_time)


def _to_boolean(value: str) -> bool:
    value = value.lower()
    
    if value == 'y' or value == '1':
        return True
    elif value == 'n' or value == '0':
        return False


def list_data():
    global names_list, dates_list
        
    for i in range(len(names_list)):
        print(f'{i + 1}. {dates_list[i]} -- {names_list[i]} ')


def edit_data(name: str = None) -> None:
    global names_list, dates_list
    
    print('\n +++++ Edit Data +++++')
    
    if not name:
        name = input('What person do you whant to change? \n >>> ').capitalize()
       
    try: 
        position = names_list.index(name)
        new_name = input('Give the new name \n >>> ')
        names_list[position] = new_name
        print(f'---- {name.upper()} is now {new_name.upper()} ----')
    except:
        print(f'-!- {name.upper()} doesn\'t exist -!-')


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
    
    