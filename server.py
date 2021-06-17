from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime,timedelta
import time

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
with SimpleXMLRPCServer(("127.0.0.1",8008), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()
    
    antrian = []   
    iterasi = 0
    
    def registrasi(noRekam,nama,tanggalLahir,klinik):
        global iterasi

        # untuk menyimpan data yang diinputkan user kedalam variabel
        antrian.append([])
        antrian[iterasi].append(noRekam)
        antrian[iterasi].append(nama)
        antrian[iterasi].append(tanggalLahir)
        antrian[iterasi].append(klinik)
        # menentukan jam masuk praktek
        antrian[iterasi].append((datetime.now() + timedelta(hours = 1)).strftime("%H:%M:%S"))

        noAntrian = hitungAntrian(antrian,klinik)
        antrian[iterasi].append(noAntrian)

        iterasi += 1

        if noAntrian == 0:
            waktuTunggu = 0
            noAntrian += 1
        else:
            now = datetime.now().strftime("%H:%M:%S")
            waktuTunggu = iterasi*60
        
        arr = [noAntrian,waktuTunggu]

        return arr

    def seeList():
        return antrian

    def hitungAntrian(arr,key):
        jumlah = 0
        for j in range(len(arr)):
            for k in range(len(arr[j])):
                if arr[j][k] == key:
                    jumlah += 1
        return jumlah

    def lihatAntrian(noRekam,klinik):
        global antrian
        for j in range(len(antrian)):
            # untuk mengecek klinik dan no rekam medis dari array
            if antrian[j][3] == klinik and antrian[j][0] == noRekam:
                return antrian[j]
        return False


    server.register_function(registrasi, 'registrasi')
    server.register_function(seeList, 'seeList')
    server.register_function(lihatAntrian, 'lihatAntrian')
    
    print("Serving.....")
    # while True:
    #     print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    #     time.sleep(1)
    
    server.serve_forever()