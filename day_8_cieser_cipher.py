def encoding (code,shift,encode_or_decode):
    encoded =''
    text=''
    shift_amount=shift
    if encode_or_decode=='decode':
            shift_amount *= -1
    for letter in code:
        #print(encode_or_decode)
        ltr_indx = alphabets.index(letter)       
        shifted_position = ltr_indx+shift_amount
        shifted_position%=len(alphabets)       
        text +=alphabets[shifted_position]
        #print(encode_or_decode)
        
    print(text)
    return text
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#deep
another_text='yes'
while another_text:
    if another_text=='yes':
        code = input('enter your message to encrypt or decrypt : ')
        shift =int(input("enter shift number : "))
        encode_or_decode = input('do you want to encode or decode : ')
        op= encoding(code,shift,encode_or_decode)
        print(f'Here is the {encode_or_decode}d output : {op}')
        another_text =(input("another text.yes or no .? :")).lower()
    else:
        break


