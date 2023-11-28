import prettytable
from prettytable import PrettyTable

# יצירת אובייקט של PrettyTable
pokemon = PrettyTable()

# הגדרת שמות עמודות
pokemon.field_names = ["Name", "Type"]

# הוספת שורות
pokemon.add_row(["Pikachu", "Electric"])
pokemon.add_row(["Squirtle", "Water"])
pokemon.add_row(["Charmander", "Fire"])

# הדפסת הטבלה
print(pokemon)
