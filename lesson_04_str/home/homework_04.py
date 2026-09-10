adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_words = adwentures_of_tom_sawer.count('h')
print("Літера 'h' в тексті зустрічається", count_words, "разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
count_words = 0
for r in adwentures_of_tom_sawer: 
    if r.istitle():
       count_words += 1
else: pass
print ("Кількість слів у тексті, які починаються з великої літери дорівнює:",count_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
import re
find_all_words = list(re.finditer("Tom", adwentures_of_tom_sawer))
if len(find_all_words) > 0:
    position_second_elements = find_all_words[1].start()
    print ("Індекс другої позиції розташування слова Tom є:", position_second_elements)
else: pass

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print (adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print (adwentures_of_tom_sawer_sentences)
number_of_sentence = adwentures_of_tom_sawer_sentences[3]
letter_lower = number_of_sentence.lower()
print(letter_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = [sentences_text.strip("\n")
                                     for sentences_text in adwentures_of_tom_sawer_sentences]
for start_sentences in adwentures_of_tom_sawer_sentences:
    if start_sentences.startswith('By the time'):
        print("Так, є речення які починаються з By the time")
    else: pass 

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print (adwentures_of_tom_sawer_sentences)
choice_sentence = adwentures_of_tom_sawer_sentences[-2]
choice_sentence = choice_sentence.split()
count_words_choice_sentence = len(choice_sentence)
print("Кількість слів останнього речення:", count_words_choice_sentence)
