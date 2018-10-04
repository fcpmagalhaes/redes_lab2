# encoding: utf-8

import sys, subprocess, time
from random import randint
from subprocess import call

endereco = subprocess.check_output('pwd', shell=True)
endereco = endereco.rstrip('\n')
opcao = 0

print (30 * '-')
print ("   B A T E - P A P O    ")
print (30 * '-')
print ("1. Criar uma sala ")
print ("2. Entrar em uma sala ")
print ("3. Sair")
print (30 * '-')

while(opcao != 1 and opcao != 2 and opcao !=3):
    opcao = raw_input('Digite a sua escolha [1-3] : ')
    opcao = int(opcao)

if opcao == 1:
    porta = randint(4000, 9000)
    subprocess.call(['gnome-terminal', '-x', 'python', endereco+'/server.py', str(porta)])
    time.sleep(2)
    subprocess.call(['python', endereco+'/chat_client.py', 'localhost', str(porta)])
elif opcao == 2:
    porta = raw_input('Digite a sala que deseja entrar: ')
    subprocess.call(['python', endereco+'/chat_client.py', 'localhost', str(porta)])
elif opcao == 3:
    print "Tchau!\n\n"
    sys.exit()

