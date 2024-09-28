def single_root_words(root_word, *other_words,):
    same_words = []                       #создаем пустой список
    root_word_lower = root_word.lower()   #переводим все символы первого параметра в нижний регистр
    for i in other_words:                 #создаем цикл для перебора символов в параметре other_words
        other_words_lower = i.lower()     #переводим все символы второго параметра в нижний регистр
        if root_word_lower in other_words_lower or other_words_lower in root_word_lower: #проверям совпавшие элементы
            same_words.append(i)          #добавляем в список совпавшие элементы параметров

    return same_words                     # возвращаем список который образовала функция

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)