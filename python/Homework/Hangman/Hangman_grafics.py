logo = '''
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a 
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88 
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
'''

hangman_1 = """ 
____
|/   |
|   
|    
|    
|    
|
|_____
""";
hangman_2 = """
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""";
hangman_3 = """
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""";
hangman_4 = """
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""";
hangman_5 = """
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""";
hangman_6 = """
 ____
|/   |
|   (_)
|   \|/
|    |
|  ./ 
|
|_____
""";
hangman_7 = """
 ____
|/   |
|   (_)
|   \|/
|    |
|  ./ \.
|
|_____
""";
game_over = """
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
"""
you_won = """

┌──────────────────────────────────────────────────────────────────────────┐
│                                                                       __ │
│                                                                      |  \│
│ __    __   ______   __    __        __   __   __   ______   _______  | $$│
│|  \  |  \ /      \ |  \  |  \      |  \ |  \ |  \ /      \ |       \ | $$│
│| $$  | $$|  $$$$$$\| $$  | $$      | $$ | $$ | $$|  $$$$$$\| $$$$$$$\| $$│
│| $$  | $$| $$  | $$| $$  | $$      | $$ | $$ | $$| $$  | $$| $$  | $$ \$$│
│| $$__/ $$| $$__/ $$| $$__/ $$      | $$_/ $$_/ $$| $$__/ $$| $$  | $$ __ │
│ \$$    $$ \$$    $$ \$$    $$       \$$   $$   $$ \$$    $$| $$  | $$|  \│
│ _\$$$$$$$  \$$$$$$   \$$$$$$         \$$$$$\$$$$   \$$$$$$  \$$   \$$ \$$│
│|  \__| $$                                                                │
│ \$$    $$                                                                │
│  \$$$$$$                                                                 │
└──────────────────────────────────────────────────────────────────────────┘                           
"""