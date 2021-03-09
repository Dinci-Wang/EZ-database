#這邊的輸入ppeak是平均 如果輸入是最高的話要把144行改成for (2 5)
import math
import numpy as np
import copy
from itertools import zip_longest
from sklearn.metrics import precision_recall_fscore_support
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics
from imblearn.under_sampling import ClusterCentroids,CondensedNearestNeighbour,InstanceHardnessThreshold,NearMiss,NeighbourhoodCleaningRule,TomekLinks,RandomUnderSampler
from imblearn.over_sampling import SMOTE,ADASYN,BorderlineSMOTE,KMeansSMOTE,SVMSMOTE,RandomOverSampler
# =============================================================================除以P波個數
#     for i in range(1485):
#         for stage in range(0,14):
#             if ii_1485[i,stage,0]>=1:
#                 
#         
#                 ii_1485[i,stage,2]=ii_1485[i,stage,2]/ii_1485[i,stage,0]
#                 ii_1485[i,stage,3]=ii_1485[i,stage,3]/ii_1485[i,stage,0]
#                 ii_1485[i,stage,4]=ii_1485[i,stage,4]/ii_1485[i,stage,0]
#                 v1_1485[i,stage,2]=v1_1485[i,stage,2]/v1_1485[i,stage,0]
#                 v1_1485[i,stage,3]=v1_1485[i,stage,3]/v1_1485[i,stage,0]
#                 v1_1485[i,stage,4]=v1_1485[i,stage,4]/v1_1485[i,stage,0]
#     np.save(r'hospital\mean_1485_II',ii_1485)
#     np.save(r'hospital\mean_1485_V1',v1_1485)
# =============================================================================
#%% P_STANDING E_ALL R_ALL E_STAGE 1 E_STAGE 2 E_STAGE 3 E_STAGE 4 E_STAGE 5 E_STAGE 6 E_STAGE 7 R_1 MIN R_3 MIN R_5 MIN R_LAST
def make_knn_database(hospital_ii,hospital_v1,level,search_lead):
    #把資料轉換成適當格式
    mean_matrix=search_mean(hospital_ii,hospital_v1,level,search_lead)
    ass=hospital_ii[:,[0,1,2],1:]
    for i in range(ass.shape[0]):#病人
        for ii in range(ass.shape[1]):#P E R
            for iii in range(0,ass.shape[2]):#peak duraton pfront prear
                if ass[i,ii,iii]==-9999:
                    
                    this_level=int(level[i])
                    ass[i,ii,iii]=mean_matrix[iii,this_level,ii]
    
    
    ass=ass.reshape(ass.shape[0],ass.shape[1]*ass.shape[2])
    #ass = ass / ass.max(axis=0)  #normalize

    return ass
def search_mean(hospital_ii,hospital_v1,level_1485,search_lead):
    #抓各組參數平均值
    if search_lead==1:
        hospital_ii=hospital_v1
    mean_matrix=np.zeros((4,3,14))
    list=['P_STANDING','E_ALL','R_ALL','E_STAGE 1','E_STAGE 2','E_STAGE 3','E_STAGE 4',
          'E_STAGE 5','E_STAGE 6','E_STAGE 7','R_1 MIN','R_3 MIN','R_5 MIN','R_LAST']
    for stage in range(0,14):#0 14
        for level in range(0,3):#0 3
            ass=hospital_ii[np.where(level_1485==level),stage,0:]
            ass=np.reshape(ass,(ass.shape[1],ass.shape[2]))
            ass=np.delete(ass,np.where(ass[:,0]==-9999),axis=0)
            ass=np.delete(ass,np.where(ass[:,0]==0),axis=0)
            for parameter in range(1,5):
                temp_ass=ass[:,parameter]
                mean_matrix[parameter-1,level,stage]=round(np.mean(temp_ass),2)
    return mean_matrix
def search_median(hospital_ii,hospital_v1,level_1485,search_lead):
    #抓各組參數中位數
    if search_lead==1:
        hospital_ii=hospital_v1
    median_matrix=np.zeros((4,3,14))
    list=['P_STANDING','E_ALL','R_ALL','E_STAGE 1','E_STAGE 2','E_STAGE 3','E_STAGE 4',
          'E_STAGE 5','E_STAGE 6','E_STAGE 7','R_1 MIN','R_3 MIN','R_5 MIN','R_LAST']
    for stage in range(0,14):#0 14
        for level in range(0,3):#0 3
            ass=hospital_ii[np.where(level_1485==level),stage,0:]
            ass=np.squeeze(ass)
            ass=np.delete(ass,np.where(ass[:,0]==-9999),axis=0)
            ass=np.delete(ass,np.where(ass[:,0]==0),axis=0)
            for parameter in range(1,5):
                temp_ass=ass[:,parameter]
                median_matrix[parameter-1,level,stage]=round(np.median(temp_ass),2)

    return median_matrix

def search_std(hospital_ii,hospital_v1,level_1485,search_lead):
    #抓各組參數標準差
    if search_lead==1:
        hospital_ii=hospital_v1
    std_matrix=np.zeros((4,3,14))
    list=['P_STANDING','E_ALL','R_ALL','E_STAGE 1','E_STAGE 2','E_STAGE 3','E_STAGE 4',
          'E_STAGE 5','E_STAGE 6','E_STAGE 7','R_1 MIN','R_3 MIN','R_5 MIN','R_LAST']
    for stage in range(0,14):#0 14
        for level in range(0,3):#0 3
            ass=hospital_ii[np.where(level_1485==level),stage,0:]
            ass=np.squeeze(ass)
            ass=np.delete(ass,np.where(ass[:,0]==-9999),axis=0)
            ass=np.delete(ass,np.where(ass[:,0]==0),axis=0)
            for parameter in range(1,5):
                temp_ass=ass[:,parameter]
                std_matrix[parameter-1,level,stage]=round(np.std(temp_ass),2)

    return std_matrix

def search_stage_sample(hospital_ii,hospital_v1,level_1485,search_lead):
    if search_lead==1:
        hospital_ii=hospital_v1
    #抓取各個level在每個stage有多少筆
    list=['P_STANDING','E_ALL','R_ALL','E_STAGE 1','E_STAGE 2','E_STAGE 3','E_STAGE 4',
      'E_STAGE 5','E_STAGE 6','E_STAGE 7','R_1 MIN','R_3 MIN','R_5 MIN','R_LAST']
    number_matrix=np.zeros((3,14))
    for level in range(0,3):
        level_data=hospital_ii[np.where(level_1485==level),:,:] #level=i的那些病人組成的一疊病歷表
        level_data=np.squeeze(level_data)
        for stage in range(0,14):
            counter=0
            for people in range(level_data.shape[0]):
                if level_data[people,stage,0]!=-9999:
                    counter=counter+1
            number_matrix[level,stage]=counter
    return number_matrix
if __name__ == "__main__":    
    #%%數據清洗 pnumber peak pduration pfront frear
    print("load data")
    
    nii_1485 = np.load(r'hospital\1485_II.npy')
    nv1_1485 = np.load(r'hospital\1485_V1.npy')
    for i in range(1485):
        for stage in range(0,14):
                for parameter in  range(0,5):
                    if nii_1485[i,stage,parameter]<=0:
                        nii_1485[i,stage,:]=-9999
                    
                        
                    
    for i in range(1485):
        for stage in range(0,14):
            if nv1_1485[i,stage,0]!=-9999:
                for parameter in  range(0,5):
                    if nv1_1485[i,stage,parameter]<=0:
                        nv1_1485[i,stage,:]=-9999
                        
    nii_1485[np.isnan(nii_1485)] = -9999
    nv1_1485[np.isnan(nv1_1485)] = -9999
    for i in range(1485):
        for stage in range(0,14):
            for parameter in range(1,5):
                if nii_1485[i,stage,parameter]==-9999:
                    break
                nii_1485[i,stage,parameter]=nii_1485[i,stage,parameter]/nii_1485[i,stage,0]
                nv1_1485[i,stage,parameter]=nv1_1485[i,stage,parameter]/nv1_1485[i,stage,0]
    
    
    
    np.save(r'hospital\mean_1485_II',nii_1485)
    np.save(r'hospital\mean_1485_V1',nv1_1485)
    #清洗結束
    #%%

    ii_1485 = np.load(r'hospital\mean_1485_II.npy')
    v1_1485 = np.load(r'hospital\mean_1485_V1.npy')
    id_1485=np.load(r'hospital\1485_id.npy')
    level_1485=np.load(r'hospital\1485_level.npy')

    

    std_matrix=search_std(ii_1485,v1_1485,level_1485,0)#最後面的1-> lead v1 0->lead II
    median_matrix=search_median(ii_1485,v1_1485,level_1485,0)
    number_matrix=search_stage_sample(ii_1485,v1_1485,level_1485,0)
    mean_matrix=search_mean(ii_1485,v1_1485,level_1485,0)
    
    
    
    dataformat=make_knn_database(ii_1485,v1_1485,level_1485,0) #knn
    np.save(r'hospital\dataformat',dataformat)
   
    dataformat=shuffle(dataformat)
    #%%
    X_train, X_test, y_train, y_test = train_test_split(dataformat, level_1485, test_size=0.20) #contrl label cat

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train,y_train)
    knn_result=knn.predict(X_test)
    print(confusion_matrix(y_test, knn_result))
    accuracy = metrics.accuracy_score(y_test, knn_result)
    f1 = metrics.f1_score(y_test, knn_result, average='macro')
    print("#f1:",f1,"  #accuracy:",accuracy)
# =============================================================================
#              P_number    P_peak    p_duration    P_front    P_rear
# P_STANDING 
# E_ALL 
# R_ALL 
# E_STAGE 1 
# E_STAGE 2 
# E_STAGE 3 
# E_STAGE 4 
# E_STAGE 5 
# E_STAGE 6 
# E_STAGE 7 
# R_1 MIN 
# R_3 MIN 
# R_5 MIN 
# R_LAST
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    