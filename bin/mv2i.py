#!/usr/bin/python
#encoding: utf-8

# Carrega as variáveis do sistema
import env

# Carrega os para utilizar a interface 
# com o sistema e time para sincronizar
# o loop principal
import os
import time

# Variável que possui o número de 
# arquivos que estão dentro da 
# pasta no início da execução
count = len(os.listdir(env.DEB_PATH))

# Loop principal
while True:
	# Verifica se houve inclusão de 
	# arquivos na pasta, se sim
	# exibe na tela a string "deu bom"
	if len(os.listdir(env.DEB_PATH)) != count:
		print("deu bom!")
		
		# Atualiza o número de arquivos que
		# estão dentro da pasta.
		count = len(os.listdir(env.DEB_PATH))

	# Para não consumir o CPU o programa
	# aguarda 1 segundo para fazer a próxima varredura.
	time.sleep(1)
