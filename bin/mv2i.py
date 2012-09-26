#!/usr/bin/python
#encoding: utf-8

# Carrega as variáveis do sistema
import env

# Carrega a classe Trigger
from Trigger import Trigger
from VerificaArquivos import VerificaArquivos

# Carrega os para utilizar a interface 
# com o sistema e time para sincronizar
# o loop principal
import os
import time

mv2i = VerificaArquivos()

# Loop principal
while True:
	mv2i.wait()
	# Para não consumir o CPU o programa
	# aguarda 1 segundo para fazer a próxima varredura.
	time.sleep(1)
