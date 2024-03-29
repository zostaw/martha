# Martha

Simple demonstration of **Function Calling** in local LLM model.  
It's commandline chat interface to model.  
It uses a simple prompt to guide assistant to teach you python and when code is suggested, it can be evaluated directly in chat.  
The program stores history of conversation.

Supported format: *GGUF*


## Usage


1. Download LLM chat model, i.e. [OpenHermes 2.5 Mistral 7B](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF/blob/main/openhermes-2.5-mistral-7b.Q5_0.gguf) from Hugging Face.

2. Adjust model path in martha.py (by default it's looking under: *./models/openhermes-2.5-mistral-7b-16k.Q5_K_M.gguf*)

3. Execute:

```python
./martha.py
```

Begin conversation...

```
user:
```

## Example conversation

In below example **bold** statements are written by user, the *rest* (including provided code and output) is output of the program.

###### Conversation

*user:* **What are list comprehensions?**  
*assistant: List comprehensions are a concise way to create lists in Python by combining a loop and a conditional statement into a single line of code. They provide an efficient and readable way to generate new lists based on existing lists or other iterable objects. Here's an example:*  

```
# Original list
original_list = [1, 2, 3, 4, 5, 6]

# List comprehension to double each element in the list
doubled_list = [num * 2 for num in original_list]
print("Original list:", original_list)  # Original list: [1, 2, 3, 4, 5, 6]
print("Doubled list:", doubled_list)  # Doubled list: [2, 4, 6, 8, 10, 12]
```

*In this example, we create a new list called `doubled_list` by multiplying each element of `original_list` by 2 using a list comprehension. The syntax is `[expression for item in iterable]`, where `expression` is the operation you want to perform on each item and `iterable` is the list or other iterable object you're operating on.*  
*Do you want to execute the code (y/n)?* **y**  
*Output:*  
```
Original list: [1, 2, 3, 4, 5, 6]
Doubled list: [2, 4, 6, 8, 10, 12]
```
