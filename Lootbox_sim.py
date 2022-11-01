#By: Shannon bennett
import random

#Pick random items for the loot box
def open_box(num_items):
    items_list = []
    
    for i in range(num_items):
         num = random.randint(1, 100)

         if num <=5:
            rarity = 'Legendary'
                       
         elif num <=15:       
            rarity = 'Epic'
                   
         elif num <=50:
            rarity = 'Rare'
           
         elif num <=100:
            rarity = 'Common'
            
         items_list.append(rarity)           
         print('  item ', i+1, 'of', str(num_items) + '...', rarity, 'item!')   

    items.extend(items_list)


#------Main code
gems = 0
boxes = 0
boxes_opened = 0
total_spent = 0
items = []

num_items = 4


print('Welcome to loot Box Simulator! \n')

while True:
    print('You have ⟡', gems, 'and ❒', boxes)
    print('Choose from the following options: ')
    print('  1) Buy gems (550 gems for just $19.95!)')
    print('  2) Buy loot box (costs 100 gems)')
    print('  3) Open loot box')
    print('  4) View statistics')
    print('  5) Quit')

    command = input('> ')
   
    if command == '1':
        gems = gems + 550
        total_spent = total_spent + 19.95
        print('Thank you for your purchase! \n ')

    elif command == '2':
        if gems >= 100:
            gems = gems - 100
            boxes = boxes + 1
            print('loot box purchased \n ')       
        else:
            print('insufficient gems \n ' )

    elif command == '3':
        if boxes == 0:
            print('insufficient loot boxes \n ')

        else:
             print('Opening loot box:')
             boxes = boxes - 1
             boxes_opened = boxes_opened + 1
             
             open_box(num_items)
             print('\n ')
             
    elif command == '4':
        
        print('Total spent: $' + str(round(total_spent,3)))
        print('Loot boxes opened:', boxes_opened)

        if boxes_opened > 0:
            legendary_count = items.count('Legendary')
            total_items = len(items)
            print('Legendary items: ', legendary_count, ' (' + str(round((legendary_count/total_items)*100,2)) + '%' ') \n ')
        
    elif command == '5':         
         print('Goodbye!')
         break

    
    else:
        print('Invalid choice \n ')   
