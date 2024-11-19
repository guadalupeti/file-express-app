import shutil
import os
# Biblioteca shutil e suas principais funções
# Funções de alto nível como copiar, mover arquivos e diretórios.

caminho = os.path.dirname(__file__)

#1:
shutil.move(__file__, "Diretório")    
#Move um arquivo para um diretório

#2:
shutil.copy(__file__, caminho)
#Copia um arquivo e manda para um diretório

#3:
shutil.copy2(__file__, caminho)
#Igual o copy, porém também copia os metadados do arquivo

#4:
shutil.rmtree("diretorio")
#Remove um diretório e todo conteúdo nele

#5:
shutil.make_archive("nome","formato","diretorio")
#Cria um arquivo compactado a partir de um diretório

#6:
shutil.unpack_archive("nome","diretorio para extrair")