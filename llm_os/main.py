from .cpu import CPU


def main():
    cpu = CPU()
    while True:
        prompt = input("You: ")
        _ = cpu.streaming_chat(prompt)
        print()
        if prompt == "exit":
            break
