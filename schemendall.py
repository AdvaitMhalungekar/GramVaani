
# ✅ Step 2: Import and configure Gemini
import google.generativeai as genai

#  Your Gemini API Key
genai.configure(api_key="AIzaSyC31Q-Pr3hsUmpwaWUtnl9KcyIfnJ3BcDM")

# ✅ Step 3 (Fixed): List available models
# ✅ Show available models with full info
#for model in genai.list_models():
  #  print(f" {model.name} | Supports content generation: {'generateContent' in model.supported_generation_methods}")


# ✅ Step 4: Use a valid model (change based on available ones)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")  # or any supported one you see listed


# ✅ Step 5: User input profile
user_inputs = [
    {'identifier': 'gender', 'value': 'Female'},
    {'identifier': 'age-general', 'min': '28', 'max': '28'},
    {'identifier': 'maritalStatus', 'value': 'Married'},
    {'identifier': 'beneficiaryState', 'value': 'Delhi'},
    {'identifier': 'beneficiaryState', 'value': 'All'},
    {'identifier': 'residence', 'value': 'Rural'},
    {'identifier': 'residence', 'value': 'Both'},
    {'identifier': 'caste', 'value': 'General'},
    {'identifier': 'disability', 'value': 'No'},
    {'identifier': 'minority', 'value': 'No'},
    {'identifier': 'isStudent', 'value': 'No'},
    {'identifier': 'employmentStatus', 'value': 'Employed'},
    {'identifier': 'isGovEmployee', 'value': 'No'},
    {'identifier': 'occupation', 'value': 'Health Worker'},
    {'identifier': 'isBpl', 'value': 'No'},
    {'identifier': 'familyIncomeAnnual', 'min': '20000', 'max': '20000'}
]
# ✅ Step 6: Domain options
domains = {
    "1": "Agriculture, Rural & Environment",
    "2": "Banking, Financial Services and Insurance",
    "3": "Business & Entrepreneurship",
    "4": "Education & Learning",
    "5": "Health & Wellness"
}

# ✅ Step 7: User selects domain
print(" Select a domain to explore:")
for key, val in domains.items():
    print(f"{key}. {val}")

selected_key = input("\nEnter the number of the domain you want to explore (1–5): ").strip()
domain = domains.get(selected_key, None)

if not domain:
    print(" Invalid selection. Please run again and choose a number from 1–5.")
    exit()

# ✅ Step 8: Format user input
def format_user_input(data):
    formatted = ""
    for item in data:
        key = item['identifier'].replace('-', ' ').title()
        value = item.get('value') or f"{item.get('min')} to {item.get('max')}"
        formatted += f"- {key}: {value}\n"
    return formatted

# ✅ Step 9: Build prompt
def build_prompt(domain, user_input):
    return f"""
You are an assistant for suggesting Indian Government Welfare Schemes.

Only consider schemes under the domain: **{domain}**

Based on the user profile below, give a list of eligible schemes with:
1. Name of the Scheme
2. Description
3. Eligibility Summary

User Profile:
{format_user_input(user_input)}

Respond in a clean format. Only list relevant schemes the user is eligible for.
"""
# ✅ Step 10: Ask Gemini for eligible schemes
response = model.generate_content(build_prompt(domain, user_inputs))

# ✅ Step 11: Display output
print("\n Eligible Government Schemes:\n")
print(response.text)
