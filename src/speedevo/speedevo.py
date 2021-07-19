from pandas import pandas as pd
from matplotlib import pyplot as plt
from speedtest import Speedtest


class Speedevo:
	__slots__ = ['servers', 'threads', 'speed', 'path']

	def __init__(self):
		self.servers = [16438]  	# Local do servidor
		self.threads = 16  			# Quantidade de threads que vai ser utilizada
		self.speed = Speedtest()
		self.path = None

		try:
			self.speed.get_servers(self.servers)
		except Exception:
			self.speed.get_closest_servers()
			self.speed.get_best_server()

	"""
	Parametros
	----------
	Nome do arquivo: str
		Nome do arquivo onde ira armazenar as informações em .xlxs
		Nome do arquivo não pode ser vazio
	"""
	
	def speed_test(self, name_file=str):
		self.speed.download(threads=self.threads)   # threads de download
		self.speed.upload(threads=self.threads)  	# threads de upload

		results_dict = {
			'Download': [self.speed.results.download / 1000000.0], # resultado de download em megabits
			'Upload': [self.speed.results.upload / 1000000.0],	   # resultado do upload em megabits
			'Ping': [self.speed.results.ping], 					   # resultado do ping da internet
			'Server': [self.speed.results.server], 				   # servidor que voce utilizou para realizar o teste
			'Times Tamp': [self.speed.results.timestamp],		   # informa a hora e data que foi realizada o teste
			'Bytes Sent': [self.speed.results.bytes_sent],		   # quantidade de bites enviados
			'Bytes Received': [self.speed.results.bytes_received], # quantidade de bites recebidos
			'Client': [self.speed.results.client],				   # ip do cliente e o servidor e o seu servidor
		}

		dice = pd.DataFrame(data=results_dict)
		self.path = name_file + '.xlsx'

		try:
			file = open(self.path, mode='x', encoding='UTF8')
			file.close()

			with open(self.path, mode='w', newline='', encoding='UTF8'):
				dice.to_excel(self.path)

		except IOError:
			with open(self.path, mode='a', newline='', encoding='UTF8'):
				previous = pd.read_excel(self.path)
				previous = previous.drop(columns=['Unnamed: 0'])
				previous.head()
				new = pd.concat((previous, dice), axis=0, ignore_index=True)
				new.to_excel(self.path)

	"""
	Parametros
	----------
	line: str
		Colocar o nome do arquivo para mostrar um grafico do download e upload.
		Nome do arquivo nao pode ser vazio.
		OBS: o comando speed_test precisa ter sido usado antes, pois precisa do arquivo .xsxl gerado por essa função.
	"""
	def line(self, name_file=str):
		file = pd.read_excel(name_file + '.xlsx')
		plt.plot(file['Download'], c='b', ls='-', lw='2', marker='o', fillstyle='full', label='Download')
		plt.plot(file['Upload'], c='r', ls='-', lw='2', marker='^', fillstyle='full', label='Upload')
		plt.legend()
		plt.title('Gráfico de linha - Speed Evo', color='black', fontsize=16)
		plt.xlabel('Índice', fontsize=16)
		plt.ylabel('Velocidade', fontsize=16)
		plt.show()
	"""
	Parametros
	----------
	histogram: str
		Colocar o nome do arquivo e a coluna que deseje ser mostrada.
		Nome do arquivo e da coluna nao pode ser vazi.o
		OBS: o comando speed_test precisa ter sido usado antes, pois precisa do arquivo .xsxl gerado por essa função.
	"""
	def histogram(self, name_file=str):
		file = pd.read_excel(name_file + '.xlsx')
		plt.hist(file['Download'], bins=20, label='Download')
		plt.hist(file['Upload'], bins=20, label='Upload')
		plt.legend()
		plt.title('Histograma - Speed Evo', color='black', fontsize=16)
		plt.xlabel('Velocidade', fontsize=16)
		plt.ylabel('Índice', fontsize=16)
		plt.show()
