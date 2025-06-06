def get_most_common_letter(text):
    counter = {}
    for char in text.replace(" ", ""):
        counter[char] = counter.get(char, 0) + 1
        print(f" counter is {counter}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(f"Letter is '{counter.items()}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
