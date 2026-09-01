def recognize_dialog_act(sentence):

    text = sentence.lower()

    if text.endswith("?"):
        return "QUESTION"

    elif text.startswith(
        ("please", "can you", "could you")
    ):
        return "REQUEST"

    elif text.startswith(
        ("hello", "hi", "hey")
    ):
        return "GREETING"

    elif text.startswith(
        ("thank", "thanks")
    ):
        return "THANKING"

    elif text.startswith(
        ("yes", "okay", "sure")
    ):
        return "ACCEPTANCE"

    else:
        return "STATEMENT"


text = input("Enter dialog sentence: ")

print("Dialog Act:",
      recognize_dialog_act(text))
