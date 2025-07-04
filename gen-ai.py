import google.generativeai as genai

client = genai.configure(api_key="GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash") 
model = genai.GenerativeModel("gemini-2.5-flash")
name = "YOUR_NAME_ON_WHATSAPP"
response = model.generate_content(f"You are a person named {name}. Get the chat history and reply to the user as you are {name} from the chat history.")
print(response.text)