from dataprocessing import dataprocess

class apriori:

    def __init__(self,transaction_list,support):
        self.trans = transaction_list
        self.sup =  support
        self.size = len(transaction_list)
        self.minsupc = int(support*len(transaction_list))
        self.frequents = []

    def frequent1items(self):
        oneitems = {}
        for n in self.trans:
            for i in n:
                if i in oneitems:
                    oneitems[i] = oneitems[i] + 1
                else:
                    oneitems[i] = 1
        frequentone = {}
        for p in oneitems:
            if oneitems[p] >= self.minsupc:
                frequentone[p] = oneitems[p]
                self.frequents.append(set([p]))
        #return frequentone

    def allbutonesame(self,list1,list2):
        c= 0
        for val in list1:
            if val in list2:
                c += 1
        return c
    def merge(self,level):
        klevels = []
        #print(self.frequents)
        for n in self.frequents:
            if len(n) == level:
                klevels.append(n)
        kplus1 = []
        for n in klevels:
            for o in klevels:
                t = set(n|o)
                if level -1 == self.allbutonesame(n,o) and kplus1.count(t) ==0:
                    #kplus1.append(set(n|o))
                    kplus1.append(t)
        #for n in kplus1:
            #if kplus1.count(n) > 1:
                #kplus1.remove(n)
        for n in kplus1:
            self.frequents.append(n)
        #print(len(kplus1))
        #for n in kplus1:

    def prune(self,level):

        def checksupp(valu):
            c=0
            for x in self.trans:
                if (set(x) >= valu) == True:
                    c += 1
            return c

        klevel = []
        #print(self.frequents)
        for n in self.frequents:
            if len(n) == level:
                klevel.append(n)
        for n in klevel:
            #print(checksupp(n))
            if checksupp(n) <= self.minsupc:
                self.frequents.remove(n)
        #print(self.frequents)
    def frequentreturn(self):
        print(self.frequents)

'''
            kpruned = []
            for i in n:
                kpruned.append(n-set([i]))

            for k in kpruned:
                if checksupp(k) == False:
                    print(n)
                    #self.frequents.remove([n])
                    qwer =0
        #print(self.frequents)
        '''



x =dataprocess('adult.data.train.csv', ',').tuplemaker()

y = apriori(x, 0.6)
y.frequent1items()
y.merge(1)
y.prune(2)
