import xmlrpc.client
import os

s = xmlrpc.client.ServerProxy('http://127.0.0.1:8008', allow_none=True)

def HomePage():
	while True:
		os.system("CLS")
		print("==========> Bagian Homepage <========")
		print("=====================================")
		print("======__________________________=====")
		print("=====|           Menu           |====")
		print("=====|  1. Pilih Klinik         |====")
		print("=====|  2. Lihat Data Antrian   |====")
		print("=====|     Seluruh Klinik       |====")
		print("=====|  3. Cari Klinik dan      |====")
		print("=====|     Lihat Data Antrian   |====")
		print("=====|  4. Cari Antrian         |====")
		print("=====|  0. Exit                 |====")
		print("=====|__________________________|====")
		print("=====================================")
		print("=====> Masukkan Pilihan Anda <=======")
		print("=====================================")
		# untuk menyimpan jawaban dari inputan user
		answer = input('=======> Pilihan Anda: ')

		# kondisi pilihan homepage
		if answer == '1':
			PilihKlinik()
		elif answer == '2':
			s.refreshUrutan()
			print()
			print("Berikut adalah data medis yang ada pada seluruh klinik yang kami miliki:")
			print(s.seeList())
			print()
			print("=====> Mohon ditunggu <=======")			
			input()
		elif answer == '3':
			lihatAntrianKlinik()
			input()
		elif answer == '4':
			cariAntrian()
			input()
		elif answer == '0':
		   	AreYouSure()
		   	os.system("CLS")
		   	break
		else:
			print()
			print("====> Masukkan Pilihan Anda dengan benar  <====")
			print("===============================================")
			print("=======> TEKAN ENTER UNTUK MELANJUTKAN <=======")
			print("===============================================")
			input()
			os.system("CLS")

def AreYouSure():
	print("=======================================================")
	print("Apakah kamu benar-benar ingin meninggalkan homepage ?")
	print(" 1. Ya")
	print(" 2. Tidak")
	print("=======================================================")
	answer = input('=======> Pilihan Anda: ')

	# kondisi pilihan homepage
	if answer == '1':
		print()
		print("======================> Sekian Terima Kasih Dan Sampai Jumpa <======================")
		input()
	elif answer == '2':
		HomePage()

def PilihKlinik():
	while True:
		os.system("CLS")
		global klinik
		print("========> Bagian Pilih Klinik <======")
		print("=====================================")
		print("=========> Selamat Datang <==========")
		print("======__________________________=====")

		# untuk menampilkan pilihan klinik
		print("=====|  Silahkan Pilih Klinik   |====")
		print("=====|  1. Klinik Sukapura      |====")
		print("=====|  2. Klinik Sukabirus     |====")
		print("=====|  3. Klinik Telkom        |====")
		print("=====|  0. Exit                 |====")
		print("=====|__________________________|====")
		print("=====================================")
		print("=====> Masukkan Pilihan Anda <=======")
		print("=====================================")

		# untuk menyimpan jawaban dari inputan user
		answer = input('=======> Pilihan Anda: ')

		# kondisi untuk menentukan klinik sesuai dengan answer dari user
		if answer == '1':
			klinik = "Klinik Sukapura"
			DataMedis()
		elif answer == '2':
		   	klinik = "Klinik Sukabirus"
		   	DataMedis()
		elif answer == '3':
		   	klinik = "Klinik Telkom"
		   	DataMedis()
		elif answer == '0':
			HomePage()
			break
		else:
			print()
			print("====> Masukkan Pilihan Anda dengan benar! <====")
			print("===============================================")
			print("=======> TEKAN ENTER UNTUK MELANJUTKAN <=======")
			print("===============================================")
			input()
			os.system("CLS")
	
def DataMedis():
	os.system("CLS")
	global noRekam, nama, tanggalLahir
	print("==========> Bagian Data Medis <========")
	print("=======================================")
	print("=====> Masukkan Data diri Anda <=======")
	# untuk menyimpan jawaban data medis dari user
	noRekam = input("Nomor Rekam Medis : ")
	nama = input("Nama : ")
	tanggalLahir = input("Tanggal Lahir : ")

	# untuk menjalankan fungsi registrasi dari server
	hasil = s.registrasi(noRekam,nama,tanggalLahir,klinik)

	# menampilkan nomor antrian dan waktu tunggu
	print("Nomor Antrian :",hasil[0])
	print("Waktu Tunggu :",hasil[1]," Menit")
	print("===============================================")
	print("=======> TEKAN ENTER UNTUK MELANJUTKAN <=======")
	print("===============================================")
	input()

def lihatAntrianKlinik():
	os.system("CLS")
	print("==> Bagian Lihat Antrian di Klinik  <==")
	print("=======================================")
	print("=====> Masukkan Data diri Anda <=======")
	NoRekam = input("Nomor Rekam Medis : ")
	Klinik = input("Klinik : ")
	hasil = s.lihatAntrian(NoRekam,Klinik)
	if hasil == False:
		print("Maaf data antrian anda tidak ditemukan di ",Klinik)
	else:
		print(hasil)
	print()
	print("===============================================")
	print("=======> TEKAN ENTER UNTUK MELANJUTKAN <=======")
	print("===============================================")

def cariAntrian():
    os.system("CLS")
    print("========> Bagian Cari Antrian  <=======")
	print("=======================================")
	print("=====> Masukkan Data diri Anda <=======")
    # nama klinik
    k = input("Nama Klinik : ")
    # no rekam medis
    nk = input("No Rekam Medis : ")
    tunggu,hasil = s.lihatAntrian(nk,k)

    if hasil == False:
        print("Maaf data antrian anda tidak ditemukan di seluruh klinik")
    else:
        print("Nomor Antrian anda adalah ",hasil)
        print("Anda harus Menunggu ",tunggu," Antrian Lagi")

#MAIN
os.system("CLS")
HomePage()
# PilihKlinik()
# DataMedis()
# cariAntrian();
# s.refreshUrutan()

#function yang diambil dari server
# print()
# print("Berikut adalah data medis yang ada pada seluruh klinik yang kami miliki:")
# print(s.seeList())
# print("=====> Mohon ditunggu <=======")