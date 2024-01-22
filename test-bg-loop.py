import pandas as pd
list = []
for i in range(10):
    list.append(i)

df = pd.DataFrame(list)   
print('hi') 
import json
details = {'Name': "Bob",
          'Age' :28}
  
with open('file.txt', 'w') as file:
     file.write(json.dumps(details))