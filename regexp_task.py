regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.


import re
# P = input()

# print (bool(re.match(regex_integer_in_range, P)) 
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

match_result = re.match(r"AV", 'AV Analitics Vidhia AV')
print (match_result.start())
print (match_result.end())
print (match_result.group(0))

search_result = re.search(r"Analitics", 'AV Analitics Vidhia AV')
print (search_result.start())
print (search_result.end())
print (search_result.group(0))

zip_reg = re.compile(r"^[1-9]\d{5}$")
find_result = zip_reg.match('100000')
print (find_result)

find_result = zip_reg.match('999999')
print (find_result)

find_result = zip_reg.match('012345')
print (find_result)

find_result = zip_reg.match('12345')
print (find_result)

find_result = zip_reg.match('666666')
print (find_result)

# zip_reg = re.compile(r"(\d)(?=\d\1)")
zip_reg = re.compile(r"(\d)(?=1)")
# zip_reg = re.compile(r"(1\d{1}1)(5\d{1}5)")
find_result = zip_reg.findall('0125251434')
print (len(find_result))
print (find_result)

rr = re.compile('(\d)1')
print(rr.findall('11233452167'))