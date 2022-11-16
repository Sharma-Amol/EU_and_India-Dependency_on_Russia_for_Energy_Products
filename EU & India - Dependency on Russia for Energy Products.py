#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis & Visualization
# by [Amol Sharma](https://www.linkedin.com/in/sharma-amol/)
# 
# Below datasets have been used for the sole purpose of showcasing my proficiency with various Python libraries. All data are latest iterations as available on 10th November 2022.
# 
# ## Primary Dataset 
# [Eurostat](https://ec.europa.eu/eurostat/databrowser/explore/all/envir?lang=en&subtheme=nrg&display=list&sort=category)
# 
# [Tradestat](https://tradestat.commerce.gov.in/eidb/)
# 
# [Directorate General of Commercial Intelligence and Statistics (Principal commodity level data)](http://ftddp.dgciskol.gov.in/)
# 
# 
# ## Customized Datasets  
# 
#  
# 
# ## Reference
# Eurostat Statistics Explained - [Energy statistics - an overview](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Energy_statistics_-_an_overview_)
#  
# 
# ## Aim
# Lighting, heating, transport, industry: energy is vital to run all essential day-to-day services and businesses. Through statistics, we can make the complex processes of the energy we use more understandable and answer questions regarding sources, form of energy,import dependency,etc.
# 
# **Part 1 - European Union**
# 
# The analysis has been done to answer following queries :-
# 1. EU wide trends in Production of Primary Energy by Fuel Type during 2010-2020.
# 2. EU wide Production of Primary Energy by Fuel Type in year 2020.
# 3. Across Europe which countries are Net Importers/exporters of energy products.
# 4. Decadal(2010-2020) trends in EU's dependency on Russia for Solid Fossil Fuel, Oil and Petroleum Products and Natural Gas import.
# 5. EU's top 5 sources of import for Solid Fossil Fuel, Oil and Petroleum Products and Natural Gas in last 5 years (2016-2020)
# 
# **Part 2 - India**
# 
# Following queries are answered :-
# 1. India's top 5 sources of import for Crude in last 5 years (2017-18 to 2021-22).
# 2. Trends in India's crude import from Russia in last 5 years.
# 3. Comparison between India's crude import from Russia between April-August 2022-23 and April-August 2021-22.
# 4. Trends in India's coal import from Russia in last 5 years (2017-18 to 2021-22).

# ## Part 1 European Union

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pd.ExcelFile('C:\\Users\\amols\\Portfolio Notebooks\\European Union\\Production of Primary Energy by fuel type.xls').sheet_names


# In[3]:


primary_production = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\European Union\\Production of Primary Energy by fuel type.xls',sheet_name=None)


# In[4]:


primary_production['2010']


# **Reference area** : Annual data series cover in principle all Member States of the European Union (27 countries), EFTA-countries (Iceland and Norway), EU candidate countries (Montenegro, North Macedonia, Albania, Serbia and Turkey) and potential candidate countries (Bosnia & Herzegovina and Kosovo). Data for Energy Community Contracting Parties are also available (in addition to countries listed before this covers Moldova, Ukraine and Georgia).
# 
# The EU and Eurozone aggregates are also shown.
# 
# **Remark** - Some data is missing/not reported. EU - 28 countries row is redundant after Britain left EU in 2020. Georgia and Bosnia and Herzegovina haven't reported respective figures. These rows can be dropped or replaced with a value. However, for the purpose of this study, I'll keep the data. 

# In[5]:


primary_production['2010'].info()


# In[6]:


primary_production['2010'].columns


# In[7]:


primary_production['2010'].index


# In[8]:


primary_production['2010'].set_index('GEO/SIEC',inplace=True)


# **Primary production of energy** is any extraction of energy products in a useable form from natural sources. This occurs either when natural sources are exploited (for example, in coal mines, crude oil fields, hydro power plants) or in the fabrication of biofuels.
# Transforming energy from one form into another, such as electricity or heat generation in thermal power plants (where primary energy sources are burned), or coke production in coke ovens, is not primary production.
# 
# **EU Energy Mix** = Renewables and biofuels + Solid fossil fuels + Natural gas + Crude oil + Nuclear heat + Others(Natural gas liquids + Additives and oxygenates (excluding biofuel portion) + Peat + Oil shale and oil sands + Other hydrocarbons + Industrial waste (non-renewable) + Non-renewable municipal waste + Heat)

# In[9]:


primary_production['2010']['Others'] = primary_production['2010']['O4200 - Natural gas liquids'] + primary_production['2010']['O4400X4410 - Additives and oxygenates (excluding biofuel portion)']+primary_production['2010']['O4500 - Other hydrocarbons']+primary_production['2010']['P1100 - Peat']+primary_production['2010']['S2000 - Oil shale and oil sands']+primary_production['2010']['W6100 - Industrial waste (non-renewable)']+primary_production['2010']['W6220 - Non-renewable municipal waste']+primary_production['2010']['H8000 - Heat']


# In[10]:


primary_production['2010'].drop(labels=['O4200 - Natural gas liquids','O4400X4410 - Additives and oxygenates (excluding biofuel portion)','O4500 - Other hydrocarbons','P1100 - Peat','S2000 - Oil shale and oil sands','W6100 - Industrial waste (non-renewable)','W6220 - Non-renewable municipal waste','H8000 - Heat'],inplace=True,axis=1)


# In[11]:


primary_production['2010']


# The same process can be repeated across all sheets through a for loop.

# In[12]:


x = 2011
for x in range(2011,2021):
    primary_production[f'{x}'] = primary_production[f'{x}'].set_index('GEO/SIEC')
    primary_production[f'{x}']['Others'] = primary_production[f'{x}']['O4200 - Natural gas liquids'] + primary_production[f'{x}']['O4400X4410 - Additives and oxygenates (excluding biofuel portion)']+primary_production[f'{x}']['O4500 - Other hydrocarbons']+primary_production[f'{x}']['P1100 - Peat']+primary_production[f'{x}']['S2000 - Oil shale and oil sands']+primary_production[f'{x}']['W6100 - Industrial waste (non-renewable)']+primary_production[f'{x}']['W6220 - Non-renewable municipal waste']+primary_production[f'{x}']['H8000 - Heat']
    primary_production[f'{x}'].drop(labels=['O4200 - Natural gas liquids','O4400X4410 - Additives and oxygenates (excluding biofuel portion)','O4500 - Other hydrocarbons','P1100 - Peat','S2000 - Oil shale and oil sands','W6100 - Industrial waste (non-renewable)','W6220 - Non-renewable municipal waste','H8000 - Heat'],inplace=True,axis=1)
    x = x+1


# In[13]:


primary_production['2020'].to_excel('EU Primary Production by fuel 2020.xlsx')


# **Query 1** - What is the EU wide trends in Production of Primary Energy by Fuel Type during 2010-2020?

# In[14]:


primary_energy_by_fuel_type = pd.DataFrame(columns=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])
a = 2010
for a in range (2010,2021):
    primary_energy_by_fuel_type[str(a)]=primary_production[str(a)].loc['European Union - 27 countries (from 2020)']
    a = a+1


# In[15]:


primary_energy_by_fuel_type


# In[16]:


a = 2011
for a in range(2011,2021):
    primary_energy_by_fuel_type[f'{a}']=(primary_energy_by_fuel_type[f'{a}']/primary_energy_by_fuel_type['2010'])*100
    a = a+1
primary_energy_by_fuel_type['2010']=(primary_energy_by_fuel_type['2010']/primary_energy_by_fuel_type['2010'])*100


# In[17]:


primary_energy_by_fuel_type


# In[18]:


primary_energy_by_fuel_type.to_excel('European Union - Production of Primary Energy by Fuel Type 2010-2020.xlsx')


# In[19]:


fig = plt.figure(figsize=(10,10),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['TOTAL - Total'],color='#de3131',label='TOTAL - Total',ls='-',lw=4)
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['C0000X0350-0370 - Solid fossil fuels'],color='#e37617',label = 'Solid fossil fuels',ls='--',lw=4)
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['G3000 - Natural gas'],color='#e3b717',label='Natural gas',ls='-.',lw=4)
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['O4100_TOT - Crude oil'],color='#76e317',label='Crude oil',ls=':',lw=4)
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['RA000 - Renewables and biofuels'],color='#17e3be',label='Renewables and biofuels',ls=(0,(5,1)),lw=4)
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['N900H - Nuclear heat'],color='#175ee3',label='Nuclear heat',ls=(0,(3,6,1,6,1,6)),lw=4)
ax.plot(primary_energy_by_fuel_type.columns,primary_energy_by_fuel_type.loc['Others'],color='#c817e3',label='Others',ls=(0,(3,1,1,1,1,1)),lw=4)
ax.set_ylabel('2010 = 100, Unit = Terajoule (TJ)')
plt.title("European Union - Production of Primary Energy by Fuel Type 2010-2020")
ax.legend(loc=(1.1,0.5))
plt.grid(visible=True,axis='y')
fig.savefig('European Union - Production of Primary Energy by Fuel Type 2010-2020.jpg',bbox_inches='tight')


# **Query 2** - What is the EU wide Production of Primary Energy by Fuel Type (as percentage of total)in year 2020?

# In[20]:


share_of_total_production_2020 = pd.DataFrame()
share_of_total_production_2020 = primary_production['2020'].loc['European Union - 27 countries (from 2020)']
share_of_total_production_2020


# In[21]:


share_of_total_production_2020.to_excel('EU Production of Primary Energy by fuel type 2020.xlsx')


# In[22]:


a = []
x=1
for x in range(1,7):
    a.append(((share_of_total_production_2020.iloc[x])/share_of_total_production_2020['TOTAL - Total'])*100)
    x = x+1


# In[23]:


plt.figure(figsize=(6,6),dpi=100)
plt.title('EU - Production of Primary Energy (as percentage of total) 2020')
plt.pie(x=a,labels=['Solid fossil fuels','Natural gas','Crude oil','Renewables and biofuels','Nuclear heat','Others'],autopct='%1.1f%%',explode = [0.05,0.08,0.1,0,0,0])
plt.savefig('EU - Production of Primary Energy (as percentage of total) 2020.jpg',bbox_inches='tight')
plt.show()


# The decrease in primary energy production in the EU over the past decades resulted in increased imports of primary energy and energy products.
# 
# **Query 3** - Across Europe which countries are Net Importers/exporters of energy products?

# In[24]:


Net_import_of_energy = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\European Union\\Primary Production, Imports, Exports (new).xlsx')


# In[25]:


Net_import_of_energy.head(10)


# In[26]:


Net_import_of_energy.index


# In[27]:


Net_import_of_energy.columns


# In[28]:


Net_import_of_energy.set_index('GEO (Labels)',inplace=True)


# Georgia and Bosnia & Herzegovina have Import/Export data missing. For purpose of illustration, we'll fill it as 0

# In[29]:


Net_import_of_energy.fillna(0,inplace=True)


# In[30]:


a = 2010
for a in range (2010,2022,2):
    Net_import_of_energy[f'{a} Net Imports'] = Net_import_of_energy[f'{a} Imports'] - Net_import_of_energy[f'{a} Exports']
    a = a+2
Net_import_of_energy


# In[31]:


Net_import_of_energy.to_excel('EU country wise net imports.xlsx')


# In[32]:


plt.figure(figsize=(10,10),dpi=100)
fig = sns.barplot(y = Net_import_of_energy.index,x = Net_import_of_energy['2020 Net Imports'],orient='h')
fig.set(xlabel="Net Imports (Thousand tonnes of oil equivalent)")
plt.title('EU - Country Wise Net Imports 2020')
plt.savefig('EU - Country Wise Net Imports 2020.jpg',bbox_inches='tight')
plt.show()


# **Query 4** What are the decadal(2010-2020) trends in EU's dependency on Russia for Solid Fossil Fuel, Oil and Petroleum Products and Natural Gas import.
# 
# **Query 5** Which Countries are EU's top 5 sources of import for Solid Fossil Fuel, Oil and Petroleum Products and Natural Gas in last 5 years (2016-2020)

# In[33]:


solid_fossil_import = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\European Union\\EU Solid Fossil Fuel Import by country.xlsx',sheet_name='Sheet 1')


# In[34]:


solid_fossil_import.head(20)


# In[35]:


# Russia at 18
year = []
russia_sff_import = []
total_sff_import = []
a = 2010
for a in range (2010,2021):
    year.append(a)
    russia_sff_import.append(solid_fossil_import.at[16,str(a)])
    total_sff_import.append(solid_fossil_import[str(a)].sum())


# In[36]:


russia_total_sff_import = pd.DataFrame(data=np.array([russia_sff_import,total_sff_import]),index = ['Russia','Total'],columns=year)
russia_total_sff_import.loc['Percentage'] = (russia_total_sff_import.loc['Russia']/russia_total_sff_import.loc['Total'])*100


# In[37]:


russia_total_sff_import


# In[38]:


russia_total_sff_import.to_excel('EU russia total sff import 2010-2020.xlsx')


# In[39]:


fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(10,5),dpi=100)
ax[0].plot(russia_total_sff_import.columns,russia_total_sff_import.loc['Russia'],color='r')
ax[0].grid()
ax[0].set_title('EU - Solid Fossil Fuel Imports From Russia')
ax[0].set_ylabel('Thousand tonnes')
ax[1].bar(russia_total_sff_import.columns,russia_total_sff_import.loc['Total'])
ax[1].plot(russia_total_sff_import.columns,russia_total_sff_import.loc['Russia'],color='r',label = 'Russia')
ax[1].legend(loc = 'upper left')
ax[1].set_title('EU - Overall Solid Fossil Fuel Imports')
ax[1].set_ylabel('Thousand tonnes')
fig.suptitle('EU - Solid Fossil Fuel Imports')
plt.tight_layout()
fig.savefig('EU - Solid Fossil Fuel Imports.jpg',bbox_inches='tight')


# In[40]:


import_2016 = solid_fossil_import[['PARTNER (Labels)','2016']].nlargest(n=5,columns='2016')
import_2017 = solid_fossil_import[['PARTNER (Labels)','2017']].nlargest(n=5,columns='2017')
import_2018 = solid_fossil_import[['PARTNER (Labels)','2018']].nlargest(n=5,columns='2018')
import_2019 = solid_fossil_import[['PARTNER (Labels)','2019']].nlargest(n=5,columns='2019')
import_2020 = solid_fossil_import[['PARTNER (Labels)','2020']].nlargest(n=5,columns='2020')


# In[41]:


fig,((ax1,ax2,ax3,ax4,ax5)) = plt.subplots(nrows=1,ncols=5,figsize=(15,5),dpi=100,)
fig.suptitle('EU- Country Wise Solid Fossil Fuel Imports 2016-2020')
ax1.bar(import_2016['PARTNER (Labels)'],import_2016['2016'])
ax1.set_title('2016')
ax1.set_ylabel('Thousand tonnes')
ax1.tick_params('x',labelrotation=90)
ax2.bar(import_2017['PARTNER (Labels)'],import_2017['2017'])
ax2.set_title('2017')
ax2.tick_params('x',labelrotation=90)
ax2.set_ylabel('Thousand tonnes')
ax3.bar(import_2018['PARTNER (Labels)'],import_2018['2018'])
ax3.set_title('2018')
ax3.tick_params('x',labelrotation=90)
ax3.set_ylabel('Thousand tonnes')
ax4.bar(import_2019['PARTNER (Labels)'],import_2019['2019'])
ax4.set_title('2019')
ax4.tick_params('x',labelrotation=90)
ax4.set_ylabel('Thousand tonnes')
ax5.bar(import_2020['PARTNER (Labels)'],import_2020['2020'])
ax5.set_title('2020')
ax5.tick_params('x',labelrotation=90)
ax5.set_ylabel('Thousand tonnes')
fig.savefig('EU- Country Wise Solid Fossil Fuel Imports 2016-2020.jpg',bbox_inches='tight')
plt.tight_layout()


# In[42]:


oil_petroleum_import = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\European Union\\EU Imports of oil and petroleum products by country.xlsx',sheet_name='Sheet 1')


# In[43]:


oil_petroleum_import.head(20)


# In[44]:


# Russia at 16
year = []
russia_oil_petrol_import = []
total_oil_petrol_import = []
a = 2010
for a in range (2010,2021):
    year.append(a)
    russia_oil_petrol_import.append(oil_petroleum_import.at[16,str(a)])
    total_oil_petrol_import.append(oil_petroleum_import[str(a)].sum())
russia_total_oil_petrol_import = pd.DataFrame(data=np.array([russia_oil_petrol_import,total_oil_petrol_import]),index = ['Russia','Total'],columns=year)
russia_total_oil_petrol_import.loc['Percentage'] = (russia_total_oil_petrol_import.loc['Russia']/russia_total_oil_petrol_import.loc['Total'])*100


# In[45]:


russia_total_oil_petrol_import


# In[46]:


russia_total_oil_petrol_import.to_excel('EU russia total oil petrol import 2010-2020.xlsx')


# In[47]:


fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(10,5),dpi=100)
ax[0].plot(russia_total_oil_petrol_import.columns,russia_total_oil_petrol_import.loc['Russia'],color='r')
ax[0].grid()
ax[0].set_title('EU - Oil and Petrol Imports From Russia')
ax[0].set_ylabel('Thousand tonnes')
ax[1].bar(russia_total_oil_petrol_import.columns,russia_total_oil_petrol_import.loc['Total'])
ax[1].plot(russia_total_oil_petrol_import.columns,russia_total_oil_petrol_import.loc['Russia'],color='r',label = 'Russia')
ax[1].legend(loc = 'best')
ax[1].set_title('EU - Overall Oil and Petrol Imports')
ax[1].set_ylabel('Thousand tonnes')
fig.suptitle('EU - Oil and Petrol Imports')
fig.savefig('EU - Oil and Petrol Imports.jpg',bbox_inches='tight')
plt.tight_layout()


# In[48]:


oil_petroleum_import.drop(136,axis=0,inplace=True)


# In[49]:


import_2016 = oil_petroleum_import[['PARTNER (Labels)','2016']].nlargest(n=5,columns='2016')
import_2017 = oil_petroleum_import[['PARTNER (Labels)','2017']].nlargest(n=5,columns='2017')
import_2018 = oil_petroleum_import[['PARTNER (Labels)','2018']].nlargest(n=5,columns='2018')
import_2019 = oil_petroleum_import[['PARTNER (Labels)','2019']].nlargest(n=5,columns='2019')
import_2020 = oil_petroleum_import[['PARTNER (Labels)','2020']].nlargest(n=5,columns='2020')


# In[50]:


fig,((ax1,ax2,ax3,ax4,ax5)) = plt.subplots(nrows=1,ncols=5,figsize=(15,5),dpi=100,)
fig.suptitle('EU- Country Wise Oil and Petroleum Imports 2016-2020')
ax1.bar(import_2016['PARTNER (Labels)'],import_2016['2016'])
ax1.set_title('2016')
ax1.tick_params('x',labelrotation=90)
ax1.set_ylabel('Thousand tonnes')
ax2.bar(import_2017['PARTNER (Labels)'],import_2017['2017'])
ax2.set_title('2017')
ax2.tick_params('x',labelrotation=90)
ax2.set_ylabel('Thousand tonnes')
ax3.bar(import_2018['PARTNER (Labels)'],import_2018['2018'])
ax3.set_title('2018')
ax3.tick_params('x',labelrotation=90)
ax3.set_ylabel('Thousand tonnes')
ax4.bar(import_2019['PARTNER (Labels)'],import_2019['2019'])
ax4.set_title('2019')
ax4.tick_params('x',labelrotation=90)
ax4.set_ylabel('Thousand tonnes')
ax5.bar(import_2020['PARTNER (Labels)'],import_2020['2020'])
ax5.set_title('2020')
ax5.tick_params('x',labelrotation=90)
ax5.set_ylabel('Thousand tonnes')
fig.savefig('EU- Country Wise Oil and Petroleum Imports 2016-2020.jpg',bbox_inches='tight')
plt.tight_layout()


# In[51]:


natural_gas_import = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\European Union\\EU Imports of natural gas by country.xlsx',sheet_name='Sheet 1')


# In[52]:


natural_gas_import.head(20)


# In[53]:


# Russia at 16
year = []
russia_natural_gas_import = []
total_natural_gas_import = []
a = 2010
for a in range (2010,2021):
    year.append(a)
    russia_natural_gas_import.append(natural_gas_import.at[16,str(a)])
    total_natural_gas_import.append(natural_gas_import[str(a)].sum())
russia_total_natural_gas_import = pd.DataFrame(data=np.array([russia_natural_gas_import,total_natural_gas_import]),index = ['Russia','Total'],columns=year)
russia_total_natural_gas_import.loc['Percentage'] = (russia_total_natural_gas_import.loc['Russia']/russia_total_natural_gas_import.loc['Total'])*100


# In[54]:


russia_total_natural_gas_import


# In[55]:


russia_total_natural_gas_import.to_excel('EU russia total natural gas import 2010-2020.xlsx')


# In[56]:


fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(10,5),dpi=100)
ax[0].plot(russia_total_natural_gas_import.columns,russia_total_natural_gas_import.loc['Russia'],color='r')
ax[0].grid()
ax[0].set_title('EU - Natural Gas Imports From Russia')
ax[0].set_ylabel('Million cubic metres')
ax[1].bar(russia_total_natural_gas_import.columns,russia_total_natural_gas_import.loc['Total'])
ax[1].plot(russia_total_natural_gas_import.columns,russia_total_natural_gas_import.loc['Russia'],color='r',label = 'Russia')
ax[1].legend(loc = 'upper left')
ax[1].set_title('EU - Overall Natural Gas Imports')
ax[1].set_ylabel('Million cubic metres')
fig.suptitle('EU - Natural Gas Imports')
fig.savefig('EU - Natural Gas Imports.jpg',bbox_inches='tight')
plt.tight_layout()


# In[57]:


natural_gas_import.drop(136,axis=0,inplace=True)


# In[58]:


import_2016 = natural_gas_import[['PARTNER (Labels)','2016']].nlargest(n=5,columns='2016')
import_2017 = natural_gas_import[['PARTNER (Labels)','2017']].nlargest(n=5,columns='2017')
import_2018 = natural_gas_import[['PARTNER (Labels)','2018']].nlargest(n=5,columns='2018')
import_2019 = natural_gas_import[['PARTNER (Labels)','2019']].nlargest(n=5,columns='2019')
import_2020 = natural_gas_import[['PARTNER (Labels)','2020']].nlargest(n=5,columns='2020')


# In[59]:


fig,((ax1,ax2,ax3,ax4,ax5)) = plt.subplots(nrows=1,ncols=5,figsize=(15,5),dpi=100,)
fig.suptitle('EU- Country Wise Natural Gas Imports 2016-2020')
ax1.bar(import_2016['PARTNER (Labels)'],import_2016['2016'])
ax1.set_title('2016')
ax1.tick_params('x',labelrotation=90)
ax1.set_ylabel('Million cubic metres')
ax2.bar(import_2017['PARTNER (Labels)'],import_2017['2017'])
ax2.set_title('2017')
ax2.tick_params('x',labelrotation=90)
ax2.set_ylabel('Million cubic metres')
ax3.bar(import_2018['PARTNER (Labels)'],import_2018['2018'])
ax3.set_title('2018')
ax3.tick_params('x',labelrotation=90)
ax3.set_ylabel('Million cubic metres')
ax4.bar(import_2019['PARTNER (Labels)'],import_2019['2019'])
ax4.set_title('2019')
ax4.tick_params('x',labelrotation=90)
ax4.set_ylabel('Million cubic metres')
ax5.bar(import_2020['PARTNER (Labels)'],import_2020['2020'])
ax5.set_title('2020')
ax5.tick_params('x',labelrotation=90)
ax5.set_ylabel('Million cubic metres')
fig.savefig('EU- Country Wise Natural Gas Imports 2016-2020.jpg',bbox_inches='tight')
plt.tight_layout()


# ## Part 2 India

# ![India%20Energy%20Balance%20%28Niti%29.png](attachment:India%20Energy%20Balance%20%28Niti%29.png)
# According to Niti Aayog's [India Energy Dashboards](https://www.niti.gov.in/edm/#home) 
# 1. India’s energy needs are largely met by two fuels – coal and crude (91.85 % of Total). 
# 2. Coal (domestic + Import) alone accounts for 56.31 % of total primary energy supply. 
# 3. Crude, 55.79 % of all energy product import, accounts for 35.53 % of total primary energy supply.
# 4. Rest of primary energy mix is comprised of Natural Gas, Lignite, Renewables and Nuclear energy.

# **Query 1** India's top 5 sources of import for Crude in last 5 years (2017-18 to 2021-22).
# 
# **Query 2** Trends in India's crude import from Russia in last 5 years.
# 
# **Query 3** Comparison between India's crude import from Russia between April-August 2022-23 and April-August 2021-22.
# 
# **Query 4** Trends in India's coal import from Russia in last 5 years (2017-18 to 2021-22).

# In[60]:


pd.ExcelFile('C:\\Users\\amols\\Portfolio Notebooks\\India Crude and Natural Gas\\HS 2709 Country wise Import in $.xlsx').sheet_names


# In[61]:


india_crude_import = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\India Crude and Natural Gas\\HS 2709 Country wise Import in $.xlsx',sheet_name=None,index_col=0)


# In[62]:


# An excel file with multiple sheets is read as a dictionary. It will have sheet name as keys and sheet itself as values.
india_crude_import.values()


# All sheets have last 3 entries as Total, India's Total Imports and % share. For our visualization we'll drop these entries from all sheets.
# We'll also convert all NaN values to 0 for sorting.

# In[63]:


index1 = ['2017-18','2018-19','2019-20','2020-21','2021-22','2022-23\n(Apr-Aug)']
value = []
value1 = []
a = 2017
b = 18
for a in range (2017,2023):
    india_crude_import[f'{a}-{b}']=india_crude_import[f'{a}-{b}'].where(pd.notnull(india_crude_import[f'{a}-{b}']),0)
    india_crude_import[f'{a}-{b}'].set_index('Country / Region',inplace=True)
    india_crude_import[f'{a}-{b}'].rename(columns={india_crude_import[f'{a}-{b}'].columns[0]:'Amount'},inplace=True)
    value.append(india_crude_import[f'{a}-{b}'].at['RUSSIA','Amount'])
    value1.append(india_crude_import[f'{a}-{b}'].at['Total','Amount'])
    india_crude_import[f'{a}-{b}'].drop(india_crude_import[f'{a}-{b}'].tail(3).index,inplace=True)
     
    a = a+1
    b = b+1
indcrude_overall_russia =pd.DataFrame(data=value,index=index1,columns=['Russia'])
indcrude_overall = pd.DataFrame(data=value1,index=index1,columns=['Total'])


# In[64]:


indcrude_overall_russia


# In[65]:


indcrude_overall_russia.to_excel('India russia crude import.xlsx')
indcrude_overall.to_excel('India total crude import.xlsx')


# In[66]:


fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(10,5),dpi=100)
ax[0].plot(indcrude_overall_russia.index,indcrude_overall_russia['Russia']/1000,color='r')
ax[0].grid()
ax[0].set_title('India - Crude Imports From Russia')
ax[0].set_ylabel('Billion $')
ax[1].bar(indcrude_overall.index,indcrude_overall['Total']/1000)
ax[1].plot(indcrude_overall_russia.index,indcrude_overall_russia['Russia']/1000,color='r',label = 'Russia')
ax[1].legend(loc = 'upper left')
ax[1].set_title('India - Overall Crude Imports')
ax[1].set_ylabel('Billion $')
fig.suptitle('India - Crude Imports')
fig.savefig('India - Crude Imports.jpg',bbox_inches='tight')
plt.tight_layout()


# In[67]:


indcrude_202223_top5 = india_crude_import['2022-23'].nlargest(5,india_crude_import['2022-23'].columns)
indcrude_202122_top5 = india_crude_import['2021-22'].nlargest(5,india_crude_import['2021-22'].columns)
indcrude_202021_top5 = india_crude_import['2020-21'].nlargest(5,india_crude_import['2020-21'].columns)
indcrude_201920_top5 = india_crude_import['2019-20'].nlargest(5,india_crude_import['2019-20'].columns)
indcrude_201819_top5 = india_crude_import['2018-19'].nlargest(5,india_crude_import['2018-19'].columns)
indcrude_201718_top5 = india_crude_import['2017-18'].nlargest(5,india_crude_import['2017-18'].columns)


# In[68]:


fig,ax = plt.subplots(nrows=2,ncols=3,figsize=(10,6),dpi=100)
ax[0][0].bar(x=indcrude_201718_top5.index,height=indcrude_201718_top5['Amount']/1000)
ax[0][0].set_title('2017-18')
ax[0][0].tick_params('x',labelrotation=90)
ax[0][0].set_ylabel('Billion $')
ax[0][1].bar(x=indcrude_201819_top5.index,height=indcrude_201819_top5['Amount']/1000)
ax[0][1].set_title('2018-19')
ax[0][1].tick_params('x',labelrotation=90)
ax[0][1].set_ylabel('Billion $')
ax[0][2].bar(x=indcrude_201920_top5.index,height=indcrude_201920_top5['Amount']/1000)
ax[0][2].set_title('2019-20')
ax[0][2].tick_params('x',labelrotation=90)
ax[0][2].set_ylabel('Billion $')
ax[1][0].bar(x=indcrude_202021_top5.index,height=indcrude_202021_top5['Amount']/1000)
ax[1][0].set_title('2020-21')
ax[1][0].tick_params('x',labelrotation=90)
ax[1][0].set_ylabel('Billion $')
ax[1][1].bar(x=indcrude_202122_top5.index,height=indcrude_202122_top5['Amount']/1000)
ax[1][1].set_title('2021-22')
ax[1][1].tick_params('x',labelrotation=90)
ax[1][1].set_ylabel('Billion $')
ax[1][2].bar(x=indcrude_202223_top5.index,height=indcrude_202223_top5['Amount']/1000)
ax[1][2].set_title('2022-2023(Apr-Aug)')
ax[1][2].tick_params('x',labelrotation=90)
ax[1][2].set_ylabel('Billion $')
fig.suptitle('India - Country wise Crude Imports')
fig.savefig('India - Country wise Crude Imports.jpg',bbox_inches='tight')
plt.tight_layout()


# In[69]:


indcrude_import_apraug21 = pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\India Crude and Natural Gas\\Directorate General of Commercial Intelligence and Statistics Crude Data 2021 (Apr-Aug).xls',index_col=0)


# In[70]:


indcrude_import_apraug21


# In[71]:


indcrude_import_apraug21_top5 = indcrude_import_apraug21[['Country of Consignment','April, 21 To August, 21 Value(US $)']].nlargest(5,'April, 21 To August, 21 Value(US $)')


# In[72]:


fig,((ax1,ax2)) = plt.subplots(nrows=1,ncols=2,figsize=(5,5),dpi=100)
ax1.bar(indcrude_202223_top5.index,indcrude_202223_top5['Amount']/1000)
ax1.tick_params('x',labelrotation=90)
ax1.set_title('2022-23 (April-August)')
ax1.set_ylabel ('Billion $')
ax2.bar(indcrude_import_apraug21_top5['Country of Consignment'],indcrude_import_apraug21_top5['April, 21 To August, 21 Value(US $)']/1000000000)
ax2.tick_params('x',labelrotation=90)
ax2.set_title('2021-22 (April-August)')
ax2.set_ylabel ('Billion $')
fig.suptitle('India Crude Imports')
fig.savefig('India Crude Imports April-August.jpg',bbox_inches='tight')
plt.tight_layout()


# In[73]:


pd.ExcelFile('C:\\Users\\amols\\Portfolio Notebooks\\India Crude and Natural Gas\\HS 2701  Country wise Import in $.xlsx').sheet_names


# In[74]:


ind_coal_import=pd.read_excel('C:\\Users\\amols\\Portfolio Notebooks\\India Crude and Natural Gas\\HS 2701  Country wise Import in $.xlsx',sheet_name=None,index_col=0)


# In[75]:


ind_coal_import


# In[76]:


index1 = ['2017-18','2018-19','2019-20','2020-21','2021-22','2022-23\n(Apr-Aug)']
value = []
value1 = []
a = 2017
b = 18
for a in range (2017,2023):
    ind_coal_import[f'{a}-{b}'].set_index('Country / Region',inplace=True)
    ind_coal_import[f'{a}-{b}'].rename(columns={ind_coal_import[f'{a}-{b}'].columns[0]:'Amount'},inplace=True)
    value.append(ind_coal_import[f'{a}-{b}'].at['RUSSIA','Amount'])
    value1.append(ind_coal_import[f'{a}-{b}'].at['Total','Amount'])
    a = a+1
    b = b+1
indcoal_overall_russia =pd.DataFrame(data=value,index=index1,columns=['Russia'])
indcoal_overall = pd.DataFrame(data=value1,index=index1,columns=['Total'])


# In[77]:


indcoal_overall_russia.to_excel('India russia coal import.xlsx')
indcoal_overall.to_excel('India total crude import.xlsx')


# In[78]:


fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(10,5),dpi=100)
ax[0].plot(indcoal_overall_russia.index,indcoal_overall_russia['Russia']/1000,color='r')
ax[0].grid()
ax[0].set_title('India - Coal Imports From Russia')
ax[0].set_ylabel('Billion $')
ax[1].bar(indcoal_overall.index,indcoal_overall['Total']/1000)
ax[1].plot(indcoal_overall_russia.index,indcoal_overall_russia['Russia']/1000,color='r',label = 'Russia')
ax[1].legend(loc = 'upper left')
ax[1].set_title('India - Overall Coal Imports')
ax[1].set_ylabel('Billion $')
fig.suptitle('India - Coal Imports')
fig.savefig('India - Coal Imports.jpg',bbox_inches='tight')
plt.tight_layout()

