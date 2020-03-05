def is_pangram(sentence):
    for i in range(65, 91):
        if chr(i) not in sentence.upper():
            return False
    else:
        return True    
        
