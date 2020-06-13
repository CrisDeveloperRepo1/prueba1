import ConfigColorPunt
import os.path
import PySimpleGUI as sg
base_path=os.path.dirname(os.path.abspath(__file__))
boardConfig1 =ConfigColorPunt.Config1()
color_button=('white','white')

blank = {'letra':'', 'imagen': os.path.join(base_path,'imagenes/blank.png')}
a={'letra':'A','imagen': os.path.join(base_path,'imagenes/a.png')} #(r'img.png')
b={'letra':'B','imagen': os.path.join(base_path,'imagenes/b.png')}
c={'letra':'C','imagen': os.path.join(base_path,'imagenes/c.png')}
d={'letra':'D','imagen': os.path.join(base_path,'imagenes/d.png')}
e={'letra':'E','imagen': os.path.join(base_path,'imagenes/e.png')}
f={'letra':'F','imagen': os.path.join(base_path,'imagenes/f.png')}
g={'letra':'G','imagen': os.path.join(base_path,'imagenes/g.png')}
h={'letra':'H','imagen': os.path.join(base_path,'imagenes/h.png')}
i={'letra':'I','imagen': os.path.join(base_path,'imagenes/i.png')}
j={'letra':'J','imagen': os.path.join(base_path,'imagenes/j.png')}
k={'letra':'K','imagen': os.path.join(base_path,'imagenes/k.png')}
l={'letra':'L','imagen': os.path.join(base_path,'imagenes/l.png')}
m={'letra':'M','imagen': os.path.join(base_path,'imagenes/m.png')}
n={'letra':'N','imagen': os.path.join(base_path,'imagenes/n.png')}
o={'letra':'O','imagen': os.path.join(base_path,'imagenes/o.png')}
p={'letra':'P','imagen': os.path.join(base_path,'imagenes/p.png')}
q={'letra':'Q','imagen': os.path.join(base_path,'imagenes/q.png')}
r={'letra':'R','imagen': os.path.join(base_path,'imagenes/r.png')}
s={'letra':'S','imagen': os.path.join(base_path,'imagenes/s.png')}
t={'letra':'T','imagen': os.path.join(base_path,'imagenes/t.png')}
u={'letra':'U','imagen': os.path.join(base_path,'imagenes/u.png')}
v={'letra':'V','imagen': os.path.join(base_path,'imagenes/v.png')}
w={'letra':'W','imagen': os.path.join(base_path,'imagenes/w.png')}
x={'letra':'X','imagen': os.path.join(base_path,'imagenes/x.png')}
y={'letra':'Y','imagen': os.path.join(base_path,'imagenes/y.png')}
z={'letra':'Z','imagen': os.path.join(base_path,'imagenes/z.png')}
# im=r'g.png'
# img=r'blank2.png'####
img=os.path.join(base_path,'imagenes/blank2.png')

images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z}





class Tablero:
	def __init__(self,filas,columnas):
		self._filas = filas
		self._columnas = columnas
	def get_filas(self):
		return self._filas
	def get_columnas(self):
		return self._columnas
	
	def prueba(self):
		print('hola')

		
	def prueba2(self):
		print('d')
		self.prueba
# class Tablero1(Tablero):
	# def __init__(self):
		# super().__init__(15,15)
	# def TableroFacil(self,images):
		
		# #super().prueba()
		# def render_square(image, key, texto='',color_button=('white','white')):
			# return sg.RButton(texto,image_filename=image,image_size=(30, 30), pad=(2,2),key=key,button_color=color_button)	
		# piece_image = images['BLANK']
		# i=4
		# j=5
		# row=[]
		# lista=[]
		# #lista.append()

		# color=('white','white')
		# lista.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
		
		# i=4
		# j=5
		# color=('white','violet')
		# lista.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		# #valor = super().render(piece_image['imagen'], key=(i,j))
		# # def render_square(image, key, texto=''):
			# # return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)
		# row.append(lista)			
		# return row
		
class Tablero1(Tablero):
	def __init__(self):
		super().__init__(15,15)
	def TableroFacil(self,images):
		####
		#super().prueba()
		#color_button=('white','white')#
		def render_square(image, key, texto='',color_button=('white','white')):
			return sg.RButton(texto,image_filename=image,image_size=(40, 40), pad=(2,2),key=key,button_color=color_button)	
		# piece_image = images['BLANK']
		# i=4
		# j=5
		# row=[]
		# lista=[]
		# #lista.append()

		# color=('white','white')
		# lista.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
		
		# i=4
		# j=5
		# color=('white','violet')
		# lista.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		#valor = super().render(piece_image['imagen'], key=(i,j))
		# def render_square(image, key, texto=''):
			# return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)
		
		tablero1=[]	
		for i in range(self._filas):
			row=[]
			#color_button=('white','white')#
			for j in range(self._columnas):
				piece_image = images['BLANK']
				valor=boardConfig1[i][j].get_valor()
				if valor == 3:
					#color_button=('white','green')#
					row.append(render_square(piece_image['imagen'],key =(i,j),texto='', color_button=('white','orange')))
					
				else:
					color_button=('white','white')
					row.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
				#row.append(render_square(piece_image['imagen'],key =(i,j),texto='',color_button=('white','red')))
			tablero1.append(row)
				
		#row.append(lista)			
		return tablero1		
		
		
class Tablero2(Tablero):
	def __init__(self):
		super().__init__(15,15)
	def TableroMedio(self,images):
		
		#super().prueba()
		def render_square(image, key, texto='',color_button=('white','white')):
			return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)	
		piece_image = images['B']
		i=4
		j=5
		row=[]
		lista=[]
		#lista.append()

		color=('white','white')
		lista.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
		
		i=4
		j=5
		color=('white','violet')
		lista.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		#valor = super().render(piece_image['imagen'], key=(i,j))
		# def render_square(image, key, texto=''):
			# return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)
		row.append(lista)			
		return row		
		
		
		
		
		
		

		#
		# Tab=[]
		# receptacle=[]
		# print(self._filas)
		# for i in range(self._filas):
			# for j in range(self._columnas):
				# color_button=('white','white')
				# piece_image= images['BLANK']
				# valor=boardConfig1[i][j].get_valor
				
				# if valor == 3:
					# color=boardConfig1[i][j].get_color()
					# color_button('white',color)
					# receptacle.append(render_square(piece_image['imagen'],key =(i,j),texto='PX3'))
				# elif valor == 1:
					# color=boardConfig1[i][j].get_color()
					# color_button('white',color)
					# receptacle.append(self.render_square(piece_image['imagen'],key =(i,j)))
				# elif valor ==2 :
					# color=boardConfig1[i][j].get_color()
					# color_button('white',color)
					# receptacle.append(self.render_square(piece_image['imagen'],key =(i,j),texto='P23'))
				# else:
					# receptacle.append(self.render_square(piece_image['imagen'],key =(i,j),texto=''))
			# #row.append(sg.Button('palabraX3',key=(i,j))
			# Tab.append(receptacle)								
		# return Tab		
# class tablero1(Tablero):
	# def __init__(self,filas,columnas)
# class Tablero2(Tablero):
	# def __init__(self):
		# super().__init__(16,16)
	# def TableroFacil(self,dic):
		# print(dic)
		# print("*"*30)
		# piece_image= dic['BLANK']			
# # obj=Tablero(13,15)
# obj.prueba2()
# dic={'ocup':False,'valor':False,'color':'','palabra':False,'letra':False,'puntosx':0}
# #obj = Tablero2(dic).TableroFacil()
# obj = Tablero2()
# obj.TableroFacil(dic)
# # print(obj)
obj = Tablero1()
# print(obj.TableroFacil(images))
tabla=obj.TableroFacil(images) 

obj2 = Tablero2()
#print(obj.TableroFacil(images))
tabla2=obj2.TableroMedio(images) 
board_tab=[[sg.Column(tabla)],[sg.Button('COMENZAR'),sg.Button('PASAR'),sg.Button('GUARDAR'),sg.Button('EXIT')]]
window = sg.Window('ScrabbleAr',default_button_element_size=(10,1), auto_size_buttons=False).Layout(board_tab)
button , value = window.Read()
board_tab2=[[sg.Column(tabla2)],[sg.Button('COMENZAR'),sg.Button('PASAR'),sg.Button('GUARDAR'),sg.Button('EXIT')]]
window = sg.Window('ScrabbleAr',default_button_element_size=(10,1), auto_size_buttons=False).Layout(board_tab2)


button , value = window.Read()
