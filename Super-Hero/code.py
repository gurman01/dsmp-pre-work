# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
#print(data)
#Code starts here 
data["Gender"].replace('-','Agender',inplace=True)
gender_count=data.Gender.value_counts()
gender_count.hist()


# --------------
#Code starts here
alignment=data.Alignment.value_counts()
plt.pie(alignment)
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
s=np.cov(sc_df.Strength,sc_df.Combat)
sc_covariance=round(s[0,1],2)
multi=sc_strength*sc_combat
sc_pearson=sc_covariance/multi
print(sc_pearson)
ic_df=data[['Intelligence','Combat']]
ic_intelligence=ic_df.Intelligence.std()
ic_combat=ic_df.Combat.std()
i=np.cov(ic_df.Intelligence,ic_df.Combat)
ic_covariance=round(i[0,1],2)
multi1=ic_intelligence*ic_combat
ic_pearson=ic_covariance/multi1
print(ic_pearson)


# --------------
#Code starts here
total_high= data.Total.quantile(0.99)
#print(total_high)
super_best=data[data['Total']>total_high]
#print(super_best)
super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here

f, (ax_1, ax_2, ax_3) = plt.subplots(3, sharex=True, sharey=True)

ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])



'''ax1.plot("Intelligence")
ax2.plot("Speed")
ax3.plot("Power")'''

'''
data.boxplot(Intelligence)
plt.title(Intelligence)
data.boxplot(Speed)
plt.title(Speed)
data.boxplot(Power)
plt.title(Power)'''


