                                    #Import libraries
from pylab import *
import subprocess                   #Used to run terminal commands
import os
                                    #Array of file no.s
modelfiles = array(['11', '12', '13', '16', '17', '21', '22', '23', '26', '27', '31', '32', '33', '36', '37', '61', '62', '63', '66', '67', '71', '72', '73', '76', '77', '111', '112', '113', '116', '117', '121', '122', '123', '126', '127', '131', '132', '133', '136', '137', '161', '162', '163', '166', '167', '171', '172', '173', '176', '177', '211', '212', '213', '216', '217', '221', '222', '223', '226', '227', '231', '232', '233', '236', '237', '261', '262', '263', '266', '267', '271', '272', '273', '276', '277', '311', '312', '313', '316', '317', '321', '322', '323', '326', '327', '331', '332', '333', '336', '337', '361', '362', '363', '366', '367', '371', '372', '373', '376', '377', '611', '612', '613', '616', '617', '621', '622', '623', '626', '627', '631', '632', '633', '636', '637', '661', '662', '663', '666', '667', '671', '672', '673', '676', '677', '711', '712', '713', '716', '717', '721', '722', '723', '726', '727', '731', '732', '733', '736', '737', '761', '762', '763', '766', '767', '771', '772', '773', '776', '777'])
                                    #Test sequence
#devdata = array(['121', '111', '622', '71', '662', '122', '262', '31', '311', '172', '21', '331', '277', '11', '77', '66', '12', '16', '22', '61', '116', '233', '711', '132', '13', '23', '212', '322', '217'])
devdata = array(['262', '662', '66', '711', '12', '233', '217', '121', '622', '61', '11', '13', '122', '22', '111', '77', '277', '212', '16', '331', '311', '116', '31', '21', '23', '172', '322', '132', '71'])
#testdata = array(['3','1','4','2','5'])
testdata = array(['33','12','21','233','72'])

                                    #To predict the utterances
def seqpredict(files,test,Nmax=2,beg=9,nd=38) :    
                                        #Initialize
    allprob = np.zeros((len(files),len(test)))
    trueval = np.zeros(len(test))                                    
                                        #Get probabilities for all models
    for i in range(0,len(files)) :
        
        fileno = files[i]
        args = ["./test_hmm ctsHMM.dev ctsModels_p0.85_cl48/"+fileno+".hmm"]
        popen = subprocess.Popen(args, stdout=subprocess.PIPE,shell=True)
        popen.wait()
        output = popen.stdout.read()
        output = output.decode("utf-8")
        output = output.split("\n")
        output = array(output)
        output = np.genfromtxt(output[beg:nd],delimiter=' ',dtype=str)
        #print(output)
        output = output[:,4]
        output = output.astype("float")
        #print(output)
        allprob[i] = output
    
    predict = np.argpartition(allprob,-Nmax,axis=0)[-Nmax:]
    for i in range(0,len(test)) :
        trueval[i] = np.where(int(test[i]) == files.astype("int"))[0]
    trueval = trueval.astype("int")
    
    return predict,trueval
#'''    
predict,trueval = seqpredict(modelfiles,devdata)    
print(modelfiles[predict])
print(modelfiles[trueval])
print(predict-trueval)
acc = len(np.where(predict-trueval==0)[0])/len(trueval)
print(acc)
print(np.where(predict-trueval==0)[1])
#'''
'''
predict,trueval = seqpredict(modelfiles,testdata,nd=14)    
print(modelfiles[predict])
'''
#print(max(output))
#print(len(output))
#print(output[0][4],output[1][4],output[2][4])

