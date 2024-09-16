# dictionary => Mapping Table
words={}
words["1"]="One"    #新增key = "1"，value = "one"
words["2"]="Two"    #新增key = "2"，value = "two"
words["3"]="three"  #新增key = "3"，value = "three"

print(words["1"], "", words["2"])

del words["2"]  #刪除key = 2的項
print(words)