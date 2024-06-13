import google.generativeai as genai

YOUR_API_KEY = "YOUR_API_KEY_HEAR"

genai.configure(api_key=YOUR_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content('tell me a poite in Japanese in 20 words' )

print(response.text)
# happy coding jorny 