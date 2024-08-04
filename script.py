from translate import Translator

translator = Translator (to_lang = "zh")

try:
 with open ('test.txt',mode='r') as my_file:
            text = (my_file.read())
            translation = translator.translate(text)
            with open('test-lang.txt',mode="w") as my_new_file:
                my_new_file.write(transaltion)

except FileNotFoundError as e:
    print('check your file path')
