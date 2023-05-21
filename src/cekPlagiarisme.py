from function import *
from prettytable import PrettyTable
import os
stop = False
while(stop==False):
    print("░█████╗░███████╗██╗░░██╗  ██████╗░██╗░░░░░░█████╗░░██████╗░██╗░█████╗░██████╗░██╗░██████╗███╗░░░███╗███████╗")
    print("██╔══██╗██╔════╝██║░██╔╝  ██╔══██╗██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗██║██╔════╝████╗░████║██╔════╝")
    print("██║░░╚═╝█████╗░░█████═╝░  ██████╔╝██║░░░░░███████║██║░░██╗░██║███████║██████╔╝██║╚█████╗░██╔████╔██║█████╗░░")
    print("██║░░██╗██╔══╝░░██╔═██╗░  ██╔═══╝░██║░░░░░██╔══██║██║░░╚██╗██║██╔══██║██╔══██╗██║░╚═══██╗██║╚██╔╝██║██╔══╝░░")
    print("╚█████╔╝███████╗██║░╚██╗  ██║░░░░░███████╗██║░░██║╚██████╔╝██║██║░░██║██║░░██║██║██████╔╝██║░╚═╝░██║███████╗")
    print("░╚════╝░╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░░░░╚═╝╚══════╝")
    print("------------------------------------------------------------------------------------------------------------")
    print("Selamat Datang di Cek Plagiarisme Ala Sulthan Dzaky Alfaro")
    print("Pengecekan ini tidaklah sempurna jadi jangan 100% dipercayai :D")
    print("Contoh masukan file : test.txt")
    print("Atau path dari file yang akan di test,agar terhindar dari eror")
    print("Contoh : D:\\Makalah\\file.txt")
    inptteks1 = input("Masukkan file teks 1 = ")
    inptteks2 = input("Masukkan file teks 2 = ")
    try:
        hasilfinal,kmp11,kmp12,kmp21,kmp22,kttks1,kttks2,prsnt1,prsnt2 = getpersentage(inptteks1,inptteks2)
        print("Presentase plagiarisme antara "+os.path.basename(inptteks1)+" dan "+os.path.basename(inptteks2)+" sekitar = "+str(hasilfinal))
        cek = input("Apakah anda ingin melihat detail dari pengecekan?(y/n) = ")
        if(cek=="Y" or cek=="y"):
            print("-----------------------------------------------------")
            print(os.path.basename(inptteks1)+" terhadap "+os.path.basename(inptteks2))
            str1 = "Kata "+os.path.basename(inptteks1)
            str1kmp1 = "KMP "+os.path.basename(inptteks1)
            str1kmp2 = "KMP "+os.path.basename(inptteks2)
            prstksm1 = "Presentase Kesamaan(%)"
            tampung1 = [[str1,str1kmp1,str1kmp2,prstksm1]]
            for i in range(len(kttks1)):
                tampung1.append([kttks1[i],kmp11[i],kmp12[i],prsnt1[i]])
            tab1 = PrettyTable(tampung1[0])
            for i in range(1,len(tampung1)):
                tab1.add_row(tampung1[i])
            print(tab1)
            print("Rata-rata presentase kesamaan = ",str(rataArr(prsnt1)))
            print("-----------------------------------------------------")
            print(os.path.basename(inptteks2)+" terhadap "+os.path.basename(inptteks1))
            str2 = "Kata "+os.path.basename(inptteks2)
            str2kmp1 = "KMP "+os.path.basename(inptteks1)
            str2kmp2 = "KMP "+os.path.basename(inptteks2)
            prstksm2 = "Presentase Kesamaan(%)"
            tampung2 = [[str2,str2kmp1,str2kmp2,prstksm2]]
            for i in range(len(kttks2)):
                tampung2.append([kttks2[i],kmp21[i],kmp22[i],prsnt2[i]])
            tab2 = PrettyTable(tampung2[0])
            for i in range(1,len(tampung2)):
                tab2.add_row(tampung2[i])
            print(tab2)
            print("Rata-rata presentase kesamaan = ",str(rataArr(prsnt2)))
            print("Jadi presentase kemiripan antara 2 file = "+str(hasilfinal))
        else:
            print("Ok,detail pengecekan tidak ditampilkan")
        mllg = input("Apakah anda ingin mengecek plagiarisme lagi?(y/n) = ")
        if(mllg=="Y" or mllg=="y"):
            stop = False
            os.system('cls')
        else:
            print("Ok, program akan berhenti. Terima kasih telah menggunakan program ini")
            stop = True

    except:
        os.system('cls')
        print("Masukan file ada yang salah. Cek lagi directory atau tempat file yang kamu ingin test")
