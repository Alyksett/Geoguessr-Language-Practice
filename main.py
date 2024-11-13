from langs import languages, Language
import random
from tabulate import tabulate

def get_random_langage() -> Language:
    l = len(languages)
    rand = random.randint(0, l-1)
    return languages[rand]

def subselect_passage(lang: Language):
    text = lang.text
    words = text.split(" ")
    number_words = 50
    start = random.randint(0, len(words)-number_words-1)
    d = words[start: start+number_words]
    return " ".join(d)

def get_input(target:str):
    guesses = 0
    hints = 1
    guess = ""

    while True:
        guess = input("What language is this: ")
        match guess.lower():
            case "help":
                print("===========")
                print("\n".join([l.language for l in languages]))
                print("===========")
                continue
            case "hint":
                print(" " * 10 + f"Hint: {target[0:hints]}")
                hints += 1
                continue
            case "idk":
                guesses = -1
                print(target)
                break
            case _ if guess.lower() != target.lower():
                guesses += 1
                print(" " * 10 + "Incorrect")
            case _ if guess.lower() == target.lower():
                print(" " * 10 + "Correct")
                break
    return guesses, hints-1

def try_window(languages: list[Language]) ->list[Language]:
    res = []
    long_res = []
    for l in languages:
        print("-"*60)
        passage = subselect_passage(l)
        p = "\n".join([l.text[i:i+60] for i in range(0, len(passage), 60)])
        print(p)
        print("-"*60)
        guesses, hints = get_input(target=l.language.lower())
        if guesses > 0 or hints > 0:
            res.append(l)
        if guesses > 3:
            long_res.append(l)
    return res

def main():
    langs: list[Language] = languages
    random.shuffle(languages)
    scores = {l.language: 0 for l in langs}
    
    n = len(langs)
    k = 4
    low = 0
    long_retries = []
    for i in range(n-k+1):
        subset = langs[low:i+k]
        retries = try_window(subset)
        while(retries):
            for r in retries:
                scores[r.language] += 1
            random.shuffle(retries)
            retries = try_window(retries)
        low = i+k
    folded = [[language, score] for language, score in scores.items()]
    folded = sorted(folded, key=lambda s:s[1], reverse=True)
    print(tabulate(folded, headers=["Language", "Score"], colalign=["left"]))
    print("\"Score\" is the number of attempts.")

main()


