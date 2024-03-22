class Zdaniya:
	gorod = None
	ulica = None
	nomer_doma = None

	def set_data(self, gorod=None, ulica=None, nomer_doma=None):
		self.gorod = gorod
		self.ulica = ulica
		self.nomer_doma = nomer_doma

	def get_data(self):
		print(f"gorod: {self.gorod}", f"ulica: {self.ulica}", f"nomer_doma: {self.nomer_doma}", sep="\n")

	def __init__(self, gorod=None, ulica=None, nomer_doma=None):
		self.set_data(gorod, ulica, nomer_doma)
		self.get_data()
