
from datetime import datetime
import csv
import os


# Establece almacen temporal de los datos
data_list = []

# Establece nombre del archivo donde guardar los datos
DATA_TABLE = 'data.csv'
# Establece el nombre de las columnas del archivo
DATA_SCHEMA = ['time', 'name', 'mail']



# Realiza la lectura del archivo
def _initialize_data_from_storage() -> None:
    
    # Abre el archivo en modo de lectura
    with open(DATA_TABLE, mode = 'r') as f:
        
        # Asigna el nombre de columanas a cada valor
        reader = csv.DictReader(f, fieldnames = DATA_SCHEMA)
        
        # Agrega cada dato al almacen temporal
        for row in reader:
            data_list.append(row)



# Realiza la escritura del archivo
def _save_data_to_storage() -> None:
    
    # Crea el nombre del archivo temporal
    tmp_table_name = '{}.tmp'.format(DATA_TABLE)
    
    # Abre/Crea el archivo temporal en modo escritura
    with open(tmp_table_name, mode = 'w') as f:
        
        # Escribe los datos del almacen temporal al archivo temporal
        writer = csv.DictWriter(f, fieldnames = DATA_SCHEMA)
        writer.writerows(data_list)
        
        # Elimina el archivo original
        os.remove(DATA_TABLE)
        # Renombra el archivo temporal como el archivo original
        os.rename(tmp_table_name, DATA_TABLE)
    
    

# Determina que comando se pretende ejecutar
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



# Crear un nuevo dato
def create_data():
    global data_list
    
    print('\n+++++ Create Data +++++')
    
    # Establece el modelo del diccionario del dato a crear
    new_data = {
        'time': _get_cliet_field('time'),
        'name': _get_cliet_field('name').capitalize(),
        'mail': _get_cliet_field('mail').lower(),
    }
    
    # Verifica la no existencia del dato a crear 
    if not _verify_name_existence(new_data)[0]:
        data_list.append(new_data)
    else:
        print('That person already exist')



# Input para determiar los valores de un dato
def _get_cliet_field(field_name: str) -> str:
    field = None
    
    # Retorna la fecha actual automaticamente
    if field_name == 'time':
        return datetime.now()
    
    # Realiza el input hasta que el campo tenga un valor
    while not field:
        field = input(f'What is the client\'s {field_name.upper()}?\n>>> ')
        
    return field



# Verificar la existencia y posicion dentro de la lista de un dato
def _verify_name_existence(new_data: dict) -> tuple:
    global data_list
    
    # Recorre la lista de datos
    for position, data in enumerate(data_list):
        # Compara el nombre de cada dato con el nombre buscado
        if data['name'] == new_data['name']:
            # Retorna el estado y la posicion del dato
            return (True, position)
    
    # Retorna falso en caso de que el dato no exista
    return (False, None)



# Presenta los datos en forma de lista
def list_data():
    global data_list
    
    # Recorre la lista imprimiendo cada uno de los valores
    for position, data in enumerate(data_list):
        print('{}> {} -- {} -- {} '.format(
            position + 1, 
            data['time'], 
            data['name'], 
            data['mail'])
        )



# Permite realizar edicion a los datos de la lista
def edit_data() -> None:
    global data_list
    
    print('\n+++++ Edit Data +++++')
    
    # Pregunta que dato va a ser editado
    edit_name = input('What person do you whant to change?\n>>> ').capitalize()
    
    # Determian si el dato se encuentra en la lista
    position = _verify_name_existence({'name': edit_name})[1]
    
    if not position and position != 0:
        return print(f'{edit_name.upper()} dosn\'t exist')
    
    else:
        # Comprueba que el campo a editar exista
        key_edit = input('What value do you want to change?\n>>> ').lower()
        
        if key_edit in data_list[position].keys():
            data_list[position][key_edit] = _get_cliet_field(key_edit)
        else:
            print(f'{key_edit.upper()} is not a correct key')



# Permite eliminar un dato en especifico
def delete_data():
    global data_list
    
    print('\n+++++ Delete Data +++++')
    
    # Pregunta que dato va a ser eliminado
    delete_name = input('What person do you whant to delete?\n>>> ').capitalize()
    
    # Verifica la existencia del dato
    state = _verify_name_existence({'name': delete_name})
    
    if state[0]:
        # Elimina el dato en su totalidad
        data_list.pop(state[1])
        print(f'---- {delete_name.upper()} was deleted ----')
    else:
        print(f'-!- {delete_name.upper()} doesn\'t exist -!-')



def start_program() -> None:    
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
    
    # Inicia la lectura del archivo
    _initialize_data_from_storage()
    
    status = True
    start_program()
    while status == True:
        start_comand = input('\n \n>>> ')
        detect_command(start_comand)
    
    # Realiza la escritura en disco  
    _save_data_to_storage()