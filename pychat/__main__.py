import openai
import os

OPEN_API_KEY = 'OPENAI_API_KEY'

# todo
# handle detection of OPEN_API_KEY availability
# max_tokens can be set as a parameter outside with a default value
# 


def main():

    open_ai_api_key = os.getenv(OPEN_API_KEY)

    if open_ai_api_key == None:
        print('OPENAI_API_KEY required')
        exit(-1)
        
    print("Pychat v0.1")
    query = input("Input: ")

    completion = openai.Completion.create(
        engine="text-davinci-003", prompt=query, max_tokens=4000
    )

    output = completion.choices[0].text
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
