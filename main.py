from langs import languages, Language
import random

def get_random_langage() -> Language:
    l = len(languages)
    rand = random.randint(0, l-1)
    return languages[rand]

def subselect_passage(lang: Language):
    # text = lang.text
    # words = text.split(" ")
    # length =  len(words)
    # min_length = length//3
    # max_length = length//2
    # start = random.randint(0, length-max_length)
    # end = random.randint(min_length, max_length)
    # d = words[start:end + start]
    # return " ".join(d)
    return lang.text

def get_input(target:str, text:str):
    guesses = 0
    hints = 1
    guess = ""
    
    while(guess.lower() != target):
        guess = input("What language is this: ")    
        
        if(guess == "hint"):
            print(" " * 10 + f"Hint: {target[0:hints]}")
            hints += 1
            hints+=1
            continue
        if(guess.lower() != target and guess != "idk"):
            guesses += 1
            print(" " * 10 + "Incorrect")
        if(guess == "idk"):
            guesses = -1
            print(target)
            break
        if(guess.lower() == target):
            print(" " * 10 + "Correct")
            break
    return guesses, hints-1 

def try_window(languages: list[Language]) ->list[Language]:
    res = []
    long_res = []
    for l in languages:
        print("-"*60)
        p = "\n".join([l.text[i:i+60] for i in range(0, len(l.text), 60)])
        print(p)
        print("-"*60)
        guesses, hints = get_input(target=l.language.lower(), text=l.text)
        if guesses > 0 or hints > 1:
            res.append(l)
        if guesses > 3:
            long_res.append(l)
    return res

def main():
    langs: list[Language] = languages
    random.shuffle(languages)
    scores = {(langs[i].language for i in langs) : 0}
    n = len(langs)
    k = 2
    low = 0
    long_retries = []
    for i in range(n-k+1):
        subset = langs[low:i+k]
        retries = try_window(subset)
        for r in retries:
            scores[r.language] += 1
        while(retries):
            for r in retries:
                scores[r.language] += 1
            random.shuffle(retries)
            retries = try_window(retries)
        low = i+k
    
main()


