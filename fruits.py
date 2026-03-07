import pgzero 


fruits = {
    '1': 'apple',
    '2': 'banana',
    '3': 'orange',
    '4': 'grape',
    '5': 'mango'
}


fruit_counts = {
    'apple': 0,
    'banana': 0,
    'orange': 0,
    'grape': 0,
    'mango': 0
}

for i in range(5):
    print("\nChoose your favorite fruit:")
    for key, value in fruits.items():
        print(f"{key}: {value}")

    choice = input(f"User {i+1}, enter the number of your fruit: ").strip()


    if choice in fruits:
        fruit_name = fruits[choice]
        fruit_counts[fruit_name] += 1
    else:
        print(f"'{choice}' is not a valid key — that fruit does not exist.")

print("\nFruit counts:")
for fruit, count in fruit_counts.items():
    print(f"{fruit} : {count}")


check = input("\nEnter a fruit name to check its count: ").strip().lower()

if check in fruit_counts:
    print(f"{check} was chosen {fruit_counts[check]} times.")
else:
    print(f"'{check}' is not in the dictionary — the key is gone.")
