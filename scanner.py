from googletrans import Translator
import pytesseract

PATH_TO_IMAGE = "ang.jpg"
PATH_TO_PYTESSERACT = "C:\\Program Files\\Tesseract-OCR\\tesseract"

pytesseract.pytesseract.tesseract_cmd = PATH_TO_PYTESSERACT
mess = []
mess = pytesseract.image_to_string(
    PATH_TO_IMAGE).strip("\n").split()

words_set = set([])
for i in mess:
    if (len(i) > 5):
        words_set.add(i.lower().replace(".", "").replace(",", "").replace(
            "(", "").replace(")", "").replace("?", "").replace("\"", "").replace(":", ""))

words = list(words_set)
print(words)

translator = Translator()

translated_word = []
for word in words:
    translated_word.append(translator.translate(word, dest="pl").text.lower())

print(translated_word)

with open("flashcards.txt", "a", encoding="utf-8") as file:
    for i in range(len(words)):
        file.write(words[i] + "," + translated_word[i] + "\n")
