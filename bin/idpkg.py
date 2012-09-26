#!/usr/bin/python
#encoding: utf-8

import subprocess
import sys

class Instalation:
	def __init__(self):
		self.debfiles = list()
		self.packages = list()
		self.params = ["dpkg"]

	def debfile(self,argv):
		a = subprocess.Popen(["dpkg-deb","-I",argv],stdout=subprocess.PIPE)
		b = subprocess.Popen(["grep","Package"],stdin=a.stdout,stdout=subprocess.PIPE)
		c = subprocess.Popen(["cut","-d",":","-f2"],stdin=b.stdout,stdout=subprocess.PIPE)
		a.stdout.close()
		b.stdout.close()

		self.packages.append(c.communicate()[0].replace(" ","").replace("\n",""))
		self.debfiles.append(argv)

	def install(self):
		r = subprocess.Popen(self.params+["-i"]+self.debfiles,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
		r.wait()
		return r.returncode

	def uninstall(self):
		r = subprocess.Popen(self.params+["-r"]+self.packages,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
		r.wait()
		return r.returncode
