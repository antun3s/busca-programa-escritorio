import os
import re

#os.system('@chcp 65001')
#os.system('dir /s /b /o:gn > C:\file-list.txt')

''''
prog = [
    ['RFB','RFB.*irpf.jar|IFPF[0-9]{4}\\\\aplicacao\\\\dados\\\\[0-9]{11}'],
    ['Certificados','.pfx$'],
    ['DCTF','DCTFMensal[0-9]{2}.exe$'],
    ['DIRF','Dirf[0-9]{4}.exe$|Dirf2015\\\\DADOS$'],
    ['GCAP','GCAP.jar$|GCAP[0-9]{4}\\\\aplicacao\\\\dados\\\\[0-9]{11}'],
    ['ITR','pgditr.jar$|ITR[0-9]{4}\\\\aplicacao\\\\dados\\\\[0-9]{11}'],
    ['PERDCOMP','PERDCOMP[0-9]{2}.exe$|PERDCOMP[0-9]{2}\Documentos Gravados$|PERDCOMP_TABELAS.mdb'],
    ['SPED-ECF','SpedEcf.exe$|Programas SPED\\\\ECF\\\\mysql\\\\data$'],
    ['SPED-Contabil','Sped\ Contabil.exe$|\\\\SpedContabil\\\\mysql\\\\data$']
    ]

'''
prog = [
    ['SPED-Contabil','Sped\ Contabil.exe$|\\\\SpedContabil\\\\mysql\\\\data$']
    ]   


def search_line(pattern, file1):
    for i, line in enumerate(file1):  
        for match in re.finditer(pattern, line):
            print ( line ,end='')

for x in range(len(prog)):
    # load file to search
    #file = open('file-list.txt', 'r', encoding="utf8")
    file = open('file-list-gfisco.txt', 'r', encoding="utf8")
    
    
    print ('# Searching for', prog[x][0],':')
    pattern = re.compile( prog[x][1] )
    print (pattern)
    search_line(pattern,file)