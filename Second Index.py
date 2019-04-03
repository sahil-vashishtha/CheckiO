def second_index(text: str, symbol: str) -> [int, None]:
    t=0
    a=0
    if text.count(symbol)<2:
        return None
    else:
        for i in range(0,len(text)):
            if text[i]==symbol and a<2:
                t=i
                a+=1
        return t
    
    


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')