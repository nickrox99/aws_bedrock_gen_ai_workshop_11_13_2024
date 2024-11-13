# Variable content
TOPIC = "Pigs"

# Prompt template with a placeholder for the variable content
PROMPT = f"Create a haiku about {TOPIC}"

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("pigs", text.lower()) and re.search("haiku", text.lower()))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))