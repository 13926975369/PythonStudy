# -*-coding:utf-8 -*-
import requests
import jieba
import sys
import re
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
        if(fen != ''and fen != "\n" and fen != "\n\n" and fen.isdigit()!=True and len(fen)>0):
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

def pipei(argv='/home/qin/zuoye/fenci/作业的另一种可能格式.txt',fname='/home/qin/zuoye/fenci/太空旅客分好词的版本.txt'):
    dictpipei={}
    path = '/home/qin/zuoye/词典/'
    allpath = '角色/ 剧情/ 视听/ 制作/ 主题/ '
    alljuese ='反派.txt 角色.txt 角色中的其他.txt 男主角.txt 女主角.txt 配角.txt '
    alljuqing = '发展.txt 结局.txt 剧情.txt 开头.txt 泪点.txt 笑点.txt '
    allshiting = '动作.txt 画面.txt 镜头.txt 视听.txt 试听效果中的其他.txt 音乐.txt '
    allzhizuo = '编剧.txt 出品公司.txt 导演.txt 选景.txt 制作.txt '
    allzhuti = '风格.txt 题材内容.txt 主题.txt '
    with open('/home/qin/zuoye/太空旅客.txt','r') as fff:
        contents = fff.read()
        zhengze = '(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s'
        n = 1
        while n<=5 :
            match = re.match(zhengze, allpath)
            result = match.group(n)
            if n==1:
                n1 = 1
                while n1<=6:
                    zhengze1 = '(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s'
                    match1 = re.match(zhengze1, alljuese)
                    result1 = match1.group(n1)
                    cunfang1 = open(argv,'a')
                    cunfang1.write('\n')
                    cunfang1.write(result1+ ':\n')
                    cunfang1.close()
                    with open(path+result+result1,'r') as f1:
                        f1s = f1.readlines()
                        for line in f1s :
                            line = line.strip('\n')
                            result1s = re.findall(line, contents)
                            num1 = len(result1s)
                            dictpipei[line] = num1
                            with open(argv,'a') as writefile1:
                                writefile1.write(line)
                                writefile1.write(' ')
                                writefile1.write(str(dictpipei[line]))
                                writefile1.write('\n')
                    n1+=1
                    dictpipei.clear()

            if n == 2:
                n2 = 1
                while n2 <= 6:
                    zhengze2 = '(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s'
                    match2 = re.match(zhengze2, alljuqing)
                    result2 = match2.group(n2)
                    cunfang2 = open(argv, 'a')
                    cunfang2.write('\n')
                    cunfang2.write(result2+ ':\n')
                    cunfang2.close()
                    with open(path+result+result2,'r') as f2:
                        f2s = f2.readlines()
                        for line in f2s :
                            line = line.strip('\n')
                            result2s = re.findall(line, contents)
                            num2 = len(result2s)
                            dictpipei[line] = num2
                            with open(argv,'a') as writefile2:
                                writefile2.write(line)
                                writefile2.write(' ')
                                writefile2.write(str(dictpipei[line]))
                                writefile2.write('\n')
                    n2+=1
                    dictpipei.clear()


            if n == 3:
                n3 = 1
                while n3 <= 6:
                    zhengze3 = '(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s'
                    match3 = re.match(zhengze3, allshiting)
                    result3 = match3.group(n3)
                    cunfang3 = open(argv, 'a')
                    cunfang3.write('\n')
                    cunfang3.write(result3+ ':\n')
                    cunfang3.close()
                    print path+result+result3
                    with open(path+result+result3,'r') as f3:
                        f3s = f3.readlines()
                        for line in f3s :
                            line = line.strip('\n')
                            result3s = re.findall(line, contents)
                            num3 = len(result3s)
                            dictpipei[line] = num3
                            with open(argv,'a') as writefile3:
                                writefile3.write(line)
                                writefile3.write(' ')
                                writefile3.write(str(dictpipei[line]))
                                writefile3.write('\n')
                    n3+=1
                    dictpipei.clear()

            if n == 4:
                n4 = 1
                while n4 <= 5:
                    zhengze4 = '(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s'
                    match4 = re.match(zhengze4, allzhizuo)
                    result4 = match4.group(n4)
                    cunfang4 = open(argv, 'a')
                    cunfang4.write('\n')
                    cunfang4.write(result4+ ':\n')
                    cunfang4.close()
                    with open(path+result+result4,'r') as f4:
                        f4s = f4.readlines()
                        for line in f4s :
                            line = line.strip('\n')
                            result4s = re.findall(line, contents)
                            num4 = len(result4s)
                            dictpipei[line] = num4
                            with open(argv,'a') as writefile4:
                                writefile4.write(line)
                                writefile4.write(' ')
                                writefile4.write(str(dictpipei[line]))
                                writefile4.write('\n')
                    n4+=1
                    dictpipei.clear()


            if n == 5:
                n5 = 1
                while n5 <= 3:
                    zhengze5 = '(.*?)\s(.*?)\s(.*?)\s'
                    match5 = re.match(zhengze5, allzhuti)
                    result5 = match5.group(n5)
                    cunfang5 = open(argv, 'a')
                    cunfang5.write('\n')
                    cunfang5.write(result5+ ':\n')
                    cunfang5.close()
                    with open(path+result+result5,'r') as f5:
                        f5s = f5.readlines()
                        for line in f5s :
                            line = line.strip('\n')
                            result5s = re.findall(line, contents)
                            num5 = len(result5s)
                            dictpipei[line] = num3
                            with open(argv,'a') as writefile5:
                                writefile5.write(line)
                                writefile5.write(' ')
                                writefile5.write(str(dictpipei[line]))
                                writefile5.write('\n')
                    n5+=1
                    dictpipei.clear()
            n+=1


# fenci()
# Tfidf('太空旅客分好词的版本.txt')
pipei()