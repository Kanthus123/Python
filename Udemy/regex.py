import re #RegEx library

string = "'I AM NOT YELLING', she said"
new = re.sub('ABC', '', string)
# 1 = checa se tem o que queremos remover,
#2 - Troca o que der true por algo definido , 
#3 - variavel a ser manipulada
