import re
from prettytable import PrettyTable
def KMP(kata,text):
    ubahkata = kata.lower()
    ubahtext = text.lower()
    panjangkata = len(kata)
    panjangtext = len(text)
    border = boderFunction(kata)
    i = 0
    j = 0
    indexhasil = []
    while((len(text)-i)>=(len(kata)-j)):
        if(ubahkata[j]==ubahtext[i]):
            i+=1
            j+=1
        if(j==panjangkata):
            indexhasil.append(i-j)
            j = border[j-1]
        elif(i<panjangtext and ubahkata[j]!=ubahtext[i]):
            if(j!=0):
                j = border[j-1]
            else:
                i+=1
    return indexhasil
            


def isArrSame(arr1,arr2):
    if(len(arr1)!=len(arr2)):
        return False
    else:
        for i in range(len(arr1)):
            if(arr1[i]!=arr2[i]):
                return False
        return True
def boderFunction(kata):
    if(len(kata)==0):
        return []
    else:
        border = [0 for i in range(len(kata))]
        border[0] = 0
        if(len(kata)==1):
            return border
        else:
            maks = 1
            while(maks<len(kata)):
                simpan = 0
                arrpref = []
                for i in range(maks+1):
                    arrpref.append(kata[i])
                    arrsuff = []
                    acuan = 0
                    if(maks-i == 0):
                        acuan = 1
                    else:
                        acuan = maks-i
                    for j in range(maks,acuan-1,-1):
                        arrsuff.insert(0,kata[j])
                    if(isArrSame(arrpref,arrsuff)):
                        simpan = i+1
                border[maks] = simpan
                maks+=1
        return border
def notDuplicate(arr):
    hasil = []
    for i in range(len(arr)):
        if(arr[i] not in hasil):
            hasil.append(arr[i])
    return hasil
def bacatxt(namafile):
    file = open(namafile,'r')
    text = file.read()
    file.close()
    return text
def bacatxttoarr(namafile):
    file = open(namafile,'r')
    text = file.read()
    file.close()
    clean = re.sub(r'[^a-zA-Z0-9\s\-]', '', text)
    hasil = clean.split()
    akhir = notDuplicate(hasil)
    return akhir
def rataArr(arr):
    jml = 0
    for i in range(len(arr)):
        jml+=arr[i]
    hasil = jml/len(arr)
    return hasil
def getpersentage(namafile1,namafile2):
    str1 = bacatxt(namafile1)
    str2 = bacatxt(namafile2)
    arr1 = bacatxttoarr(namafile1)
    arr2 = bacatxttoarr(namafile2)
    hasilteks1 = []
    hasilteks2 = []
    hasilkmp11arr = []
    hasilkmp21arr = []
    hasilkmp1arr = []
    hasilkmp2arr = []
    #KMP Teks 1
    for i in range(len(arr1)):
        hasilkmp11 = KMP(arr1[i],str1)
        hasilkmp11arr.append(len(hasilkmp11))
        hasilkmp21 = KMP(arr1[i],str2)
        hasilkmp21arr.append(len(hasilkmp21))

        minim = min(len(hasilkmp11),len(hasilkmp21))
        maksim = max(len(hasilkmp11),len(hasilkmp21))
        if(maksim==0):
            hasilteks1.append(0)
        else:
            hasilteks1.append(minim/maksim*100)

    #KMP Teks 2
    for i in range(len(arr2)):
        hasilkmp1 = KMP(arr2[i],str1)
        hasilkmp1arr.append(len(hasilkmp1))
        hasilkmp2 = KMP(arr2[i],str2)
        hasilkmp2arr.append(len(hasilkmp2))
        minim = min(len(hasilkmp1),len(hasilkmp2))
        maksim = max(len(hasilkmp1),len(hasilkmp2))
        if(maksim==0):
            hasilteks2.append(0)
        else:
            hasilteks2.append(minim/maksim*100)
    #Rata-rata
    rata1 = rataArr(hasilteks1)
    rata2 = rataArr(hasilteks2)
    hasilakhir = (rata1+rata2)/2
    return hasilakhir,hasilkmp11arr,hasilkmp21arr,hasilkmp1arr,hasilkmp2arr,arr1,arr2,hasilteks1,hasilteks2

    

# arr = ["coba","mencoba","tanya","mentanya","kerja","bekerja","digital","digitalisasi","digitalisir","digitalisasi","digital"]
# hasil = deleteSubset(arr)
# print(hasil)

# print(bacatxt("D:\\python\\Makalah Stima\\test.txt"))
# hasil = ("D:\\python\\Makalah Stima\\test.txt")
# hasil2 = ("D:\\python\\Makalah Stima\\test2.txt")
# hasilakhir,arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8 = getpersentage(hasil,hasil2)
# print(len(arr1))
# print(len(arr2))
# print(len(arr3))
# print(len(arr4))
# print(len(arr5))
# print(len(arr6))
# print(len(arr7))
# print(len(arr8))
# tampung = [["Kata teks1","KMP teks 1","KMP teks 2","Presentase kesamaan"]]
# for i in range(len(arr5)):
#     tampung.append([arr5[i],arr1[i],arr2[i],arr7[i]])
# tab = PrettyTable(tampung[0])
# for i in range(1,len(tampung)):
#     tab.add_row(tampung[i])
# print("Hasil rata rata = ",rataArr(arr7))
# print(tab)
# print(hasilakhir)





