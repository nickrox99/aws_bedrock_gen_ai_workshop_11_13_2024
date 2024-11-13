# Prompt - this is the only field you should change
PROMPT = "Please write an 800 word story."

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    trimmed = text.strip()
    words = len(trimmed.split())
    return words >= 800

# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))