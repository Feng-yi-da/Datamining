# coding=utf-8
# coding=gbk

import math
import random


def K_Mean(Node, K, Number):
    # 节点数
    Nodenum = len(Node)

    # 维度
    N = len(Node[0])

    # 节点所属中心
    # [-1,-1,-1,...,-1]
    NodeBelong = [int for i in range(Nodenum)]
    for i in range(Nodenum):
        NodeBelong[i] = -1

    # K 个中心
    Knode = [[int for j in range(N)] for i in range(K)]
    for i in range(K):
        for j in range(N):
            Knode[i][j] = -1

    # 生成初步k个中心
    # 不生成相同的中心
    inum = 0
    while inum < K:
        # print
        # print "inumi "+str(inum)
        tempk = random.randint(0, Nodenum - 1)
        # print "tempk "+str(tempk) +" "+str(Node[tempk][0])
        # print
        isame = False
        for j in range(inum):
            same = 0
            for k in range(N):
                # print  tempk
                # print len(Node[tempk])
                # print k
                # print Node[tempk][k]

                if Knode[j][k] == Node[tempk][k]:
                    same = same + 1
                    # print "same" + str(same)
            # print "Knode[" + str(j) + "][" + str(K) + "] " + str(Knode[j][k]) + " Node[tempk][k]" + str(Node[tempk][k])
            if same == N:
                inum = inum - 1
                isame = True
                # print "inumd " + str(inum)
                # print "33"
        if isame == False:
            for j in range(N):
                Knode[inum][j] = Node[tempk][j]
            inum = inum + 1

            # for i in range(K):
            #     out = ""
            #     for j in range(N):
            #         out = out + str(Knode[i][j]) + " "
            #     print out

    # 冒泡排序
    for i in range(N):
        listLength = K
        while listLength > 0:
            for j in range(listLength - 1):
                if i !=0:
                    beforsame = 0
                    for k in range(i):
                        if Knode[j][k] == Knode[j+1][k]:
                            beforsame = beforsame + 1
                    # print beforsame
                    if beforsame == i:
                        # print "******"+str(i)
                        if Knode[j][i] > Knode[j + 1][i]:
                            tempKnode = Knode[j]
                            Knode[j] =  Knode[j + 1]
                            Knode[j + 1] = tempKnode
                else:
                    if Knode[j][i] > Knode[j + 1][i]:
                        tempKnode = Knode[j]
                        Knode[j] = Knode[j + 1]
                        Knode[j + 1] = tempKnode
            listLength -= 1


    print "初步中心"
    for i in range(K):
        out = "（"
        for j in range(N):
            out = out + str(Knode[i][j]) + " "
        print out + ")"

    # Number 最大迭代次数
    for i in range(Number):

        # 每个点所属的中心
        for j in range(Nodenum):
            minDistance = 1000000
            for k in range(K):
                distance = 0.0
                for l in range(N):
                    distance = distance + math.pow(Knode[k][l] - Node[j][l], 2)
                if minDistance > distance:
                    minDistance = distance
                    NodeBelong[j] = k

        # out = ""
        # for j in range(N):
        #     out = out + str(NodeBelong[j]) + " "
        # print out
        # print "***************"
        # print i
        # print "***************"
        stopNum = 0
        # 计算新的中心
        for j in range(K):
            for k in range(N):
                tatoll = 0.0
                num = 0.0
                for l in range(Nodenum):
                    if NodeBelong[l] == j:
                        tatoll = tatoll + Node[l][k]
                        num = num + 1
                # print "K " + str(j) + " N" + str(k) + " Nodenum " + str(l)
                avg = tatoll / num
                if avg == Knode[j][k]:
                    stopNum = stopNum + 1
                Knode[j][k] = avg

        # 迭代结果一致，停止迭代
        if stopNum == N * K:
            print "Stop"
            break

    print "点集是 ："

    for i in range(Nodenum):
        outNode = "( "
        for j in range(N):
            outNode = outNode + str(Node[i][j]) + " "
        outNode = outNode + " )"
        print outNode

    # 输出结果
    print
    for i in range(K):
        outK = "簇中心是 ("
        for j in range(N):
            outK = outK + str(Knode[i][j]) + " "
        outK = outK + ")"
        print outK
        print "簇成员："
        for j in range(Nodenum):
            if NodeBelong[j] == i:
                # for k in range(N):
                outNode = "("
                for l in range(N):
                    outNode = outNode + str(Node[j][l]) + " "
                outNode = outNode + ")"
                print outNode
        print


Node1 = [[1], [2], [3], [4], [5], [6], [7], [8], [10], [11], [12], [13]]

Node2 = [[1, 1], [1, 2], [1, 5], [1, 6], [2, 1], [2, 3], [2, 4], [2, 5], [3, 2], [4, 1], [5, 3], [6, 6], [7, 1], [8, 2],
         [10, 4], [11, 1], [12, 1], [13, 2]]

Node3 = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [2, 1, 1], [2, 2, 1], [2, 4, 1], [2, 8, 1], [4, 3, 1], [5, 3, 1], [6, 3, 1],
         [8, 3, 1]]
K = 5
Number = 2
print "一维"
K_Mean(Node1, K, Number)
print "###################################################"
print
print "二维"
K_Mean(Node2, K, Number)
print
print "##################################################"
print
print "三维"
K_Mean(Node3, K, Number)
