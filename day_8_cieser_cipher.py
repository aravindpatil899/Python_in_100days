def encoding (code,shift):
    encoded =''
    text=''
    for letter in code:
        ltr_indx = alphabets.index(letter)
        if ltr_indx+shift>=len(alphabets):
            encoding = alphabets[(ltr_indx+shift)-26]
        else:
            encoding = alphabets[ltr_indx+shift]
        text+=encoding
    return text
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#deep
another_text='yes'
while another_text:
    if another_text=='yes':
        code = input('enter your message to encrypt : ')
        shift =int(input("enter shift number : "))
        op= encoding(code,shift)
        print(op)
        another_text =(input("another text.yes or no .? :")).lower()
    else:
        break


