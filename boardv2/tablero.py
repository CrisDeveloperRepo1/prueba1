import PySimpleGUI as sg
import random
import coloresTablero
import os.path
tab=coloresTablero.tablero
#sg.ChangeLookAndFeel('Dark purple')
sg.theme('Dark Blue')
base_path=os.path.dirname(os.path.abspath(__file__))
#os.path.join(base_path,'/imagenes/blank.png')
#blank = {'letra':'', 'imagen': r'blank.png'}
blank = {'letra':'', 'imagen': os.path.join(base_path,'imagenes/blank.png')}
a={'letra':'A','imagen': os.path.join(base_path,'a.png')} #(r'img.png')
b={'letra':'B','imagen': os.path.join(base_path,'b.png')}
c={'letra':'C','imagen': os.path.join(base_path,'c.png')}
d={'letra':'D','imagen': os.path.join(base_path,'d.png')}
e={'letra':'E','imagen': os.path.join(base_path,'e.png')}
f={'letra':'F','imagen': os.path.join(base_path,'f.png')}
g={'letra':'G','imagen': os.path.join(base_path,'g.png')}
h={'letra':'H','imagen': os.path.join(base_path,'h.png')}
i={'letra':'I','imagen': os.path.join(base_path,'i.png')}
j={'letra':'J','imagen': os.path.join(base_path,'j.png')}
k={'letra':'K','imagen': os.path.join(base_path,'k.png')}
l={'letra':'L','imagen': os.path.join(base_path,'l.png')}
m={'letra':'M','imagen': os.path.join(base_path,'m.png')}
n={'letra':'N','imagen': os.path.join(base_path,'n.png')}
o={'letra':'O','imagen': os.path.join(base_path,'o.png')}
p={'letra':'P','imagen': os.path.join(base_path,'p.png')}
q={'letra':'Q','imagen': os.path.join(base_path,'q.png')}
r={'letra':'R','imagen': os.path.join(base_path,'r.png')}
s={'letra':'S','imagen': os.path.join(base_path,'s.png')}
t={'letra':'T','imagen': os.path.join(base_path,'t.png')}
u={'letra':'U','imagen': os.path.join(base_path,'u.png')}
v={'letra':'V','imagen': os.path.join(base_path,'v.png')}
w={'letra':'W','imagen': os.path.join(base_path,'w.png')}
x={'letra':'X','imagen': os.path.join(base_path,'x.png')}
y={'letra':'Y','imagen': os.path.join(base_path,'y.png')}
z={'letra':'Z','imagen': os.path.join(base_path,'z.png')}
# im=r'g.png'
# img=r'blank2.png'####
img=os.path.join(base_path,'blank2.png')
#b={'letra': 'B', 'imagen' : os.path_join(PATH, 'a.png')}
# b={'letra':'A','imagen': os.path.join(PATH,'a.png')}
# b={'letra':'B','imagen': os.path.join(PATH,'a.png')}
# c={'letra':'C','imagen': os.path.join(PATH,'a.png')}
# d={'letra':'D','imagen': os.path.join(PATH,'a.png')}
color_button=('white','white')
images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z}

initial_atril=[]
images_keys= list(images.keys())
images_keys.remove('BLANK')


for i in range(0,7):
	initial_atril.append(random.choice(images_keys))


def render_square(image, key, texto=''):
	return sg.RButton(texto,image_filename=image,image_size=(50, 50) ,size=(2,2), pad=(2,2),key=key,button_color=color_button) ##size 2,2 
	
tablero=[]
for i in range(15):  ### tablero botones
	row=[]
	for j in range(15):
		#color_button=('white','white')
		color_button=('white','white')

		piece_image = images['BLANK']
		dd=tab[i][j]
		if dd['color']== 'red':
					
				color_button=('white','red')
				### me gustaria agregarlo aca  palabrax3
				row.append(render_square(piece_image['imagen'],key = (i,j), texto='PX3')) ### aca agrego los botones a la matriz
		# elif dd['color']=='orange':
				# color_button=('white','blue')
				# row.append(render_square(piece_image['imagen'],key = (i,j)))			
		elif dd['color']=='violet':
			    #corona=r'corona.png'
				color_button=('white','Dark violet')
				corona=r'corona.png'
				row.append(render_square(corona,key = (i,j)))			
		elif dd['color']=='orange':
				color_button=('white',dd['color'])
				row.append(render_square(piece_image['imagen'],key = (i,j),texto='PX2'))
				
		else:
			row.append(render_square(piece_image['imagen'],key = (i,j)))
			#row.append(sg.Button('palabraX3',key=(i,j))	
	tablero.append(row)
color_button=('white','white')	
#print(tablero)	
	
## botones del atril

atril = []
atril2 = []
for i in range(7):
	row = []
	piece_image = images[initial_atril[i]]
	row.append(render_square(piece_image['imagen'],key = i))
	atril.append(row)###	
	
#print(atril)
#inte=r'interrogacion.png'
inte=os.path.join(base_path,'interrogacion.png')
for i in range(7):
	row = []
	#piece_image = images[initial_atril[i]]
	row.append(render_square(inte,key = i))
	atril2.append(row)###	

columna_3 = [ [sg.Text('PUNTOS MAQUINA')],[sg.Listbox(values =[], key='datosj', size=(30,10))]]
columna_1 = [ [sg.Text('PUNTOS JUGADOR')],[sg.Listbox(values =[], key='datosm', size=(30,10))]]	
#maquina=[sg.Text('PUNTOS MAQUINA')]	
board_tab=[[sg.Button('CHECK')],[sg.Column(columna_1),sg.Column(atril), sg.Column(tablero), sg.Column(atril2),sg.Column(columna_3)],[sg.Button('COMENZAR'),sg.Button('PASAR'),sg.Button('GUARDAR'),sg.Button('EXIT')]]
window = sg.Window('ScrabbleAr',default_button_element_size=(10,1), auto_size_buttons=False).Layout(board_tab)
#indow = sg.Window('tablero', layout, default_button_element_size=(5,2), auto_size_buttons=False)
#event, value = window.Read()
palabra=''
while True:
	letra=''
	l=-1
	button , value = window.Read()
	if button == 'CHECK':
		if palabra == '':
			sg.Popup('todavia no formo una palabra')
		else:
		    print(palabra)
		# if len(word)>= 2 and len(word) <=7:
	if button in (None , 'EXIT'):
		exit()		
	if type(button) is int:
		
		if initial_atril[button] !='':
			letra= initial_atril[button]
			palabra += letra
		
			initial_atril[button]=''
			texto=''
			window[button].update(texto,image_filename=img,image_size=(50, 50), button_color=('',''))##
			button , value = window.Read()
			if type(button) is tuple:
	
				image1= images[letra]
				image1=image1['imagen']
		
				#render_square(image1['imagen'],key=(0,0))
				texto=''
				window[button].update(texto,image_filename=image1,image_size=(50, 50) ,button_color=('white','grey'))
				l=0
			# piece_image = images['BLANK']
		# row.append(render_square(piece_image['imagen'],key = (i,j)))	
		
		
		
	if type(button) is tuple:
		if l ==-1:
			
			sg.Popup('movimiento incorrecto')
