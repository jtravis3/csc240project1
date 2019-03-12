from apriori import *
def runapriori(file,delim,support):
    x =dataprocess(file, delim).tuplemaker()

    y = apriori(x, support)
    y.frequent1items()
    for n in range(1,len(x[0])-1):
        y.merge(n)
        y.prune(n+1)
    print(y.frequents)

runapriori('adult.data.train.csv',',',0.6)
