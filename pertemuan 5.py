hari = []
while True:
    print('Masukan Hari kuliah anda ' + str(len(hari) + 1) +
          ' (untuk mengakhiri program ini kosongkan.):')
    nama = input()
    if nama == '':
        break
hari = hari + [nama]  # list concatenation
print('hari kuliah anda adalah:')
for nama in hari:
    print(' ' + nama)
