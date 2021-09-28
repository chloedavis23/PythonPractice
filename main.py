def define(word): 
    word.lower()
    
    if word == "Osowski": 
        return "This word does not exist in this dictionary"
        
    elif word == "Skunk":
        return "Stinky creature that farts"

    elif word == "Computer": 
        return "This word does not exist in this dictionary"

    elif word == "Cloud": 
        return "Floating water in the sky"

    elif word == "Fun": 
        return "This word does not exist in this dictionary"

    elif word == "ARMY": 
        return "BTS fanbase"

    elif word == "Music": 
        return "Good stuff" 

    elif word == "Student": 
        return "Educated person in school"

    elif word == "Deez": 
        return "nutz" 
        
    else: 
        return "That word is not in this dictionary YET."

print(define("Deez"))