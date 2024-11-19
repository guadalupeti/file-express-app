import os
import shutil
from datetime import datetime

# As próximas 5 funções trabalham em conjunto

# Recebe um caminho de diretório e retorna uma lista com o nome de cada arquivo nele
def read_dir_list(dir_name: str):
    file_list = os.listdir(dir_name)
    return file_list


# Recebe a lista de arquivos no diretório, separa somente o formato do arquivo e retorna essa outra lista
def split_file_text(list: list[str]):
    format_list = []
    for c in list:
        split = os.path.splitext(c)
        format_list.append(split[1])
    return format_list


# Recebe a lista de formato dos arquivos e o caminho para o diretório. 
# Cria um diretório pra cada formato de arquivo
def create_dirs(format_list: list[str], dir: str):
    for format in format_list:
        os.makedirs(os.path.join(dir, format.replace('.', '')), exist_ok=True)


# Recebe o caminho do diretório, a lista de arquivos no diretório e de formato dos arquivos.
# Depois move cada arquivo para o diretório de seu respectivo formato
def move_files(dir: str, file_list: list[str], format_list: list[str]):
    for num, file in enumerate(file_list):
        if format_list[num] == '':
            continue

        shutil.move(os.path.join(dir, file), os.path.join(dir, format_list[num].replace('.', '')))


# Recebe o diretório e reune todas funções de cima para realmente executar a função
def create_dir_by_file_format(dir: str):

    if not os.path.exists(dir):
        print('O Diretório não existe!')

    else:
        #Pega uma lista dos arquivos no dir e joga na variavel
        file_list = read_dir_list(dir)

        #Pega uma lista dos formatos de cada arquivo e joga na variavel
        global format_file_list
        format_file_list = split_file_text(file_list)

        #Cria diretórios baseados no formato do arquivo
        create_dirs(format_file_list, dir)

        #Move os arquivos para as pastas do respectivo formato
        move_files(dir, file_list, format_file_list)


# Recebe um diretório e desfaz todas pastas nele e retorna os arquivos para o diretório
def undoo_dir_organization(dir: str):

    subdirs_list = os.listdir(dir)                  # Define uma lista de subdiretórios do diretório principal

    for sub_dir in subdirs_list:                    # Para cada subdiretório do dir para
        sub_dir_path = os.path.join(dir, sub_dir)   # Define o caminho dele

        if os.path.isdir(sub_dir_path):             # Confere se é um diretório
           
            if '.' + sub_dir in format_file_list:   # Confere se o nome do subdiretório corresponde a de um dos criados agora
         
                for file in os.listdir(sub_dir_path):                  # Para cada arquivo em um subdiretório
                    shutil.move(os.path.join(sub_dir_path, file), dir) # Move-o para o diretório pai

                shutil.rmtree(sub_dir_path) # Depois de remover os arquivos todos, apaga o subdiretório
        else:
            continue


# Recebe um caminho de diretório e um caminho de icone(ico) e 
# faz a alteração do icone personalizado do diretório
def change_dir_color(dir: str, icon: str):

    os.system(f'attrib +r "{dir}"')

    content = f'''[.ShellClassInfo]
    IconResource={icon},0'''

    desktop_ini_path = os.path.join(dir,"desktop.ini")

    os.system(f'attrib -s -h "{desktop_ini_path}"')

    with open(desktop_ini_path, "w") as file:
        file.write(content.strip())

    os.system(f'attrib +r "{dir}"')
    os.system(f'attrib +s +h "{desktop_ini_path}"')


#Função que recebe um diretório e um modo de definição(renomear por data ou enumerar por data) e 
def rename_all_files(folder: str, define_for: str):

    date_register = {}

    match define_for:
        case 'date':
            for file in os.listdir(folder):
                complete_path = os.path.join(folder,file)
                if os.path.isfile(complete_path):
                    timestamp = os.path.getctime(complete_path)
                    date = datetime.fromtimestamp(timestamp)
                    formated_date = date.strftime("%d-%m-%y")
                    extension = os.path.splitext(file)[1]

                    if formated_date not in date_register:
                        date_register[formated_date] = 1
                    else:
                        date_register[formated_date] += 1      

                    new_name = f'{formated_date}_{date_register[formated_date]}{extension}'
                    new_path = os.path.join(folder, new_name)
 
                    os.rename(complete_path, new_path)
            return True
        
        case 'enumerate_by_date':
            files_to_enumerate = []
            for file in os.listdir(folder):
                complete_path = os.path.join(folder,file)
                if os.path.isfile(complete_path):
                    timestamp = os.path.getctime(complete_path)
                    date = datetime.fromtimestamp(timestamp)
                    files_to_enumerate.append((complete_path, date))

            files_to_enumerate.sort(key = lambda x: x[1])
            
            for i, file in enumerate(files_to_enumerate, start = 1):
                extension = os.path.splitext(file[0])[1]
                new_path = os.path.join(folder, f'{i}{extension}')
                os.rename(file[0], new_path)

            return True
