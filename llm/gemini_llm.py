from google.generativeai import genai

def llm_call(prompt):
    try:
        model = genai.GenerativeModel('gemini-2-5-flash')
        response = model.generate_text(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {str(e)}") # Handle the exception and provide a meaningful error message
        return None
