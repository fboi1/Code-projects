import json
from datetime import datetime
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
startTime = datetime.now()
# open file for writing
f = open("C:\\firaas\\code\\productbook55.txt","w")

# write file
f.write(str(dict))
# with open('dict4.txt', 'w') as convert_file:
#     convert_file.write(json.dumps(dict))
# close file
f.close()
print(datetime.now() - startTime)