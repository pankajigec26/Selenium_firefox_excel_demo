import xlrd
class parse_excel:
	def __init__(self):
		self.datafile="Data.xlsx"
		self.workbook = xlrd.open_workbook(self.datafile)
		self.sh=self.workbook.sheet_by_index(0)
		self.d = {}
	def convert_data_dict(self):
		for i in range(1,self.sh.nrows):
			self.user_name = self.sh.cell(i,0).value
			self.password = self.sh.cell(i,1).value
			self.d[self.user_name] = self.password
		return self.d
		
#ab=parse_excel()
#print ab.convert_data_dict()