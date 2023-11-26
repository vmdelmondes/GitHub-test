#Branch 2 code

import hashlib

#a senha inserida pelo usuário está no arquivo password.txt
#a senha criptografada está em data_base.txt

#abre a senha inserida pelo usuário e salva em 'data'
with open('password.txt', 'r') as file:
    data = file.read()

#inicia o hash object, cria o hash e salva em hash_value
hash_object = hashlib.sha256()

hash_object.update(data.encode('utf-8'))

hash_value = hash_object.hexdigest()

#with open('data_base.txt', 'w') as file:
#    file.write(f'{hash_value}')


#pega o hash da senha do usuário do banco de dados
with open('data_base.txt', 'r') as file:
    compare = file.read()


#comapara se a senha inserida (recebida via arquivo de texto)
#é igual à senha salva no banco de dados

if compare == hash_value:
    retorno = True

else:
    retorno = False

print(retorno)