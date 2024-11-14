# Variable content
ANIMAL = "<subject>CAT</subject>"

# number of haikus
NUMBER = "<count>2</count>"

# Prefill for Claude's response
PREFILL = "<haiku>"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write {NUMBER} haiku(s) about {ANIMAL}. Put each haiku(s) in {PREFILL} tags."

# Get Claude's response
response = get_completion(PROMPT, prefill=PREFILL)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(
        (re.search("cat", text.lower()) and re.search("<haiku>", text))
        and (text.count("\n") + 1) > 5
    )

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