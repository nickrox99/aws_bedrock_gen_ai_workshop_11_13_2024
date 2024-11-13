# Prompt - this is the only field you should change
PROMPT = "Who is the best basketball player of all time? Reply with one name and one name only with no punctuation"

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return text == "Michael Jordan"

# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))