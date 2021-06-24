shopping_lists = [
                ['LIDL','toast', 'tea','coffe'], #pos 0, LIDL
                ['ALDI','tomatos','cucumber', 'apple'], #pos 1 ALDI
                ['TESCO','bread', 'honey', 'almond', True], #pos 2 TESCO
                ["DUNNES",'ice cream', 'egg', 'croissant'], #pos 3 DUNNES
                [500] #pos 4 number only
                ]

for list_n in shopping_lists:
    print('SHOPE: ',list_n[0])
    for item in list_n[1:]:
        print("ITEM:", item)




