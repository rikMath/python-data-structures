class Node(obj):
	"""Classe representando o nó de uma lista
	Data = dado armazenado
	nextNode = nó que aponta próximo
	previousNode = nó que aponta anterior"""
	def __init__(self, data):
		"""Dados inseridos inicialmente
		Próximo nó e nó anterior são inicialmente
		tratados como None
		O(1)"""
		self.data = data
		self.nextNode = None
		self.previousNode = None

class LinkedList(obj):

	def __init__(self):
		self.head = None
		self.last = None
		self.size = 0

	def insertStart(self, data):
		self.size+=1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
			self.last = newNode

		else:
			self.head.previousNode = newNode
			newNode.nextNode = self.head
			self.head = newNode

	def size(self):
		return self.size

	def insertEnd(self, data):
		self.size+=1
		newNode = Node(data)

		if not self.last:
			self.head = newNode
			self.last = newNode

		else:
			newNode.previousNode = self.last
			self.last.nextNode = newNode
			self.last = newNode

	def __str__(self):
		actualNode = self.head
		if actualNode is not None:
			while actualNode.nextNode is not None:
				print(f'{actualNode.data}')
				actualNode = actualNode.nextNode

		else:
			print('Lista Vazia')

	def remove(self, data):
		pass

	def __getitem__(self, key):
        if (self.size-1 <= key):
        	raise ValueError("Key doesn\'t exist")
        while True:
        	pass
