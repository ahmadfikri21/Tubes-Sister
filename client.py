import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://127.0.0.1:8008', allow_none=True)

print("===== Pilih Klinik =====")
print("1. Klinik Sukapura")
print("2. Klinik Sukabirus")
print("3. Klinik Telkom")
answer = input('Pilih : ')

print("\n === Masukkan data diri ===\n")

if answer == '1':
    klinik = "Klinik Sukapura"
elif answer == '2':
    klinik = "Klinik Sukabirus"
elif answer == '3':
    klinik = "Klinik Telkom"

noRekam = input("Nomor Rekam Medis : ")
nama = input("Nama : ")
tanggalLahir = input("Tanggal Lahir : ")

hasil = s.registrasi(noRekam,nama,tanggalLahir,klinik)

print("Nomor Antrian :",hasil[0])
print("Waktu Tunggu :",hasil[1]," Menit")

print(s.seeList())

hasil = s.lihatAntrian("002","Klinik Sukapura")

print("Nomor Antrian anda adalah ",hasil[5])
print("Anda harus Menunggu ",hasil[5]-1," Antrian Lagi")