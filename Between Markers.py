def between_markers(text: str, begin: str, end: str) -> str:
   l=len(text)
   st=0
   if begin in text and end in text:
       st=text.index(begin,0,l)
       st=st+len(begin)
       end=text.index(end,0,l)
       return (text[st:end])
   elif begin not in text and end not in text:
       return text
   elif begin not in text:
       st=0
       last=text.index(end,0,l)
       return (text[st:last])
   elif end not in text:
       st=text.index(begin,0,l)
       st=st+len(begin)
       return (text[st:])
   else:
       return
if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')