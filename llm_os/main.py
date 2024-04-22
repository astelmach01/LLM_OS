from .cpu import CPU


def main():
    cpu = CPU()
    while True:
        prompt = input("You: ")
        response = cpu.chat(prompt)
        print(response)
        if prompt == "exit":
            break
