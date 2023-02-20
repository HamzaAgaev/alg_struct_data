from wikidocx import *
from searchstring import knuthMorrisPratt

if __name__ == "__main__":
    referat = getReferatText("Рентгеновское излучение.docx")
    # referat = notpunctuation(referat)

    wikipage = getWikipediaText("Рентгеновское излучение")
    # wikipage = notpunctuation(wikipage)

    referat_list = referat.split()
    referat_len = len(referat)
    plagiat_syms = 0

    for rl in range(len(referat_list) - 2):
        search_str = " ".join(referat_list[rl: rl + 3])
        count_found = knuthMorrisPratt(search_str, wikipage)
        plagiat_syms += len(search_str) * count_found

    plagiat = plagiat_syms / referat_len
    print(plagiat)