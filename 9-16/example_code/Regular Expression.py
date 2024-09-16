import re

#findall在字串中找到任何符合regular expression 的子字串
pattern = re.compile (r'\b[a-z]+[A-Z0-9]*\b')
res=pattern.findall('a123 b123')
print(res)

#match從字串頭檢視此字串是否符合regular expression 
pattern = re.compile (r'\b[a-z]+[A-Z0-9]*\b')
if re.match(pattern, 'a123'):
    print('yes')

pattern = re.compile (r'\b[a-z]+[A-Z0-9]*\b')
res=pattern.search('a123 345 567')
print(res)  #印出<re.Match object; span=(0, 4), match='a123'>
print(res.group())#印出 a123

rs=r'^article/(?P<pk>[0-9])+/' 
if re.match(rs, "article/2/"):
    print("match!")
    match=re.search(rs, 'article/2/')
    print(match.group())
else: 
    print("no")
