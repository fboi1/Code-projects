import pandas as pd
import csv
# df = pd.read_csv(r"C:\firaas\code\addresses.csv", sep = r',')
# addresses = []
# print(df.columns)
# for i in range(df.shape[0]):
    
     
#     if '2-of' in df.iloc[i,2]:
#         addresses.append(df.iloc[i,2].split('2-of')[0])     
#     elif '3-of' in df.iloc[i,2]:
#         addresses.append(df.iloc[i,2].split('3-of')[0])  
#     elif '4-of' in df.iloc[i,2]:
#         addresses.append(df.iloc[i,2].split('4-of')[0]) 
#     elif 'wallet' in df.iloc[i,2]:
#         addresses.append(df.iloc[i,2].split('wallet')[0])     
#     elif ':' in df.iloc[i,2]:
#         addresses.append(df.iloc[i,2].split(':')[0])    
#     else:
#         addresses.append(df.iloc[i,2].split(':')[0])           
# print(addresses)

# address_df = pd.DataFrame(addresses)
# address_df.to_csv('addresses_cleaned.csv')

original = "EXAMPLE"
removed = original.replace("M", "")

#remove dots
df = pd.read_csv(r"C:\firaas\code\addresses_cleaned.csv", sep = r',')
addresses = []
print(df.columns)
for i in range(df.shape[0]):
    
     
    if '..' in df.iloc[i,1]:
       addresses.append(df.iloc[i,1].replace("..",""))
    else:
         addresses.append(df.iloc[i,1])    
print(addresses)

address_df = pd.DataFrame(addresses)

with open('addresses_cleaned3.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(addresses)
#address_df.to_csv('addresses_cleaned2.csv')
#print(address_df)
