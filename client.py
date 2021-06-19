import xmlrpc.client
import os

s = xmlrpc.client.ServerProxy('http://127.0.0.1:8008', allow_none=True)

def PilihKlinik():
	os.system("CLS")
	global klinik
	print("=====================================")
	print("=========> Selamat Datang <==========")
	print("======__________________________=====")

	# untuk menampilkan pilihan klinik
	print("=====|  Silahkan Pilih Klinik   |====")
	print("=====|  1. Klinik Sukapura      |====")
	print("=====|  2. Klinik Sukabirus     |====")
	print("=====|  3. Klinik Telkom        |====")
	print("=====|__________________________|====")
	print("=====================================")
	print("=====> Masukkan Pilihan Anda <=======")
	print("=====================================")

	# untuk menyimpan jawaban dari inputan user
	answer = input('=======> Pilihan Anda: ')

	# kondisi untuk menentukan klinik sesuai dengan answer dari user
	if answer == '1':
		klinik = "Klinik Sukapura"
	elif answer == '2':
	   	klinik = "Klinik Sukabirus"
	elif answer == '3':
	   	klinik = "Klinik Telkom"
	
def DataMedis():
	os.system("CLS")
	global noRekam, nama, tanggalLahir
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
	print("=======================================")
	print("=====================================")
	print("===== Tekan Enter Untuk Kembali =====")
	print("=====================================")
	input()

#MAIN
PilihKlinik();
DataMedis();

#function yang diambil dari server
print()
print("Berikut adalah data medis yang ada pada seluruh klinik yang kami miliki:")
print(s.seeList())
print("=====> Mohon ditunggu <=======")
# hasil = s.lihatAntrian("002","Klinik Sukapura")

# print("Nomor Antrian anda adalah ",hasil[5])
# print("Anda harus Menunggu ",hasil[5]-1," Antrian Lagi")