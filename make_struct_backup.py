# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:42:36 2021

@author: dinci
"""

"""
Created on Wed Dec  9 16:57:33 2020

@author: User
"""
import math
import numpy as np
import copy
from itertools import zip_longest

class data_struct:
    def __init__(self,people_number=1485,stage_number=14,parameter_number=5):
        self.people_number=people_number        
        self.stage_number=stage_number
        self.parameter_number=parameter_number
        self.hospitial_II=np.full((people_number,stage_number,parameter_number),-9999.0)
        self.hospitial_V1=np.full((people_number,stage_number,parameter_number),-9999.0)
        
        
    def return_hospital(self,lead=0):
        if lead==0:
            return self.hospitial_II
        else: 
            return self.hospitial_V1
    def putin_II(self,people_key,stage_key,stage_key2,P_number,P_peak,P_duration,P_rear,P_front):
        if stage_key!=0:
            
            if self.hospitial_II[people_key,stage_key2,0]==-9999.0:
                self.hospitial_II[people_key,stage_key2,0]=P_number
                self.hospitial_II[people_key,stage_key2,1]=P_peak
                self.hospitial_II[people_key,stage_key2,2]=P_duration
                self.hospitial_II[people_key,stage_key2,3]=P_front
                self.hospitial_II[people_key,stage_key2,4]=P_rear
            else :
                self.hospitial_II[people_key,stage_key2,0]=self.hospitial_II[people_key,stage_key2,0]+P_number
                self.hospitial_II[people_key,stage_key2,1]=self.hospitial_II[people_key,stage_key2,1]+P_peak
                self.hospitial_II[people_key,stage_key2,2]=self.hospitial_II[people_key,stage_key2,2]+P_duration
                self.hospitial_II[people_key,stage_key2,3]=self.hospitial_II[people_key,stage_key2,3]+P_front
                self.hospitial_II[people_key,stage_key2,4]=self.hospitial_II[people_key,stage_key2,4]+P_rear
            
            if self.hospitial_II[people_key,stage_key,0]==-9999.0:
                self.hospitial_II[people_key,stage_key,0]=P_number
                self.hospitial_II[people_key,stage_key,1]=P_peak
                self.hospitial_II[people_key,stage_key,2]=P_duration
                self.hospitial_II[people_key,stage_key,3]=P_front
                self.hospitial_II[people_key,stage_key,4]=P_rear
    
            else :
                self.hospitial_II[people_key,stage_key,0]=self.hospitial_II[people_key,stage_key,0]+P_number
                self.hospitial_II[people_key,stage_key,1]=self.hospitial_II[people_key,stage_key,1]+P_peak
                self.hospitial_II[people_key,stage_key,2]=self.hospitial_II[people_key,stage_key,2]+P_duration
                self.hospitial_II[people_key,stage_key,3]=self.hospitial_II[people_key,stage_key,3]+P_front
                self.hospitial_II[people_key,stage_key,4]=self.hospitial_II[people_key,stage_key,4]+P_rear
        if stage_key==0:
            if self.hospitial_II[people_key,stage_key2,0]==-9999.0:
                self.hospitial_II[people_key,stage_key2,0]=P_number
                self.hospitial_II[people_key,stage_key2,1]=P_peak
                self.hospitial_II[people_key,stage_key2,2]=P_duration
                self.hospitial_II[people_key,stage_key2,3]=P_front
                self.hospitial_II[people_key,stage_key2,4]=P_rear
            else :
                self.hospitial_II[people_key,stage_key2,0]=self.hospitial_II[people_key,stage_key2,0]+P_number
                self.hospitial_II[people_key,stage_key2,1]=self.hospitial_II[people_key,stage_key2,1]+P_peak
                self.hospitial_II[people_key,stage_key2,2]=self.hospitial_II[people_key,stage_key2,2]+P_duration
                self.hospitial_II[people_key,stage_key2,3]=self.hospitial_II[people_key,stage_key2,3]+P_front
                self.hospitial_II[people_key,stage_key2,4]=self.hospitial_II[people_key,stage_key2,4]+P_rear
    
    def putin_V1(self,people_key,stage_key,stage_key2,P_number,P_peak,P_duration,P_rear,P_front):
        if stage_key!=0:
            if self.hospitial_V1[people_key,stage_key2,0]==-9999.0:
                self.hospitial_V1[people_key,stage_key2,0]=P_number
                self.hospitial_V1[people_key,stage_key2,1]=P_peak
                self.hospitial_V1[people_key,stage_key2,2]=P_duration
                self.hospitial_V1[people_key,stage_key2,3]=P_front
                self.hospitial_V1[people_key,stage_key2,4]=P_rear
            else :
                self.hospitial_V1[people_key,stage_key2,0]=self.hospitial_V1[people_key,stage_key2,0]+P_number
                self.hospitial_V1[people_key,stage_key2,1]=self.hospitial_V1[people_key,stage_key2,1]+P_peak
                self.hospitial_V1[people_key,stage_key2,2]=self.hospitial_V1[people_key,stage_key2,2]+P_duration
                self.hospitial_V1[people_key,stage_key2,3]=self.hospitial_V1[people_key,stage_key2,3]+P_front
                self.hospitial_V1[people_key,stage_key2,4]=self.hospitial_V1[people_key,stage_key2,4]+P_rear
            
            if self.hospitial_V1[people_key,stage_key,0]==-9999.0:
                self.hospitial_V1[people_key,stage_key,0]=P_number
                self.hospitial_V1[people_key,stage_key,1]=P_peak
                self.hospitial_V1[people_key,stage_key,2]=P_duration
                self.hospitial_V1[people_key,stage_key,3]=P_front
                self.hospitial_V1[people_key,stage_key,4]=P_rear
    
            else :
                self.hospitial_V1[people_key,stage_key,0]=self.hospitial_V1[people_key,stage_key,0]+P_number
                self.hospitial_V1[people_key,stage_key,1]=self.hospitial_V1[people_key,stage_key,1]+P_peak
                self.hospitial_V1[people_key,stage_key,2]=self.hospitial_V1[people_key,stage_key,2]+P_duration
                self.hospitial_V1[people_key,stage_key,3]=self.hospitial_V1[people_key,stage_key,3]+P_front
                self.hospitial_V1[people_key,stage_key,4]=self.hospitial_V1[people_key,stage_key,4]+P_rear
        if stage_key==0:
            if self.hospitial_V1[people_key,stage_key2,0]==-9999.0:
                self.hospitial_V1[people_key,stage_key2,0]=P_number
                self.hospitial_V1[people_key,stage_key2,1]=P_peak
                self.hospitial_V1[people_key,stage_key2,2]=P_duration
                self.hospitial_V1[people_key,stage_key2,3]=P_front
                self.hospitial_V1[people_key,stage_key2,4]=P_rear
            else :
                self.hospitial_V1[people_key,stage_key2,0]=self.hospitial_V1[people_key,stage_key2,0]+P_number
                self.hospitial_V1[people_key,stage_key2,1]=self.hospitial_V1[people_key,stage_key2,1]+P_peak
                self.hospitial_V1[people_key,stage_key2,2]=self.hospitial_V1[people_key,stage_key2,2]+P_duration
                self.hospitial_V1[people_key,stage_key2,3]=self.hospitial_V1[people_key,stage_key2,3]+P_front
                self.hospitial_V1[people_key,stage_key2,4]=self.hospitial_V1[people_key,stage_key2,4]+P_rear
            
            
            
def find_parameter(wave,wave_P,wave_baseline,lead):
    p_wave_start_from=-1
    p_wave_end_at=-1
    cut_point=-1
    in_p_wave=0
    p_front=0
    p_rear=0
    p_peak_sum=0
    
    p_dur=0
    p_number=0
    for ii in range(1300):#在每個1300
        if ii==1299:
            wave_P[ii,0]=0
        if wave_P[ii,0]!=0 and in_p_wave==0:#不在P波中並且遇到P波了
            p_wave_start_from=ii#p波從這邊開始
            in_p_wave=1
            p_number=p_number+1
        if wave_P[ii,0]==0 and in_p_wave==1:#從P波中出來了
            p_dur=ii-1-p_wave_start_from
            in_p_wave=0
            cut_point=math.ceil(p_wave_start_from+3*p_dur/8)
            if p_dur>=20 and p_dur<=120:
                p_peak=-9999
                for iii in range(p_wave_start_from,ii):
                    if p_peak<=wave[iii,lead]:
                        p_peak=wave[iii,lead]
                    if iii>cut_point:#後5/8
                        
                        p_rear=p_rear+abs(wave[iii,lead]-wave_baseline[iii,lead])
                    if iii<=cut_point:#前3/8
                        p_front=p_front+abs(wave[iii,lead]-wave_baseline[iii,lead])
                if p_peak !=-9999:
                    p_peak_sum=p_peak_sum+p_peak
            else : 
                p_number=p_number-1

        
    p_peak_sum=p_peak_sum*0.005
    p_dur=p_dur*2
    p_front=p_front*0.01
    p_rear=p_rear*0.01
    return p_number,p_peak_sum,p_dur,p_front,p_rear


def remove_level3(target,level):
    pivot=np.where(level==3)
    target=np.delete(target,pivot,axis=0)
    return target
    
def make_level_181800(ID,level):
    new_level=np.full(ID.shape,3)
    for i in range(ID.shape[0]):
        pos=np.where(level[:,0]==ID[i])
        try:    
            s=int(level[pos,1])
        except: s=3
        if s==0: 
            new_level[i]=0
        if s==1:
            new_level[i]=1
        if s==2:
            new_level[i]=2
    return new_level
    

if __name__ == "__main__":    
    print("load data")
    stage = np.load(r'after_remove_level3\126605_stage.npy')
    id = np.load(r'after_remove_level3\126605_ID.npy')
    id=id.astype(int)
    time = np.load(r'after_remove_level3\126605_time.npy')
    labelP = np.load(r'after_remove_level3\126605_labelP.npy')
    wave = np.load(r'after_remove_level3\126605_wave.npy')
    level=np.load(r'after_remove_level3\126605_level.npy')
    baseline=np.load(r'after_remove_level3\126605_baseline.npy')
    id_1485=np.load(r'after_remove_level3\1485_ID.npy')
    level_1485=np.load(r'after_remove_level3\1485_level.npy')

    
    ass_hospital=data_struct(people_number=1485,stage_number=14,parameter_number=5)
    
    #%% P_STANDING  E_STAGE 1 E_STAGE 2 E_STAGE 3 E_STAGE 4 E_STAGE 5 E_STAGE 6 E_STAGE 7 R_1 MIN R_3 MIN R_5 MIN    

    
    temp_wave=wave[0,:,:]
    temp_baseline=baseline[0,:,:]
    temp_P=labelP[0,:,:]
    
    #%%
    ccc=0
    for i in range(id.shape[0]):
        print(i)
        person_ID=id[i]
        person_level=level[i]
        key_ID=np.where(id_1485==person_ID)
        key_ID=int(key_ID[0])
        stage_key=-1
        if stage[i]=='P_STANDIN':
            stage_key=0
        if stage[i]=='PRETEST_S':
            stage_key=0
        if stage[i]=='P_HYPERV.':
            stage_key=0
        if stage[i]=='E_STAGE 1':
            stage_key=3
        if stage[i]=='E_STAGE 2':
            stage_key=4
        if stage[i]=='E_STAGE 3':
            stage_key=5
        if stage[i]=='E_STAGE 4':
            stage_key=6
        if stage[i]=='E_STAGE 5':
            stage_key=7
        if stage[i]=='E_STAGE 6':
            stage_key=8
        if stage[i]=='E_STAGE 7':
            stage_key=9
        if stage[i]=='R_1 MIN':
            stage_key=10
        if stage[i]=='R_3 MIN':
            stage_key=11
        if stage[i]=='R_5 MIN':
            stage_key=12
        if stage[i]=='R_LAST':
            stage_key=13
        key2=0
        if stage_key>9:
            key2=2
        if stage_key>0 and stage_key<=9:
            key2=1
        #P波持續超過20個時間點才會抓 並且小於120
        P_number,P_peak,P_duration,P_front,P_rear=find_parameter(wave[i,:,:],labelP[i,:,:],baseline[i,:,:],0)
        ass_hospital.putin_II(key_ID,stage_key,key2,P_number,P_peak,P_duration,P_front,P_rear)
        P_number,P_peak,P_duration,P_front,P_rear=find_parameter(wave[i,:,:],labelP[i,:,:],baseline[i,:,:],1)
        ass_hospital.putin_V1(key_ID,stage_key,key2,P_number,P_peak,P_duration,P_front,P_rear)
        
    all_II=ass_hospital.return_hospital(lead=0)
    all_V1=ass_hospital.return_hospital(lead=1)
    np.save(r'hospital\1485_II',all_II)
    np.save(r'hospital\1485_V1',all_V1)
    np.save(r'hospital\1485_level',level_1485)
    np.save(r'hospital\1485_id',id_1485)
# =============================================================================
#         if all_people_II[key_ID,key2,0]==-9999:
#             all_people_II[key_ID,key2,0]=P_number
#             all_people_II[key_ID,key2,1]=P_peak
#             all_people_II[key_ID,key2,2]=P_duration
#             all_people_II[key_ID,key2,3]=P_front
#             all_people_II[key_ID,key2,4]=P_rear
#         else :
#             all_people_II[key_ID,key2,0]=all_people_II[key_ID,key2,0]+P_number
#             if all_people_II[key_ID,key2,1]<P_peak:
#                 all_people_II[key_ID,key2,1]=P_peak
#             all_people_II[key_ID,key2,2]=all_people_II[key_ID,key2,2]+P_duration
#             all_people_II[key_ID,key2,3]=all_people_II[key_ID,key2,3]+P_front
#             all_people_II[key_ID,key2,4]=all_people_II[key_ID,key2,4]+P_rear
#         
#         if all_people_II[key_ID,stage_key,0]==-9999:
#             all_people_II[key_ID,stage_key,0]=P_number
#             all_people_II[key_ID,stage_key,1]=P_peak
#             all_people_II[key_ID,stage_key,2]=P_duration
#             all_people_II[key_ID,stage_key,3]=P_front
#             all_people_II[key_ID,stage_key,4]=P_rear
# 
#         else :
#             all_people_II[key_ID,stage_key,0]=all_people_II[key_ID,stage_key,0]+P_number
#             if all_people_II[key_ID,stage_key,1]<P_peak:
#                 all_people_II[key_ID,stage_key,1]=P_peak
#             all_people_II[key_ID,stage_key,2]=all_people_II[key_ID,stage_key,2]+P_duration
#             all_people_II[key_ID,stage_key,3]=all_people_II[key_ID,stage_key,3]+P_front
#             all_people_II[key_ID,stage_key,4]=all_people_II[key_ID,stage_key,4]+P_rear
# =============================================================================


    
    
    
    
    
    
    
    
    
    
    
    