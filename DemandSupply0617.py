#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:31:07 2021

@author: zhanghaonan
"""


import pickle


### calculating the distance 
def calculate_distance_haversine(lat1, lon1, lat2, lon2):
    # radius of earth
    from math import radians, cos, sin, asin, sqrt
    r = 3962.173405788

    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = [radians(x) for x in [lat1, lon1, lat2, lon2]]
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return r * c


with open('IntermediateData/IntermediateCreatorLocation/creatorLocationMap.pickle', 'rb') as handle:
    creatorLocationMap = pickle.load(handle)

with open('IntermediateData/IntermediateReceiverLocation/receiverLocationMap.pickle', 'rb') as handle:
    receiverLocationMap = pickle.load(handle)



#
#
#
#creator_neigh500 = {}
#creator_neigh2000 = {}
#creator_neigh5000 = {}
#
#for key in creatorLocationMap.keys():
#    neighbor_list_500m = []
#    neighbor_list_2000m = []
#    neighbor_list_5000m = []
#    for elem in creatorLocationMap.keys():
#        if key[0] == elem[0]:
#            continue
#        else:
#            dist = calculate_distance_haversine(creatorLocationMap[(key)][0],creatorLocationMap[(key)][1],
#                                               creatorLocationMap[(elem)][0],creatorLocationMap[(elem)][1])
#            print(key,elem,dist)
#            if dist <= 0.31:
#                neighbor_list_500m.append(elem)
#                neighbor_list_2000m.append(elem)
#                neighbor_list_5000m.append(elem)
#            elif dist <= 1.24:
#                neighbor_list_2000m.append(elem)
#                neighbor_list_5000m.append(elem)
#            elif dist <= 3.1:
#                neighbor_list_5000m.append(elem)
#            else:
#                continue
#            
#    if key[1] == 1:            
#        creator_neigh500[key[0]] = neighbor_list_500m
#        creator_neigh2000[key[0]] = neighbor_list_2000m
#        creator_neigh5000[key[0]] = neighbor_list_5000m
#    else:
#        creator_neigh500[key] = neighbor_list_500m
#        creator_neigh2000[key] = neighbor_list_2000m
#        creator_neigh5000[key] = neighbor_list_5000m
#                
#        
#with open('IntermediateData/creator_neighbor_supply500m.pickle', 'wb') as handle:
#    pickle.dump(creator_neigh500, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#        
#with open('IntermediateData/creator_neighbor_supply2000m.pickle', 'wb') as handle:
#    pickle.dump(creator_neigh2000, handle, protocol=pickle.HIGHEST_PROTOCOL)
#    
#with open('IntermediateData/creator_neighbor_supply5000m.pickle', 'wb') as handle:
#    pickle.dump(creator_neigh5000, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#        


# In[ ]:


##
creator_neigh50 = {}
creator_neigh75 = {}
creator_neigh90 = {}
creator_neigh95 = {}
creator_neigh99 = {}

for key in creatorLocationMap.keys():
    neighbor_list_50 = []
    neighbor_list_75 = []
    neighbor_list_90 = []
    neighbor_list_95 = []
    neighbor_list_99 = []
    for elem in creatorLocationMap.keys():
        if key[0] == elem[0]:
            continue
        else:
            dist = calculate_distance_haversine(creatorLocationMap[(key)][0],creatorLocationMap[(key)][1],
                                               creatorLocationMap[(elem)][0],creatorLocationMap[(elem)][1])
            print(key,elem,dist)
            if dist <= 0.704:
                neighbor_list_50.append(elem)
                neighbor_list_75.append(elem)
                neighbor_list_90.append(elem)
                neighbor_list_95.append(elem)
                neighbor_list_99.append(elem)
                
            elif dist <= 1.778:
                neighbor_list_75.append(elem)
                neighbor_list_90.append(elem)
                neighbor_list_95.append(elem)
                neighbor_list_99.append(elem)
            
            elif dist <= 2.887:
                neighbor_list_90.append(elem)
                neighbor_list_95.append(elem)
                neighbor_list_99.append(elem)
            elif dist <= 3.53:
                neighbor_list_95.append(elem)
                neighbor_list_99.append(elem)
            elif dist <= 4.741:
                neighbor_list_99.append(elem)         
            else:
                continue
            
    if key[1] == 1:            
        creator_neigh50[key[0]] = neighbor_list_50
        creator_neigh75[key[0]] = neighbor_list_75
        creator_neigh90[key[0]] = neighbor_list_90
        creator_neigh95[key[0]] = neighbor_list_95
        creator_neigh99[key[0]] = neighbor_list_99
        
    else:
        creator_neigh50[key] = neighbor_list_50
        creator_neigh75[key] = neighbor_list_75
        creator_neigh90[key] = neighbor_list_90
        creator_neigh95[key] = neighbor_list_95
        creator_neigh99[key] = neighbor_list_99
        
                
        
with open('IntermediateData/creator_neighbor_supply50perc.pickle', 'wb') as handle:
    pickle.dump(creator_neigh50, handle, protocol=pickle.HIGHEST_PROTOCOL)

        
with open('IntermediateData/creator_neighbor_supply75perc.pickle', 'wb') as handle:
    pickle.dump(creator_neigh75, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
with open('IntermediateData/creator_neighbor_supply90perc.pickle', 'wb') as handle:
    pickle.dump(creator_neigh90, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('IntermediateData/creator_neighbor_supply95perc.pickle', 'wb') as handle:
    pickle.dump(creator_neigh95, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
with open('IntermediateData/creator_neighbor_supply99perc.pickle', 'wb') as handle:
    pickle.dump(creator_neigh99, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#



# In[223]:


#
#
#creator_neighDemand50 = {}
#creator_neighDemand75 = {}
#creator_neighDemand90 = {}
#creator_neighDemand95 = {}
#creator_neighDemand99 = {}
#
#for key in creatorLocationMap.keys():
#    neighbor_list_50 = []
#    neighbor_list_75 = []
#    neighbor_list_90 = []
#    neighbor_list_95 = []
#    neighbor_list_99 = []
#    
#    for elem in receiverLocationMap.keys():
#      #  print(key, elem)
#        if key[0] == elem[0]:
#            continue
#        else:
#            dist = calculate_distance_haversine(creatorLocationMap[(key)][0],creatorLocationMap[(key)][1],
#                                               receiverLocationMap[(elem)][0],receiverLocationMap[(elem)][1])
#            print(key,elem,dist)
#            if dist <= 0.704:
#                neighbor_list_50.append(elem)
#                neighbor_list_75.append(elem)
#                neighbor_list_90.append(elem)
#                neighbor_list_95.append(elem)
#                neighbor_list_99.append(elem)
#                
#            elif dist <= 1.778:
#                neighbor_list_75.append(elem)
#                neighbor_list_90.append(elem)
#                neighbor_list_95.append(elem)
#                neighbor_list_99.append(elem)
#                
#            elif dist <= 2.887:
#                neighbor_list_90.append(elem)
#                neighbor_list_95.append(elem)
#                neighbor_list_99.append(elem)
#            
#            elif dist <= 3.53:
#                neighbor_list_95.append(elem)
#                neighbor_list_99.append(elem)
#            elif dist <= 4.741:
#                neighbor_list_99.append(elem)     
#            else:
#                continue
#    if key[1] == 1:            
#        creator_neighDemand50[key[0]] = neighbor_list_50
#        creator_neighDemand75[key[0]] = neighbor_list_75
#        creator_neighDemand90[key[0]] = neighbor_list_90
#        creator_neighDemand95[key[0]] = neighbor_list_95
#        creator_neighDemand99[key[0]] = neighbor_list_99
#        
#    else:
#        creator_neighDemand50[key] = neighbor_list_50
#        creator_neighDemand75[key] = neighbor_list_75
#        creator_neighDemand90[key] = neighbor_list_90
#        creator_neighDemand95[key] = neighbor_list_95
#        creator_neighDemand99[key] = neighbor_list_99
#        
#                
#            
#        
#        
#     
#with open('IntermediateData/creator_neighbor_Demand50perc.pickle', 'wb') as handle:
#    pickle.dump(creator_neighDemand50, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#        
#with open('IntermediateData/creator_neighbor_Demand75perc.pickle', 'wb') as handle:
#    pickle.dump(creator_neighDemand75, handle, protocol=pickle.HIGHEST_PROTOCOL)
#    
#with open('IntermediateData/creator_neighbor_Demand90perc.pickle', 'wb') as handle:
#    pickle.dump(creator_neighDemand90, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#with open('IntermediateData/creator_neighbor_Demand95perc.pickle', 'wb') as handle:
#    pickle.dump(creator_neighDemand95, handle, protocol=pickle.HIGHEST_PROTOCOL)
#    
#with open('IntermediateData/creator_neighbor_Demand99perc.pickle', 'wb') as handle:
#    pickle.dump(creator_neighDemand99, handle, protocol=pickle.HIGHEST_PROTOCOL)
#        
