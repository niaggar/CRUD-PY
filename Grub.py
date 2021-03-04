
from datetime import date, datetime
from typing import Text


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


def create_data():
    global names_list, dates_list
    
    print('\n +++++ Create Data +++++')
    
    new_time = datetime.now()
    new_name = input('Enter the name \n >>> ')
    
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
        print(f'{i + 1}> {dates_list[i]} -- {names_list[i]} ')


def edit_data(name: str = None) -> None:
    global names_list, dates_list
    
    print('\n +++++ Edit Data +++++')
    
    if not name:
        name = input('What person do you whant to change? \n >>> ')
       
    try: 
        position = names_list.index(name)
        new_name = input('Give the new name \n >>> ')
        names_list[position] = new_name
    except:
        print('That person doesn\'t exist')


def delete_data():
    pass


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
    return input('>>> ')
    

if __name__ == '__main__':
    
    status = True
    while status == True:
        start_comand = start_program()
        detect_command(start_comand)
    
    