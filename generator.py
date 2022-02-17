# GENERA ARCHIVOS DE DIFERENTES TAMAÑOS
import os
import random
grupo = 1
for g in range(3):
	path = 'grupo_' + str(grupo) + '/'
	os.makedirs(os.path.dirname(path), exist_ok=True)
	print("group " + str(g))
	for x in range(100):
		with open(path + 'g' + str(grupo) + '_archivo_' + str(x+1), 'wt') as f:
			if grupo == 1:
				num_chars = random.randint(1, 1024*10)
			elif grupo == 2:
				num_chars = random.randint(1024*10, 1024*1000)
			elif grupo == 3:
				num_chars = random.randint(1024*1000, 1024*10000)
			else:
				break
			f.write('0' * num_chars)
		if x + 1  == 100:
			grupo = grupo + 1
		pass
	pass