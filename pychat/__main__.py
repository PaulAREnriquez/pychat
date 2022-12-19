import openai
import os
import argparse

OPEN_API_KEY = "OPENAI_API_KEY"


def main():
    # Parameterizing arguments from the command line
    parser = argparse.ArgumentParser(description="Pychat v0.1")
    # max-tokens is the flag
    parser.add_argument(
        "--max-tokens", help="Maximum size of tokes used", type=int, default=4000
    )
    parser.add_argument(
        "--engine",
        help="The openai engine to use",
        type=str,
        default="text-davinci-003",
    )

    args = parser.parse_args()
    # max-tokens become max_tokens here
    max_tokens = args.max_tokens
    engine = args.engine

    print("Options:")
    print(f"Max tokens: {max_tokens}")
    print(f"Engine: {engine}")

    open_ai_api_key = os.getenv(OPEN_API_KEY)

    if open_ai_api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    # print("Pychat v0.1")

    query = input("Input: ")
    if query != "":

        completion = openai.Completion.create(
            engine=engine, prompt=query, max_tokens=max_tokens
        )

        output = completion.choices[0].text
        print(f"Output: {output}")
    else:
        print("You did not ask anything.")


if __name__ == "__main__":
    main()
