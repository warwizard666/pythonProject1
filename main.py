import re

text = ("Что такое Регулярные выражения и как их использовать? "
        "Говоря простым языком, регуЛярное выражение — это последовательность символов, "
        "используемая для поиска "
        "и замены текста в строке или файле. Как уже было упомянуто, "
        "их поддерживает множество языков общего назначения: Python, Perl, R... "
        "Так что изучение регулярных выражений рано или поздно пригодится!!!")
pattern = r"регулярн\w+ выражен\w+"
print(re.findall(pattern, text, re.IGNORECASE))
#подсчет слов
#words_list = re.findall(r"\w+", text)
#print(words_list, len(words_list))
#подсчет предложений
#sent_list = re.split(r"[.?!]+\s*", text)
#sent_list.remove("")
#for sentense in sent_list:
       # print(sentense)
#print(len(sent_list))
#pattern = r"регулярн\w+ выражен\w+"
# result = re.search(pattern, text)
# result = re.findall(pattern, text)
# print(result)
# print(result.group(), result.start(),  result.end())
# result = re.match(pattern, text)
#start = 0
#result = ""
#while result is not None:
    #result = re.search(r"регулярн\w+ выражен\w+", text[start:])
    #if result is not None:
       # print(result.group(), result.start(),  result.end()-1)
        #start += result.end() + 1
