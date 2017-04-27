# -*-coding:utf-8 -*-
import requests
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def fenci(argv='/home/qin/zuoye/太空旅客.txt'):
    oFilePath = '/home/qin/zuoye/fenci/'
    filename = argv
    f = open(filename,'r')
    file_read = f.read()
    f.close()
    fen_list = jieba.cut(file_read,cut_all=True)
    result = []
    # fen_list_tolist = list(fen_list)
    for fen in fen_list:
        # sys.stdout.write(fen.encode('utf-8') + ',')
        fen = ' '.join(fen.split())
        if(fen != ''and fen != "\n" and fen != "\n\n" and fen.isdigit()!=True and len(fen)>2):
            result.append(fen)
            # print fen
    #print result[0]
    filename = '太空旅客.txt'
    f = open(oFilePath+filename,"w")
    # f.write('lalalalalala')
    f.write(' '.join(result)+'lalaal')
    f.close()
    # with open(oFilePath+filename,"w") as writeFile:  # 这个地方‘a'是追加’w‘是覆盖
    #     writeFile.write(''.join(result))

def Tfidf(filelist):
    path = '/home/qin/zuoye/fenci/'
    ppath = '/home/qin/zuoye/'
    ppp = []
    fname = path + filelist
    fff = open(fname,'r')

    filekeyword = open(path+'作业结果.txt','a')
    filecontents = fff.readlines()
    fff.close()
    dictTFIDF = {}
    wordsum = 0
    for line in filecontents:
        for word in line.split():
            wordsum+=1
            if dictTFIDF.has_key(word):
                dictTFIDF[word]+=1
            else:
                dictTFIDF[word]=1

    for word in dictTFIDF:
        # if(word=='表姐'):
        #     print word
        #     print dictTFIDF[word]
        # if(word=='爱情'):
        #     print word
        #     print dictTFIDF[word]
        dictTFIDF[word]=1.0*dictTFIDF[word]/wordsum
        IDF = 1/1
        dictTFIDF[word]*=IDF

    L = sorted(dictTFIDF.items(),key=lambda asd:asd[1],reverse=True)

    filekeyword.write('出现次数最多的十个三个字的词：\n')
    for keyword in L[0:10]:
        filekeyword.write(keyword[0]+' '+'TFIDF值：'+str(keyword[1])+' '+'出现次数：'+str(keyword[1]*wordsum)+'\n')
    filekeyword.close()
fenci()
Tfidf('太空旅客.txt')