def check_password_strength(password):
  """
  Analyzes the strength of a password based on various criteria.

  Args:
      password: The password string to be evaluated.

  Returns:
      A tuple containing:
          - strength_score (int): A score indicating password strength (higher is better).
          - feedback (str): A message providing feedback on password strength.
  """
  score = 0
  feedback = ""

  # Check password length
  if len(password) >= 12:
    score += 2
    feedback += "Length is good (12 characters or more). "
  elif len(password) >= 8:
    score += 1
    feedback += "Length is okay (8-11 characters), but consider making it longer. "
  else:
    feedback += "Password is too short (less than 8 characters). "

  # Check for uppercase letters
  if any(char.isupper() for char in password):
    score += 1
    feedback += "Contains uppercase letters. "
  else:
    feedback += "Consider adding uppercase letters. "

  # Check for lowercase letters
  if any(char.islower() for char in password):
    score += 1
    feedback += "Contains lowercase letters. "
  else:
    feedback += "Consider adding lowercase letters. "

  # Check for numbers
  if any(char.isdigit() for char in password):
    score += 1
    feedback += "Contains numbers. "
  else:
    feedback += "Consider adding numbers. "

  # Check for special characters
  if any(char in "!@#$%^&*()" for char in password):
    score += 1
    feedback += "Contains special characters. "
  else:
    feedback += "Consider adding special characters. "

  # Strength rating based on score
  if score >= 5:
    feedback += "Strong password!"
  elif score >= 3:
    feedback += "Moderate password. Consider adding more complexity."
  else:
    feedback += "Weak password. Consider making it longer and more complex."

  return score, feedback

def main():
  password = input("Enter your password: ")
  strength_score, feedback = check_password_strength(password)
  print(feedback)

if __name__ == "__main__":
  main()
