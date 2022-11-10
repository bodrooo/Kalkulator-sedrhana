print('ini adalah Kalkulator sedrhana buatan saya!')

print('__MENU__')
print('[1] Perkalian')
print('[2] Pembagian')
print('[3] Penjumlahan')
print('[4] Pengurangan')
print('_______________')
pilih = input('Pilih: ')

if pilih == '1':
    x = int(input('Massukkan angka: '))
    y = int(input('Massukkan angka: '))
    print(x * y)
    
if pilih == '2':
    x = int(input('Massukkan angka: '))
    y = int(input('Massukkan angka: '))
    print(x / y)   

if pilih == '3':
    x = int(input('Massukkan angka: '))
    y = int(input('Massukkan angka: '))
    print(x + y)
  
if pilih == '4':
    x = int(input('Massukkan angka: '))
    y = int(input('Massukkan angka: '))
    print(x - y) 