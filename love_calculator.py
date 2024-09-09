def calculate_love_score(name1,name2):
    true ='TRUE'
    love = 'LOVE'
    total=0
    for letter in true:
        ltr_count =0
        #if letter in (name1+name2):
        for char in (name1+name2):
            if letter == char:
                ltr_count+=1
                total+=1
        print(f'{letter} occures {ltr_count} times')
    print(f'total ={total}')
    total2=0
    for letter in love:
        ltr_count =0
        #if letter in (name1+name2):
        for char in (name1+name2):
            if letter == char:
                ltr_count+=1
                total2+=1
        print(f'{letter} occures {ltr_count} times')
    print(f'total ={total2}')
    print(str(total)+str(total2))
calculate_love_score('Angela Yu'.upper(),'Jack Bauer'.upper())