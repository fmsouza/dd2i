#encoding: utf-8

from idpkg import Instalation

# Carrega as variáveis do sistema
import env

# Carrega a classe Trigger
from Trigger import Trigger

# Carrega os para utilizar a interface 
# com o sistema
import os

class VerificaArquivos(Trigger):
	def __init__(self):
		# Variável que possui a lista de 
		# arquivos que estão dentro da 
		# pasta no início da execução
		self.now = os.listdir(env.DEB_PATH)
	
	def diff(self,l1,l2):
		return list(set(l1).union(set(l2)) - set(l1).intersection(set(l2)))

	def condition(self):
		# Verifica se houve inclusão ou exclusão de arquivos
		if self.diff(os.listdir(env.DEB_PATH),self.now)!=[]:
			return True
		else:
			return False
	
	def triggerCallback(self):
		# Atualiza a lista de arquivos que
		# estão dentro da pasta.
		self.old = self.now
		self.now = os.listdir(env.DEB_PATH)
		
		for debfile in self.diff(self.now,self.old):
			instalation = Instalation()
			instalation.debfile(debfile)
			
			if debfile not in self.old:
				instalation.install()
			else:
				instalation.uninstall()
			
			instalation=None

		print self.old,self.now
