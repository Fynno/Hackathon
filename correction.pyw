from spellchecker import SpellChecker


def CorrectionFun(words):
    spell = SpellChecker(language='de')

    unknownWords = spell.unknown(words)
    data = " ".join(words)
    for x in unknownWords:
        try:
            data.replace(x,spell.correction(x))
            print("Wrong word:")
            print(x)
        except ValueError:
            pass
    words = data.split()
    return words