# Prompt template with a placeholder for the variable content
PROMPT = f"Who is the best basketball player of all time? Please choose one specific player."

# Prefill for Claude's response
PREFILL = "Stephen Curry, who plays for"

# Get Claude's response
response = get_completion(PROMPT, prefill=PREFILL)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("Warrior", text))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))