# diccionarios
# MANTIENEN EL ORDEN DE INGRESO
# ES MUTABLE
# LAS CLAVES SON UNICAS
# EL ACCESO A UN VALOR ES SUPER RAPIDO

# listas         []
# tupla          ()
# diccionario    {}
# conjunto {}

rae1 = {}

rae = {
    'casa': 'lugar donde viven las personas',
    'perro': 'mascota de las personas',
    'puerta': 'elemento que cierra la casa'
}

# conjunto
kino = {4, 5, 6, 7, 8}

print(rae.get('perro'))

mi_primer_set = set()
mi_primer_set.add('uno')
mi_primer_set.add('dos')
mi_primer_set.add('tres')

mi_primer_set.remove('uno')
print(mi_primer_set)

beatles = {'Lennon', 'McCartney', 'Ringo', 'Harrison'}

print('Lennon' in beatles)
