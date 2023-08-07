#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

with open('summary-residential-community-data.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print(data)


# In[2]:


data[5]


# In[3]:


data[0]['year']


# In[4]:


len(data)


# In[5]:


year_list = []
postcode_list = []
suburb_list = []
emission_source_list = []
geo_shape_geometry_type_list = []
geo_shape_properties_list = []
geo_point_2d_list = []
scope_1_kg_co2e_list = []
scope_2_kg_co2e_list = []
scope_3_kg_co2e_list = []

for a in range(0,len(data)):
#     print(a)
    year_list.append(data[a]['year'])
    postcode_list.append(data[a]['postcode'])
    suburb_list.append(data[a]['suburb'])
    emission_source_list.append(data[a]['emission_source'])
    geo_shape_geometry_type_list.append(data[a]['geo_shape']['geometry']['type'])
    geo_shape_properties_list.append(data[a]['geo_shape']['properties'])
    geo_point_2d_list.append(data[a]['geo_point_2d'])
    scope_1_kg_co2e_list.append(data[a]['scope_1_kg_co2e'])
    scope_2_kg_co2e_list.append(data[a]['scope_2_kg_co2e'])
    scope_3_kg_co2e_list.append(data[a]['scope_3_kg_co2e'])
    
# year_list
# emission_source_list


# In[6]:


import pandas as pd

df = pd.DataFrame(list(zip(year_list, 
                           postcode_list, 
                           suburb_list, 
                           emission_source_list, 
                           geo_shape_geometry_type_list, 
                           geo_shape_properties_list, 
                           geo_point_2d_list,
                           scope_1_kg_co2e_list,
                           scope_2_kg_co2e_list,
                           scope_3_kg_co2e_list)),
                  
               columns =['year', 
                         'postcode',
                         'suburb_list', 
                         'emission_source_list', 
                         'geo_shape_geometry_type_list', 
                         'geo_shape_properties_list', 
                         'geo_point_2d_list',
                         'scope_1_kg_co2e_list',
                         'scope_2_kg_co2e_list',
                         'scope_3_kg_co2e_list'])
df


# In[93]:


# dup_row = df.duplicated(subset=None, keep=False)
# df.insert(0, 'is_dup', dup_row)
# df[df['is_dup'] == True]


# In[91]:


df['geo_point_2d_list']


# In[89]:


df['geo_shape_properties_list']


# In[69]:


df['geo_shape_geometry_type_list'].unique()


# In[79]:


df['suburb_list'].unique()


# In[80]:


df['postcode'].unique()


# In[50]:


Dict = dict(zip(df['suburb_list'],df['postcode']))
Dict


# In[51]:


pd.crosstab(df['suburb_list'],df['postcode'])


# In[2]:


import pandas as pd

ele_year_list = []
ele_postcode_list = []
ele_total_electricity_kwh_list = []
ele_total_emissions_kg_co2e_list = []
ele_average_intensity_kwh_per_customer_per_annum_list = []
ele_average_emissions_kg_co2e_per_customer_per_annum_list = []
ele_rest_of_municipality_total_electricity_kwh_list = []
ele_rest_of_municipality_emissions_kg_co2e_list = []

gas_year_list = []
gas_postcode_list = []
gas_total_gas_gj_list = []
gas_total_emissions_kg_co2e_list = []
gas_average_intensity_gj_per_customer_per_annum_list = []
gas_average_emissions_kg_co2e_per_customer_per_annum_list = []
gas_rest_of_municipality_total_gas_gj_list = []
gas_rest_of_municipality_emissions_kg_co2e_list = []

geo_postcode_list = []
geo_shape_geometry_coordinates_list = []
geo_shape_geometry_type_list = []
geo_point_2d_list = []


for each in range(0,len(data)):
    if data[each]['emission_source'] == 'Electricity':
        ele_year_list.append(data[each]['year'])
        ele_postcode_list.append(data[each]['postcode'])
        ele_total_electricity_kwh_list.append(data[each]['total_electricity_kwh'])
        ele_total_emissions_kg_co2e_list.append(data[each]['total_emissions_kg_co2e'])
        ele_average_intensity_kwh_per_customer_per_annum_list.append(data[each]['average_intensity_kwh_per_customer_per_annum'])
        ele_average_emissions_kg_co2e_per_customer_per_annum_list.append(data[each]['average_emissions_per_customer_kg_co2e'])
        ele_rest_of_municipality_total_electricity_kwh_list.append(data[each]['rest_of_municipality_total_electricity_kwh'])
        ele_rest_of_municipality_emissions_kg_co2e_list.append(data[each]['rest_of_municipality_emissions_kg_co2e'])

        
    if data[each]['emission_source'] == 'Gas':
        gas_year_list.append(data[each]['year'])
        gas_postcode_list.append(data[each]['postcode'])
        gas_total_gas_gj_list.append(data[each]['total_gas_gj'])
        gas_total_emissions_kg_co2e_list.append(data[each]['total_emissions_kg_co2e'])
        gas_average_intensity_gj_per_customer_per_annum_list.append(data[each]['average_intensity_gj_per_customer_per_annum'])
        gas_average_emissions_kg_co2e_per_customer_per_annum_list.append(data[each]['average_emissions_per_customer_kg_co2e'])
        gas_rest_of_municipality_total_gas_gj_list.append(data[each]['rest_of_municipality_total_gas_gj'])
        gas_rest_of_municipality_emissions_kg_co2e_list.append(data[each]['rest_of_municipality_emissions_kg_co2e'])

    if data[each]['postcode'] not in geo_postcode_list:
        geo_postcode_list.append(data[each]['postcode'])
        geo_shape_geometry_coordinates_list.append(data[each]['geo_shape']['geometry']['coordinates'])    
        geo_shape_geometry_type_list.append(data[each]['geo_shape']['geometry']['type'])
        geo_point_2d_list.append(data[each]['geo_point_2d'])


# In[3]:


df_geo = pd.DataFrame(list(zip(geo_postcode_list,
                               geo_shape_geometry_coordinates_list,
                               geo_shape_geometry_type_list,
                               geo_point_2d_list)),
                  
               columns =['geo_postcode_list',
                         'geo_shape_geometry_coordinates',
                         'geo_shape_geometry_type',
                         'geo_point_2d'])
df_geo


# In[8]:


df_ele = pd.DataFrame(list(zip(ele_year_list, 
                           ele_postcode_list, 
                           ele_total_electricity_kwh_list, 
                           ele_total_emissions_kg_co2e_list, 
                           ele_average_intensity_kwh_per_customer_per_annum_list, 
                           ele_average_emissions_kg_co2e_per_customer_per_annum_list, 
                           ele_rest_of_municipality_total_electricity_kwh_list,
                           ele_rest_of_municipality_emissions_kg_co2e_list)),
                  
               columns =['year', 
                         'postcode',
                         'total_electricity_kwh', 
                         'total_emissions_kg_co2e', 
                         'average_intensity_kwh_per_customer_per_annum',
                         'average_emissions_kg_co2e_per_customer_per_annum',
                         'rest_of_municipality_total_electricity_kwh',
                         'rest_of_municipality_emissions_kg_co2e'])

df_ele = df_ele.dropna(axis=0,how='any')

df_ele = df_ele.groupby('postcode')[['total_electricity_kwh', 
                         'total_emissions_kg_co2e', 
                         'average_intensity_kwh_per_customer_per_annum',
                         'average_emissions_kg_co2e_per_customer_per_annum',
                         'rest_of_municipality_total_electricity_kwh',
                         'rest_of_municipality_emissions_kg_co2e']].mean()

df_ele = df_ele.reset_index()
df_ele['emission_source'] = 'Electricity'
df_ele
df_ele.to_csv('df_ele.csv', index=False)


# In[9]:


df_ele


# In[10]:


# print(gas_geo_point_2d_list)
df_gas = pd.DataFrame(list(zip(gas_year_list, 
                           gas_postcode_list, 
                           gas_total_gas_gj_list, 
                           gas_total_emissions_kg_co2e_list, 
                           gas_average_intensity_gj_per_customer_per_annum_list, 
                           gas_average_emissions_kg_co2e_per_customer_per_annum_list, 
                           gas_rest_of_municipality_total_gas_gj_list,
                           gas_rest_of_municipality_emissions_kg_co2e_list)),
                      
               columns =['year', 
                         'postcode',
                         'total_gas_gj', 
                         'total_emissions_kg_co2e', 
                         'average_intensity_gj_per_customer_per_annum',
                         'average_emissions_kg_co2e_per_customer_per_annum',
                         'rest_of_municipality_total_gas_gj',
                         'rest_of_municipality_emissions_kg_co2e'])

df_gas = df_gas.dropna(axis=0,how='any')

df_gas = df_gas.groupby('postcode')[['total_gas_gj', 
                         'total_emissions_kg_co2e', 
                         'average_intensity_gj_per_customer_per_annum',
                         'average_emissions_kg_co2e_per_customer_per_annum',
                         'rest_of_municipality_total_gas_gj',
                         'rest_of_municipality_emissions_kg_co2e']].mean()

df_gas = df_gas.reset_index()
df_gas['emission_source'] = 'Gas'
df_gas
df_gas.to_csv('df_gas.csv', index=False)


# In[11]:


df_gas


# In[8]:


ele_coef = df_ele['total_emissions_kg_co2e'].sum()/df_ele['total_electricity_kwh'].sum()
ele_coef


# In[10]:


gas_coef = df_gas['total_emissions_kg_co2e'].sum()/df_gas['total_gas_gj'].sum()
gas_coef


# In[ ]:





# In[ ]:





# In[5]:


import pandas as pd

year_list = []
postcode_list = []
emission_source_list = []
average_emissions_per_customer_kg_co2e_list = []

for a in range(0,len(data)):
    year_list.append(data[a]['year'])
    postcode_list.append(data[a]['postcode'])
    emission_source_list.append(data[a]['emission_source'])
    average_emissions_per_customer_kg_co2e_list.append(data[a]['average_emissions_per_customer_kg_co2e'])


# In[23]:


df_total = pd.DataFrame(list(zip(year_list, 
                           postcode_list, 
                           emission_source_list, 
                           average_emissions_per_customer_kg_co2e_list)),
                  
               columns =['year', 
                         'postcode',
                         'emission_source', 
                         'average_emissions_per_customer_kg_co2e'])
df_total


# In[24]:


df_total


# In[33]:


df_total = df_total.dropna(axis=0,how='any')

df_total = df_total.groupby('postcode')[['average_emissions_per_customer_kg_co2e']].sum()
df_total_per_month = df_total.reset_index()

df_total_per_month['average_emissions_per_customer_kg_co2e_per_month'] = df_total_per_month['average_emissions_per_customer_kg_co2e'].map(lambda x: x/3/12)
df_total_per_month = df_total_per_month.drop(columns=['average_emissions_per_customer_kg_co2e'])
df_total_per_month

df_total_per_month.to_csv('df_total_per_month.csv', index=False)


# In[34]:





# In[ ]:




