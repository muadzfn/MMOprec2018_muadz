def checkID():
    print("masukkan nim: ")
    nim = str(int(input()))
    if len(nim) == 10:
        print(nim[0],"adalah kode universitas")
        print(nim[1:3],"adalah kode fakultas")
        print(nim[3],"adalah kode jurusan")
        print(nim[4:6],"adalah kode angkatan")
        print(nim[6:10],"adalah kode mahasiswa")
    else:
        print("nim tidak 10 digit")
        checkID()
checkID()
