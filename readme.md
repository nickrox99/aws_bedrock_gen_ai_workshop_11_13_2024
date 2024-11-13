Welcome to the Anthropic's Claude 3 Workshop!
Unlock the Full Potential of Anthropic's Claude 3 with this Prompt Engineering Workshop Are you ready to take your AI-powered applications to the next level? Join our cutting-edge online workshop on Prompt Engineering with Anthropic's Claude v3 and learn how to harness the power of this state-of-the-art language model to create highly effective and tailored AI experiences.

In this comprehensive workshop, you'll gain the skills and knowledge needed to design, test, and refine prompts that optimize Claude's performance for your specific use case. This workshop will guide you through a structured, test-driven approach to prompt development, equipping you with the tools and techniques to achieve unparalleled results.

What You'll Learn
The fundamentals of prompt engineering and its importance in unlocking Claude's full potential
How to define clear tasks and success criteria to guide your prompt development process
Strategies for creating diverse test cases that cover a wide range of inputs and edge cases
Techniques for crafting effective initial prompts and iteratively refining them based on performance evaluations
Best practices for optimizing prompts for efficiency, latency, and cost
Advanced prompt engineering techniques, such as providing clear instructions, using examples, assigning roles, incorporating XML tags, Chaining Prompts, Function calling and more
Why Choose this Workshop?
This workshop was developed by experts with deep experience in prompt engineering and AI application development
Gain hands-on experience through practical exercises and real-world examples
Access a wealth of resources, including sample prompts, test cases, and evaluation rubrics
Join a community of like-minded professionals and expand your network
Whether you're a Solutions Architect, developer, data scientist, or a business professional looking to leverage the power of Anthropic's Claude v3 model, this workshop will provide you with the expertise and confidence to create highly effective prompts that drive superior performance and user experiences.

# 1
1 - Basic Prompt Structure

Lesson Objective:
The objective of this lesson is to introduce you to the basic structure of prompts for Anthropic's Claude model using the Messages API. You will learn about the required and optional parameters for making API calls, the importance of alternating user and assistant roles, and how to use system prompts to provide context and guidelines to Claude. By the end of the lesson, you should be able to create properly formatted prompts that elicit the desired responses from Claude.

API Parameters
To make a call to Claude using the Messages API, you need to provide the following required parameters:

model: the API model name of the model you intend to call
max_tokens: the maximum number of tokens to generate before stopping (Claude may stop earlier)
messages: an array of input messages, alternating between user and assistant roles
Optional parameters include:

system: the system prompt, which provides context, instructions, and guidelines to Claude
temperature: the degree of variability in Claude's response (set to 0 for these lessons)
User and Assistant Roles
When creating a prompt using the Messages API, it's crucial to format your input messages correctly. Each message must have a role (either user or assistant) and content. The messages must alternate between user and assistant roles, always starting with a user message.

User and Assistant Roles

Here's an example of a correctly formatted prompt:

Role	Content
User	Hi Claude, how are you?
Assistant	I'm doing well, thank you for asking! How can I assist you today?
User	Can you tell me the color of the ocean?
If the messages don't alternate between user and assistant roles or if the first message isn't a user message, the API will return an error.

System Prompts
In addition to the user and assistant messages, you can provide a system prompt using the system parameter. A system prompt is a way to give Claude context, instructions, and guidelines before presenting it with a question or task.

For example, you can use a system prompt to guide Claude's response style:
Role	        Content
System	        Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question.
User	        Why is the sky blue?

Assistant	
    - What causes the sky to appear blue to our eyes? 
    - How does the Earth's atmosphere interact with sunlight to create this effect? 
    - Are there any other factors that influence the perceived color of the sky? 
    - Does the sky always appear blue, or are there variations depending on the time of day or weather conditions?
A well-crafted system prompt can significantly improve Claude's performance by providing clear guidelines and context for the task at hand.

Lab 1 - Basic Prompt Structure
The accompanying Python notebook will provide hands-on practice in creating properly structured prompts for the Messages API. You will learn how to format input messages with alternating user and assistant roles, use system prompts to guide Claude's responses, and handle common errors related to prompt structure. The exercises will challenge you to create prompts that elicit specific responses from Claude, such as counting to three or mimicking the speech patterns of a young child. By completing these exercises, you will gain a solid foundation in crafting effective prompts for Claude using the Messages API.

# 2
2 - Being Clear and Direct

Lesson Objective:
In this lesson you will learn how to provide clear and direct instructions to Claude in order to achieve the best results. This lesson emphasizes the importance of giving Claude detailed context and specific requirements for completing a task, as if instructing a new employee. You'll will learn techniques such as:

Breaking down complex tasks into numbered steps
Being specific about desired outputs
Following the "Golden Rule of Clear Prompting".
How do I work with Claude?
When working with Claude, it's crucial to provide clear and direct instructions to ensure the best possible results. Just like when training a new employee, the more explicitly you explain what you want in a straightforward manner, the more accurate and relevant Claude's responses will be.

User and Assistant Roles

To make sure Claude understands your task, give as much context and detail as possible. Include any specific rules or requirements for completing the task correctly. For example, when asking Claude to remove personally identifiable information (PII) from a text, DON'T just say:

Role	Prompt
User	Please remove all personally identifiable information from this text: {{TEXT}}
Instead, provide a more detailed prompt that defines what constitutes PII, gives step-by-step instructions on how to process the text, and specifies the desired output format:

Role	Prompt
User	We want to anonymize some text by removing all personally identifiable information (PII).  Please follow these steps: 1. Replace all instances of names, phone numbers, and home and email addresses with 'XXX'. 2. If the text contains no PII, copy it word-for-word without replacing anything. 3. Output only the processed text, without any additional commentary.  Here is the text to process: {{TEXT}}
When dealing with complex tasks, consider breaking the instructions down into numbered steps or bullet points. This makes it easier for Claude to follow the instructions and ensures that all requirements are met. For instance, instead of simply asking Claude to turn a textbook chapter into a lesson plan:

Role	Prompt
User	Turn this textbook chapter into a lesson plan: {{CHAPTER}}
Provide a structured prompt that outlines the specific steps involved:

Role	Prompt
User	Your task is to turn the given textbook chapter into a comprehensive lesson plan. To do this task, you should: 1. Extract and summarize key concepts by section 2. Convert each extracted concept into a 30-minute lesson plan, including a list of questions to check comprehension. 3. Design an accompanying homework assignment that reinforces learnings from this chapter.  Here is the chapter:  {{CHAPTER}} 
If you want Claude to give a definitive answer or take a specific stance on a topic, make that clear in your prompt. Open-ended or vague instructions may lead to more general responses. For example, asking "Who is the best basketball player of all time?" might result in Claude listing several players without choosing a single one:

Role	Prompt
User	Who is the best basketball player of all time?
Assistant	There is no definitive answer to who is the best basketball player of all time. Reasonable basketball fans and analysts can disagree on this topic. Some of the players most frequently cited as possibilities for the GOAT (Greatest Of All Time) include Michael Jordan, LeBron James, Kareem Abdul-Jabbar, Wilt Chamberlain, Bill Russell, and Magic Johnson. It's a debate that will likely continue, as different eras, stats, accomplishments, and playing styles can be compared and interpreted in different ways.
However, if you ask Claude to pick just one player despite differing opinions, it will provide a more decisive answer:

Role	Prompt
User	Who is the best basketball player of all time? Yes, there are differing opinions, but if you absolutely had to pick one player, who would it be?
Assistant	There is no definitive answer to who is the best basketball player of all time, as reasonable people can disagree on this. However, if forced to choose just one player, I would say Michael Jordan is most commonly considered the GOAT (Greatest Of All Time) based on his exceptional talent, championships, awards, and cultural impact on the game of basketball. But others like LeBron James, Kareem Abdul-Jabbar, Wilt Chamberlain and Bill Russell are also frequently mentioned in the debate. It's a subjective call without a clear consensus.
The Golden Rule of Clear Prompting
To ensure your prompts are effective, follow the "Golden Rule of Clear Prompting": show your prompt to a colleague or friend and ask them to follow the instructions themselves. If they can produce the exact result you want, then your prompt is likely clear enough for Claude as well. Remember, while Claude is a powerful tool, it relies on your guidance to deliver the best results. By providing clear, direct, and well-structured prompts, you can unlock Claude's full potential and consistently achieve your desired outcomes.

Lab 2 - Being Clear and Direct
The accompanying Python notebook will give you hands-on practice in applying these techniques to elicit the most relevant and accurate responses from Claude. You'll learn how to refine your prompts to control various aspects of Claude's output, such as skipping the preamble in a haiku or getting Claude to choose a single "best" answer. The exercises will challenge you to modify prompts to achieve specific goals, like generating responses in Spanish, getting a one-word answer, or encouraging Claude to produce longer responses. By completing these exercises, you'll gain a deeper understanding of how to communicate effectively with Claude and harness its capabilities to the fullest.