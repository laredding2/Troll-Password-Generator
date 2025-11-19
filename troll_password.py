import re
import random

def check_password(password):
    """Check password and return increasingly ridiculous requirements."""
    
    issues = []
    
    # Basic requirements
    if len(password) < 8:
        issues.append("❌ Password must be at least 8 characters long")
    
    if not re.search(r'[A-Z]', password):
        issues.append("❌ Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        issues.append("❌ Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        issues.append("❌ Password must contain at least one number")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        issues.append("❌ Password must contain at least one special character")
    
    # Now the trolling begins...
    if len(password) >= 8 and not issues:
        
        if len(password) < 12:
            issues.append("❌ Just kidding! Password must be at least 12 characters")
        
        elif not re.search(r'\d.*\d.*\d', password):
            issues.append("❌ Password must contain at least THREE numbers")
        
        elif not re.search(r'[A-Z].*[A-Z]', password):
            issues.append("❌ Password must contain at least TWO uppercase letters")
        
        elif sum(c.isdigit() for c in password) % 2 != 0:
            issues.append("❌ The number of digits must be EVEN")
        
        elif not any(emoji in password for emoji in ['🔥', '💀', '🚀', '⚡', '🎮']):
            issues.append("❌ Password must contain at least one emoji: 🔥 💀 🚀 ⚡ 🎮")
        
        elif 'pizza' not in password.lower():
            issues.append("❌ Password must contain the word 'pizza'")
        
        elif len(password) < 20:
            issues.append("❌ Actually, we need MORE security. Minimum 20 characters now!")
        
        elif not re.search(r'\d{3,}', password):
            issues.append("❌ Password must contain at least 3 consecutive digits")
        
        elif password[0].islower():
            issues.append("❌ Password must START with an uppercase letter")
        
        elif password[-1] != '!':
            issues.append("❌ Password must END with an exclamation mark!")
        
        elif 'cyber' not in password.lower():
            issues.append("❌ For extra cybersecurity, include the word 'cyber'")
        
        elif sum(c.isupper() for c in password) < 4:
            issues.append("❌ Need at least FOUR uppercase letters for maximum security")
        
        elif not re.search(r'[aeiou]{2,}', password.lower()):
            issues.append("❌ Password must contain at least 2 consecutive vowels")
        
        elif len(set(password)) < 15:
            issues.append("❌ Password must contain at least 15 UNIQUE characters")
        
        else:
            # They finally made it through everything
            return None
    
    return issues

def main():
    print("🔐 ULTRA-SECURE PASSWORD CREATOR 3000 🔐")
    print("=" * 50)
    print("Create a secure password that meets our requirements!\n")
    
    attempts = 0
    
    while True:
        attempts += 1
        password = input(f"\nAttempt #{attempts} - Enter your password: ")
        
        issues = check_password(password)
        
        if issues is None:
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! 🎉")
            print(f"Your password is accepted after {attempts} attempts!")
            print(f"Your ultra-secure password is: {password}")
            print("=" * 50)
            break
        else:
            print("\n🚫 PASSWORD REJECTED! 🚫")
            for issue in issues:
                print(f"  {issue}")
            
            if attempts % 5 == 0:
                print(f"\n💡 Hint: You've tried {attempts} times. Don't give up!")

if __name__ == "__main__":
    main()
