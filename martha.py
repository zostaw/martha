#!/usr/bin/env python3

from llama_cpp import Llama
from io import StringIO
import sys
import json
from pathlib import Path
import subprocess

CONVERSATION_FILE = Path("conversation_history.txt")
MODEL="./models/openhermes-2.5-mistral-7b-16k.Q5_K_M.gguf"

def run_python_code(code):
    if not isinstance(code, str):
        print(f'Found code "{code}" is not string...')
        return
    if code == "":
        print(f'Found code "{code}" is empty string...')
        return

    out = ""
    if input("Do you want to execute the code (y/n)? ") == "y":
        # out = subprocess.run(['which', 'python'], capture_output=True, text=True)
        # pyth_ver = out.stdout
        # print(f"python: {pyth_ver}")
        old_stdout = sys.stdout
        with StringIO() as stringio:
            redirected_output = sys.stdout = stringio
            exec(code)
            sys.stdout = old_stdout
            out = f"Output:\n```\n{redirected_output.getvalue()}\n```\n"
    return out


def main():
    # initiate
    assistant_name = Path(__file__).name
    assistant_path = Path(__file__).absolute()
    system_prompt = f"You are a python program living under {assistant_path}. {assistant_name} writes Python code to answer questions. She keeps the code as short as possible and doesn't read from user input."
    llm = Llama(
        model_path=MODEL,
        n_ctx=4096,
        temperature=0.7,
        verbose=False,
        chat_format="chatml",
        n_gpu_layers=1,
    )

    
    if CONVERSATION_FILE.is_file():
        with open(CONVERSATION_FILE, "r") as file:
            messages = json.load(file)
    else:
        messages = [
            {"role": "system", "content": system_prompt},
        ]


    while True:
        user_input = input("user: ")
        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        output_generator = llm.create_chat_completion(messages=messages)

        role, content = (
            output_generator["choices"][0]["message"]["role"],
            output_generator["choices"][0]["message"]["content"],
        )
        print(f"{role}: {content}")

        # handle python code execution
        code_output = ""
        if "```" in content and "```python\n" in content:
            python_code = content.split("```python\n")[1].split("```")[0]
            code_output = run_python_code(python_code)
            print(code_output)
        output_with_plugins = content + "\n" + code_output

        #print(f"DEBUG: {output_with_plugins}")

        # update conversation history
        messages.append(
            {
                "role": "assistant",
                "content": output_with_plugins,
            }
        )

        json_dump = json.dumps(messages, indent=2)
        with open(file=CONVERSATION_FILE, mode="w") as file:
            file.write(json_dump)


if __name__ == "__main__":
    main()
