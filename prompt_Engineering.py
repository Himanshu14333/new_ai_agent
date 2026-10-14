#prompt engineering

#6 step process to create a good prompt
#role
#task
#constraints
#output format
#zero/one short
#fallback

1.Role:
What is the role of the model?
domain and responsibility

example:
you are senior software engineer.

2.Task:
 kya karna hai?
 classification of issue , summarize the text, translation, code generation, etc.

 example:
 classify the text into positive or negative.

3.Constraints:
Bounded 
 what are the constraints?
 time, cost, accuracy, etc.

 example:
 time is limited to 1 minute.

4.Output format:
define the output format in json, text, html, etc.

5.Zero/One shot:
given an example of the output format, the model will generate the output.


6.Fallback:
if there is uncertanty, provide a fallback plan.



------------------------------------------------------------------

#ReAct

What is the ReAct pattern?
The ReAct (Reasoning + Acting) pattern is a framework that enables AI models to solve complex tasks by combining internal reasoning with external actions using tools (0:09). Instead of relying solely on pre-trained knowledge, which is limited by static training data, ReAct allows an agent to break down a prompt, decide which tool is needed, execute that tool, and incorporate the observation into its next step (1:42 - 19:47).

Core Loop Mechanism:

Thought: The model analyzes the current state and decides on a sub-task (26:16).
Action: The agent selects and calls a specific tool (e.g., a calculator or API) to perform an action (26:35).
Observation: The system feeds the result of that tool back into the model as new information (25:25).
Looping: This cycle continues iteratively until the agent determines the final answer is complete (25:48 - 26:00).
By using this pattern, developers can turn a standard Large Language Model (LLM) into a functional AI Agent capable of handling dynamic, real-world requests—like looking up current stock prices, checking flight status, or solving multi-step math problems that aren't stored in its training memory (6:13 - 17:46).




