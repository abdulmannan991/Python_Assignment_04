import streamlit as st
import random
import string
import re

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Ensure all text is visible */
        html, body, [class*="st-emotion-cache"] {
            color: white !important;
        }
        
        /* Fix checkbox text color */
        div[data-testid="stCheckbox"] label {
            color: white !important;
            font-size: 1.1rem;
            font-weight: bold;
        }
        
        /* Dark theme */
        .stApp {
            background-color: #0e1117 !important;
        }

        /* Password display box */
        .password-box {
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            background-color: #2a2d3a;
            padding: 10px;
            border-radius: 10px;
            word-wrap: break-word;
            margin-top: 15px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
        }

        /* Button styling */
        .stButton button {
            background-color: #ffcc00 !important;
            color: black !important;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }

        .stButton button:hover {
            background-color: #ffd633 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 style="text-align: center; color: white;">🔐 Password Strength Checker & Generator</h1>', unsafe_allow_html=True)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# User inputs password
password_input = st.text_input("Enter your password:", type="password")

# Check Password button
if st.button("🔍 Check Password"):
    if password_input:
        score, feedback = check_password_strength(password_input)

        if score == 4:
            st.success("✅ Strong Password! You can use this.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for item in feedback:
                st.markdown(f"- {item}")
    else:
        st.warning("⚠️ Please enter a password before checking.")

# Always show the password generation section
st.markdown("### Generate a Strong Password 🔄")

# Password length slider
length = st.slider("Select Password Length", min_value=8, max_value=32, value=12)

# Checkboxes for options
digits = st.checkbox("Include Digits")
special_characters = st.checkbox("Include Special Characters")

# Password generator function
def Password_Generator(length, digits, special_characters):
    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

# Generate password button
if st.button("⚡ Generate Password"):
    password = Password_Generator(length, digits, special_characters)
    st.markdown(f'<p class="password-box">{password}</p>', unsafe_allow_html=True)
    st.success("✅ Your secure password has been generated!")

# Footer
st.markdown('<p style="text-align: center; color: white;">🚀 Built by Abdul Mannan</p>', unsafe_allow_html=True)
