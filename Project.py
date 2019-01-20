from sys import exit

# Read data
import pandas as pd
data = pd.read_csv("wii_games.csv", delimiter = ';')
dic = data.set_index('Name').transpose().to_dict(orient='dict')

for k1, v1 in dic.items():
    for k2, v2 in v1.items():
        dic[k1][k2] = str(v2).replace(",", ".")

# Counts, description
def line_counts(col = 'Genre'):
    cnts = {}
    for v in dic.values():
        cnts[v[col]] = cnts.get(v[col], 0) + 1
    return cnts

def word_counts():
    w_cnts = {}
    all_names = " ".join(dic).split()
    for word in all_names:
        w_cnts[word] = w_cnts.get(word, 0) + 1
    return w_cnts
       
def print_counts_top(lc_or_wc, top=20):
    skip = ['The','–','2','&','the','of']
    items = sorted(lc_or_wc.items(), key=get_count, reverse=True)
    #print('From: ',sum(items[0]))
    
    for item in items[0:top]:
        if item[0] not in skip:
            print(item[0], item[1])

def get_count(count_tuple): #a function for custom sort in sorted 
    return count_tuple[1]
            
# Multiple criteria search    
def games_search(age, nh):
    lst = []
    for k1, v1 in dic.items():
        for k2, v2 in v1.items():
            if (dic[k1]["Age"]).lower() == age and dic[k1]["Not_hard"] == nh: #and dic[k1]["Multiplayer"] = multi
                lst.append(k1)
    print(set(lst))
            
# def print_search():    
    
def flow():
    print("Your are using the best", color.RED + 'Nintendo Wii' + color.END, "games selector.")
    print("\n"+"To see a summary information for games enter", color.BOLD + 's' + color.END)
    print("To get game recommendations enter",  color.BOLD + 'r' + color.END)
    print("For exit enter", color.RED + 'q' + color.END)
    
    choice = None
    
    while choice != 'q':
        choice = input("> ")
        
        if choice == 's':
            print("\n",'Game genre counts: ')    
            print_counts_top(line_counts())
            print("\n",'Game name words counts: ')
            print_counts_top(word_counts(), top=15)
            
        elif choice == 'r':
            print("\n",'Please select apropriate age: e6, e10, t13 or t17: ')
            age = input("> ")
            print("\n", "Enter 'ok' if you prefer easy games (better for small kids and beginners:)")
            nh = input("> ")
            games_search(age, nh)
            
        elif choice == 'q':
            exit(0)
            
        else:
            print("\n" + 'Our options are limited. Good loves you! Just pray every day and select an option q, s or r please.')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'        
                      
flow()    
