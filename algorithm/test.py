import re
a = 'favadaf1234[dfsfs]'
res = re.findall('va\w??',a)
print(res)