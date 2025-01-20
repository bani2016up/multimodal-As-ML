

from lumina.modules.llumina.chat import LuminaChat
from database import DocumentStore


def main() -> None:
    ds = DocumentStore()
    chat: LuminaChat = LuminaChat(ds)
    with chat.model.model.chat_session():
        chat.load_context()
        while True:
            user_input = input("..| ")
            if user_input == "exit":
                break
            commands_response = [input(f"c{i}") for i in range(int(input("range")))]
            for response in chat.ask(user_input, commands_response):
                print(response, end="")
            print("\n")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    main()
