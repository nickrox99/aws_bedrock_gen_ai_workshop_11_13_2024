# First input variable
ANIMAL1 = "Cat"

# Second input variable
ANIMAL2 = "Dog"

# number of haikus
NUMBER = "two"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write {NUMBER} haikus for each {ANIMAL1} and {ANIMAL2}. Put it in <haiku> tags."

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("tail", text.lower()) and re.search("cat", text.lower()) and re.search("<haiku>", text))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))