import pandas as pd
import numpy as np

class dataprocess:

    def __init__(self,file,delim):
        missingvals = [' ?']
        self.df = pd.read_csv(file , delimiter = delim, na_values = missingvals)


    def clean(self):
        del self.df['fnlwgt']
        #self.df = self.df[self.df.workclass != '?']
        #self.df = self.df.replace('?', np.nan)
        #self.df = self.df.dropna()
        #self.df = self.df.where(self.df == '?').drop()
        self.df = self.df.dropna()
        #print(self.df)

    def bin(self):
        self.clean()
        age_labels = ['0-18','19-30','31-40','41-50','51-60','70+']
        age_bins = [0,19,31,41,51,70,self.df.age.max()]
        self.df['age'] = pd.cut(self.df.age,bins=age_bins,labels =age_labels)
        defaultlabel =['no-gains','gains']
        capitalgainbins=[self.df.capitalgain.min()-1,1,self.df.capitalgain.max()]
        self.df['capitalgain'] = pd.cut(self.df.capitalgain, bins = capitalgainbins ,labels = defaultlabel)
        defaultlabel2 =['k','l','m','n','o','p','q','r','s','t']
        self.df['capitalloss'] = pd.cut(self.df.capitalloss, bins=10,labels = defaultlabel2)
        defaultlabel3= ['no-work','part-time','full-time']
        workhoursbins = [0,1,20,self.df.hoursperweek.max()]
        self.df['hoursperweek'] = pd.cut(self.df.hoursperweek,bins=workhoursbins, labels = defaultlabel3)

    def tuplemaker(self):
        self.bin()
        rows = self.df.iterrows()
        transactions= list(self.df.itertuples(index=False, name=None))
        #for n in rows:
            #tup = [n['age'],n['workclass'],n['education'],n['educationnum'],n['maritalstatus'],n['occupation'],n['serv'],n['relationship'],n['race'],n['sex'],n['capitalgain'],n['capitalloss'],n['hoursperweek'],n['nativecountry']]
            #tup =
            #tup = tuple(tup)
            #transactions.append(tup)
        return transactions




x = dataprocess('adult.data.train.csv', ',')
x.tuplemaker()
