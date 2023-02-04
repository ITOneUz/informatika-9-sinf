# parolni kirituvchi dastur
# import time
from time import sleep

parol = '12345'
sanoq = 0
kutish_vaqti = 3

while True:
	check_parol = input("Parolni kiriting: ")
	if (parol != check_parol):
		sanoq = sanoq + 1
	else:
		print("Parol to'g'ri kiritildi!")
		break
	if (sanoq % 3 == 0):
		print('Siz xato parol kiritdiz. ozgina kuting!')
		# time.sleep(kutish_vaqti)

		temp = kutish_vaqti
		while temp > 0:
			print(temp, "sekund qoldi")
			sleep(1)
			temp = temp - 1