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

*The Golden Rule of Clear Prompting*
**To ensure your prompts are effective, follow the "Golden Rule of Clear Prompting": show your prompt to a colleague or friend and ask them to follow the instructions themselves. If they can produce the exact result you want, then your prompt is likely clear enough for Claude as well. Remember, while Claude is a powerful tool, it relies on your guidance to deliver the best results. By providing clear, direct, and well-structured prompts, you can unlock Claude's full potential and consistently achieve your desired outcomes.**

Lab 2 - Being Clear and Direct
The accompanying Python notebook will give you hands-on practice in applying these techniques to elicit the most relevant and accurate responses from Claude. You'll learn how to refine your prompts to control various aspects of Claude's output, such as skipping the preamble in a haiku or getting Claude to choose a single "best" answer. The exercises will challenge you to modify prompts to achieve specific goals, like generating responses in Spanish, getting a one-word answer, or encouraging Claude to produce longer responses. By completing these exercises, you'll gain a deeper understanding of how to communicate effectively with Claude and harness its capabilities to the fullest.

# 3
3 - Assigning Roles - Role Prompting

Lesson Objective:
In this lesson you will learn how to use role prompting to enhance Claude's performance and tailor its responses to specific contexts. You will learn how assigning a role to Claude can improve its accuracy and understanding of the task at hand, as well as influence its tone, demeanor, and communication style to better suit the desired output. The lesson will cover when to use role prompting and provide examples demonstrating its effectiveness in various scenarios.

Claude is a highly capable AI assistant, but sometimes it benefits from having additional context to understand the role it should play in a given conversation. By assigning a role to Claude, you can prime it to respond in a specific way, improve its accuracy and performance, and tailor its tone and demeanor to match the desired context. This technique is known as role prompting.

Role Prompting

Role prompting can enhance Claude's performance in two main ways:

Improved accuracy and performance: In certain complex situations, such as solving math problems or writing code, assigning a relevant role to Claude can significantly improve its performance and understanding of the task at hand.
Tailored tone and style: By specifying a role, you can influence Claude's tone, demeanor, and communication style to better suit your needs. For example, asking Claude to act as a kindergarten teacher will result in a very different response compared to asking it to be a graduate professor.
Consider the following example where Claude is asked to provide a one-sentence perspective on skateboarding:

Role	Prompt
User	In one sentence, what do you think about skateboarding?
Assistant	Skateboarding is an exciting and creative sport that combines athleticism, skill, and self-expression.
Now, let's see how Claude's response changes when we prime it to inhabit the role of a cat:

Role	Prompt
System	You are a cat.
User	In one sentence, what do you think about skateboarding?
Assistant	As a cat, I find skateboarding to be a noisy and confusing activity that often disturbs my naps and makes me question the sensibility of humans.
As you can see, by assigning the role of a cat to Claude, its perspective, tone, and content adapt to match the new context.

Role prompting can also improve Claude's performance in tasks involving logic or mathematics. For example, consider the following logic puzzle:

Role	Prompt
User	Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?
Assistant	It's not possible to determine with certainty based on the given information. We know that Jack is married and George is not, but Anne's marital status is unknown. If Anne is unmarried, then yes, a married person (Jack) is looking at an unmarried person (Anne). However, if Anne is married, then no, a married person is not looking at an unmarried person. Without knowing Anne's marital status, we cannot definitively answer the question.
While Claude's response is reasonable, it doesn't provide a definitive answer. Now, let's see how priming Claude with the role of a logic bot changes its response:

Role	Prompt
System	You are a logic bot designed to answer complex logic problems.
User	Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?
Assistant	Yes, a married person is looking at an unmarried person. We know that Jack is married and George is not married. Therefore, when Jack looks at Anne, he is a married person looking at a person whose marital status is unknown. Regardless of Anne's marital status, Jack, who is married, is looking at either an unmarried person (if Anne is unmarried) or a person who is looking at an unmarried person (if Anne is married and looking at George). So, at least one married person (Jack) is looking at an unmarried person (Anne) or a person looking at an unmarried person (George), regardless of Anne's marital status.
By assigning the role of a logic bot, Claude provides a more definitive and accurate answer to the logic puzzle.

To get the most out of role prompting, keep these tips in mind:

Be specific: Provide clear and detailed context about the role you want Claude to play. The more information you give, the better Claude can understand and embody the desired role.
Experiment and iterate: Try different roles and variations of your prompts to find the best approach for your specific use case. Prompt engineering often involves experimentation and iteration to achieve optimal results.
Lab 3 - Assigning Roles - Role Prompting
The accompanying Python notebook will provide hands-on practice in applying role prompting to various scenarios, such as improving Claude's performance in math problems and tailoring its communication style for different audiences. By completing the exercises, students will gain a deeper understanding of how to effectively use role prompting to unlock Claude's full potential and achieve desired outcomes.

# 4
4 - Separating Data and Instructions

Lesson Objective:
The objective of this lesson is to teach you how to use XML tags to structure prompts and guide Claude's responses. You will learn how wrapping key parts of their prompts (such as instructions, examples, or input data) in XML tags can help Claude better understand the context and generate more accurate outputs. The lesson will cover what XML tags are, why they are useful, and how to effectively incorporate them into prompts, particularly when working with complex prompts or variable inputs.

What are XML tags?
 Use XML Tags

XML tags are angle-bracket tags like <tag></tag>. They come in pairs and consist of an opening tag, such as <tag>, and a closing tag marked by a /, such as </tag>. XML tags are used to wrap around content, like this: <tag>content</tag>.

Opening and closing XML tags should share exactly the same name. The tag name can be anything you like, as long as it's wrapped in angle brackets, although we recommend naming your tags something contextually relevant to the content it's wrapped around.

XML tags should always be referred to in pairs and never as just the first half of a set (e.g., "Using the document in <doc></doc> tags, answer this question.").

📌 XML tag names

There is no canonical best set of XML tag names that Claude performs particularly well with. For example, <doc> works just as well as <document>. The only time you need very specific XML tag names is in the case of function calling.
Why use XML tags?
There are several reasons why you might want to incorporate XML tags into your prompts:

Improved accuracy: XML tags help Claude distinguish between different parts of your prompt, such as instructions, examples, and input data. This can lead to more precise parsing of your prompt and thus more relevant and accurate responses, particularly in domains like mathematics or code generation.
Clearer structure: Just as headings and sections make documents easier for humans to follow, XML tags help Claude understand the hierarchy and relationships within your prompt.
Easier post-processing: You can also ask Claude to use XML tags in its responses, making it simpler to extract key information programmatically.
How to use XML tags
You can use XML tags to structure and delineate parts of your prompt from one another, such as separating instructions from content, or examples from instructions.

Role	Content
User	Please analyze this document and write a detailed summary memo according to the instructions below, following the format given in the example:  <document> {{DOCUMENT}} </document>  <instructions> {{DETAILED_INSTRUCTIONS}} </instructions>  <example> {{EXAMPLE}} </example>
Please analyze this document and write a detailed summary memo according to the instructions below, following the format given in the example:

Handling variable inputs
When working with prompt templates that include variable inputs, use XML tags to indicate where the variable content should be inserted, such as in the following example:

Role	Content
User	I will tell you the name of an animal. Please respond with the noise that animal makes. <animal>{{ANIMAL}}</animal>
As a general rule, you should always separate your variable inputs from the rest of your prompt using XML tags. This makes it clear to Claude where the examples or data begin and end, leading to more accurate responses.

Requesting structured output
You can ask Claude to use XML tags in its responses to make the output easier to parse and process:

Role	Content
User	Please extract the key details from the following email and return them in XML tags:  - Sender name in <sender></sender> tags - Main topic in <topic></topic> tags - Any deadlines or dates mentioned in <deadline></deadline> tags  <email> From: John Smith To: Jane Doe Subject: Project X Update  Hi Jane,  I wanted to give you a quick update on Project X. We've made good progress this week and are on track to meet the initial milestones. However, we may need some additional resources to complete the final phase by the August 15th deadline.  Can we schedule a meeting next week to discuss the budget and timeline in more detail?  Thanks, John </email>
Claude's response:

Role	Response
Assistant	<sender>John Smith</sender> <topic>Project X Update</topic> <deadline>August 15th</deadline>
XML tags make it easier to retrieve targeted details from Claude's response by allowing for programmatic extraction of content between specific tags.

When calling Claude via the API, you can pass closing XML tags (e.g., </json>) to the stop_sequences parameter to have Claude stop generating once it reaches the desired endpoint. This can save both money and time by eliminating any concluding remarks after the core response. The same is true of skipping Claude's friendly preamble by prefilling Claude's response with an opening XML tag.

XML best practices
To get the most out of XML tags, keep these tips in mind:

Use descriptive tag names that reflect the content they contain (e.g., <instructions>, <example>, <input>).
Be consistent with your tag names throughout your prompts.
Always include both the opening (<tag>) and closing (</tag>) tags, including when you reference them, such as "Using the document in <doc></doc> tags, answer this question."
You can and should nest XML tags, although more than five layers of nesting may decrease performance depending on the complexity of the use case.
Lab 4 - Separating Data from Instructions
The accompanying Python notebook will provide hands-on practice in applying XML tags to structure prompts and guide Claude's responses. You will learn how to effectively use XML tags to separate instructions from input data, handle variable inputs, and request structured output. The exercises will challenge you to incorporate XML tags into various prompts to improve Claude's accuracy and understanding of the task at hand. By completing these exercises, you will gain a deeper understanding of how to leverage the power of XML tags to unlock Claude's full potential and achieve more precise and accurate outputs, especially when working with complex prompts or variable inputs.