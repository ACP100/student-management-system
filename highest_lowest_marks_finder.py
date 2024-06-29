import json

def Highest_lowest_marks(name):
    with open("data/student.json", 'r') as f:
        data = json.load(f)
    
       
    # Initialize highest and lowest marks and corresponding student names for each subject
    h_maths = 0
    h_maths_name = 'j'
    l_maths = 101
    l_maths_name = 'j'
    math_marks=0

    h_science = 0
    h_science_name = 'j'
    l_science = 101
    l_science_name = 'j'
    science_marks =0

    h_social = 0
    h_social_name = 'j'
    l_social = 101
    l_social_name = 'j'
    social_marks =0

    h_english = 0
    h_english_name = 'j'
    l_english = 101
    l_english_name = 'j'
    english_marks =0

    for i in data:
        # Check for highest and lowest marks in maths
        if i['subject']['maths'] > h_maths:
            h_maths = i['subject']['maths']
            h_maths_name = i['name']
        elif i['subject']['maths'] < l_maths:
            l_maths = i['subject']['maths']
            l_maths_name = i['name']

        # Check for highest and lowest marks in science
        if i['subject']['science'] > h_science:
            h_science = i['subject']['science']
            h_science_name = i['name']
        elif i['subject']['science'] < l_science:
            l_science = i['subject']['science']
            l_science_name = i['name']

        # Check for highest and lowest marks in social
        if i['subject']['social'] > h_social:
            h_social = i['subject']['social']
            h_social_name = i['name']
        elif i['subject']['social'] < l_social:
            l_social = i['subject']['social']
            l_social_name = i['name']

        # Check for highest and lowest marks in english
        if i['subject']['english'] > h_english:
            h_english = i['subject']['english']
            h_english_name = i['name']
        elif i['subject']['english'] < l_english:
            l_english = i['subject']['english']
            l_english_name = i['name']

        if i['name'] == name:
            math_marks = i['subject']['maths']
            science_marks = i['subject']['science']
            social_marks = i['subject']['social']
            english_marks = i['subject']['english']

    # Print the results
    print(f"Highest mark in maths is {h_maths}, obtained by {h_maths_name}\n")
    print(f"Lowest mark in maths is {l_maths}, obtained by {l_maths_name}\n")
    print(f"You have obtained {math_marks} marks\n")

    print(f"Highest mark in science is {h_science}, obtained by {h_science_name}\n")
    print(f"Lowest mark in science is {l_science}, obtained by {l_science_name}\n")
    print(f"You have obtained {science_marks} marks\n")

    print(f"Highest mark in social is {h_social}, obtained by {h_social_name}\n")
    print(f"Lowest mark in social is {l_social}, obtained by {l_social_name}\n")
    print(f"You have obtained {social_marks} marks\n")

    print(f"Highest mark in english is {h_english}, obtained by {h_english_name}\n")
    print(f"Lowest mark in english is {l_english}, obtained by {l_english_name}\n")
    print(f"You have obtained {english_marks} marks\n")



