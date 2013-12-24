import redis
import json

class ItemServiceMock:
	def __init__(self):
                self.items = []
		self.items.append(Item('Televisor LCD 46 polegadas', 'Teste', 1500))
		self.items.append(Item('Smartphone 5S', 'Telefone mais smart do mercado!', 3999))
		self.items.append(Item('Geladeira Double-sided', 'Melhor geladeira do mundo! E nao podemos nos contentar com nada alem disso', 3999))
		self.items.append(Item('Carrocinha de cachorro-quente', 'Otimizada para produzir cachorro quente num ambiente multi-thread e escalavel', 3999))
		self.items.append(Item('Smartphone 5S', 'Telefone mais smart do mercado!', 3999))
		self.items.append(Item('Smartphone 5S', 'Telefone mais smart do mercado!', 3999))
	def list(self):
		return self.items

class ItemServiceRedis:
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
	def list(self):
		keys = self.r.zrevrange('releaseDate', 0, 20)
		items = []
		for key in keys:
			items.append(json.loads(self.r.get(key)))
		return items

class Item:
	def __init__(self, name, descritpion, price):
		self.name = name
		self.description = descritpion
		self.price = price
