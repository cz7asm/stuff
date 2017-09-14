import random

_vowels = ['a', 'e', 'i', 'o', 'u']
_syl = ['la', 'ba', 'do', 'ki', 'li', 'ma']
defaults = _vowels + _syl

def makeName(syls=defaults):
    """
    Generates a name-like looking string from given list
    of syllables/characters
    """
    return ''.join(random.sample(syls, random.randint(3,6))).title()

def makePairs(inlist):
    """
    Creates a list of paired items from input list.
    In case of odd number of items it's paired with None
    """
    wset = set(inlist)
    pairs = []
    for _ in range(len(wset)/2):
        pair = random.sample(wset, 2)
        for x in pair: wset.remove(x)        
        pairs.append(pair)
    if wset:
        pairs.append((wset.pop(), None))
    return pairs

