from spellchecker import SpellChecker


def CorrectionFun(words):
    spell = SpellChecker(language='de')

    unknownWords = spell.unknown(words)

    for x in unknownWords:
        try:
            words.remove(x)

        except ValueError:
            pass

    for element in unknownWords:

        words.append(spell.correction(element))
    return words