# System prompt - this is the only field you should chnage
SYSTEM_PROMPT = "Please take in English prompts and reply with Spanish."

# Prompt
PROMPT = "Hello Claude, how are you?"

# Get Claude's response
response = get_completion(PROMPT, SYSTEM_PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return "hola" in text.lower()

# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))