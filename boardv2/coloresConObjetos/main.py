import tablero
import os.path

#tab=tablero.Tablero1(dic).TableroFacil()
base_path=os.path.dirname(os.path.abspath(__file__))
#os.path.join(base_path,'/imagenes/blank.png')
#blank = {'letra':'', 'imagen': r'blank.png'}
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
#b={'letra': 'B', 'imagen' : os.path_join(PATH, 'a.png')}
# b={'letra':'A','imagen': os.path.join(PATH,'a.png')}
# b={'letra':'B','imagen': os.path.join(PATH,'a.png')}
# c={'letra':'C','imagen': os.path.join(PATH,'a.png')}
# d={'letra':'D','imagen': os.path.join(PATH,'a.png')}

images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z}
dic={'ocup':False,'valor':False,'color':'','palabra':False,'letra':False,'puntosx':0}
#tab=tablero.Tablero2().TableroFacil(images)
tab=tablero.Tablero1().TableroFacil(images)

#print(tab)
