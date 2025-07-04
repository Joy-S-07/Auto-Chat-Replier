import pyautogui
import time
import google.generativeai as genai
import pyperclip

client = genai.configure(api_key="GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash") 


def is_last_message_from_sender(chat_log, sender_name="NAME_OF_THE_PERSON_IN_THE_APP_TO_WHOM_THE_REPLY_WILL_BE_SENT"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

if __name__ == "__main__":
    # Give you time to switch to the target window
    print("Switching to the targeted window...")
    time.sleep(1)

    # Step 1: Click at the app of the chat from the gen-ai.py
    pyautogui.click(1269 ,1063)
    time.sleep(1)

    while True:
        # Step 2: Drag to select text from The starting position to ending positio that would be selected
        pyautogui.moveTo(674 , 218)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.moveTo(1843, 934, duration=0.5)
        pyautogui.mouseUp()
        time.sleep(1)
        # Step 3: Copy the selected chat
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(674 , 218) #dis-selecting to select again
        time.sleep(1)

        # Step 4: Get the chat history
        chat_history = pyperclip.paste()
        name = "YOUR_NAME_IN_THE_APP"

        # Only reply if the last message is not from you
        if is_last_message_from_sender(chat_history, sender_name="NAME_OF_THE_PERSON_IN_THE_APP_TO_WHOM_THE_REPLY_WILL_BE_SENT"):
            pyautogui.press('enter')
            response = model.generate_content(
                f"You are a person named {name} who speaks english. You are from India and you are a coder. You analyze {chat_history} and roast people in a funny way without technical terms in one line. Output should be the next chat response (text message only). Do not start like this [21:02, 12/6/2024] Rohan Das and do not reply of the masseges 2 or 3 before. Give the answer of last message only"
            )
            pyperclip.copy(response.text)
            # Paste the response
            pyautogui.click(842 , 990) # clicking on the typing box
            pyautogui.hotkey('ctrl', 'v') # pasting the reply
            pyautogui.click(1878 , 988) # position of the send button

        else:
            print(f"Last message is from {name}. No reply sent.")