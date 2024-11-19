import os
# Biblioteca os e suas principais funçoes

# 1:

# a:
caminho = os.path.dirname(__file__)
# os.path mexe nos caminhos de arquivos. dirname pega o nome
# do diretório pai do arquivo escrito


# b:
caminho_absoluto_do_arquivo = os.path.abspath(__file__)
# Entrega o caminho absoluto do arquivo


# c:
juntar_caminhos = os.path.join(caminho, __file__)
# Junta o caminho do diretório pai com o arquivo


# d:
esse_diretorio_existe = os.path.exists(caminho)
# Confere se um caminho de arquivo existe


# 2:

print(os.listdir(caminho))
# os.listdir de algum path faz uma lista dos arquivos e diretório
# presentes em um diretório

# 3:

os.makedirs(os.path.join(caminho, 'arco___ijii'), exist_ok=True)
# Função que cria diretório e seus diretórios
# base caso não existam. exist_ok = True faz não dar erro caso já exista tal diretório

# 4:

os.path.splitext(caminho)
# Didide o caminho de um arquivo em dois, um antes e outro depois
# da extensão do arquivo

# 5:

# Renomeia um arquivo ou diretório
os.rename(caminho, 'Organizador de Arquivos')
