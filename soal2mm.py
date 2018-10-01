def buatMatriks():
    m1 = []
    print('baris matriks: ',end='')
    m = int(input())
    print('kolom matriks: ',end='')
    n = int(input())
    print('nilai matriks perbaris dipisah dengan koma')
    for i in range(m):
        m1.append(list(map(int, input().split(","))))
    return m1

def jumlahMatriks(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        for i in range(0, len(m1)):
            for j in range(0, len(m1[0])):
                print(m1[i][j]+m2[i][j], end=' ')
            print(' ')
    else:
        print("matriks tidak dapat dijumlah")

def kurangMatriks(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        for i in range(0, len(m1)):
            for j in range(0, len(m1[0])):
                print(m1[i][j]-m2[i][j], end=' ')
            print(' ')
    else:
        print("matriks tidak dapat dikurang")

def kaliMatriks(m1,m2,result):
    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
         for j in range(len(m2[0])):
          for k in range(len(m2)):
           result[i][j] += m1[i][k] * m2[k][j]        
        return result
    else:
        print("matriks tidak dapat dikali")

def pangkatMatriks(m1,pangkat):
    if len(m1)==len(m1[0]):
        for i in range(1,pangkat):
            result = [[0for j in range(len(m1[0]))]for i in range(len(m1))]
            m1 = kaliMatriks(m1,m1,result)
        for r in result:
         print(r)
    else:
        print("matriks tidak dapat dipangkatkan")
        
def menu():
    print("Operasi Matriks")
    print("1. penjumlahan Matriks")
    print("2. pengurangan Matriks")
    print("3. Perpangkatan Matriks")
    print("4.exit")
    pilihan(input())
    
def pilihan(x):
    if x == "1":
        m1 = buatMatriks()
        m2 = buatMatriks()
        jumlahMatriks(m1,m2)
        menu()
    elif x == "2":
        m1 = buatMatriks()
        m2 = buatMatriks()
        kurangMatriks(m1,m2)
        menu()
    elif x == "3":
        m1 = buatMatriks()
        print("nilai pangkat")
        pangkat = int(input())
        pangkatMatriks(m1,pangkat)
        menu()
    elif x == "4":
        exit()
    else:
        menu()
menu()
