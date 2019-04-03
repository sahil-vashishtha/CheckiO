def popular_words(text: str, words: list) -> dict:
    text=text.lower()
    text=text.split()
    dic={}
    a=0
    for i in range(0,len(words)):
        for j in range(0,len(text)):
            if words[i]==text[j]:
                a+=1
        dic[words[i]]=a
        a=0
    return dic


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")