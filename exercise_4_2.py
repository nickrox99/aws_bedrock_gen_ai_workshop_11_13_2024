# Variable content
QUESTION = "ar cn brown?"

# Prompt template with a placeholder for the variable content
PROMPT = f"Hia its me i have a q about dogs jkaerjv <question>{QUESTION}</question> jklmvca tx it help me muhch much atx fst fst answer short short tx"

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("brown", text.lower()))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))