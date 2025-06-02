def smash(words):
    output = ""
    for word in words:
        output = output + " " + word
    return output.strip()
    

input = ['hello', 'world', 'this', 'is', 'great'] 
result = smash(input)
print(result)


'''
def smash(words):
    return ' '.join(words).strip()
'''