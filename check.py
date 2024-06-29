def email_check(email):
    """this function checks the validity of email

    Args:
        email (str): email that needs to be checked


    Returns:
        boolean : returns true if email is vald , else it returns False
    """
    try:
        chck = "*&^%$#!()-+={}[];:><,/?~`"
        a, b = email.split('@')
        c, d = b.split('.')
        
        if email.count('@') != 1:  # should be exactly one '@'
            raise Exception("Email should have exactly one '@'")
        elif any(letter in chck for letter in email):
            raise Exception("Email cannot contain special characters")
        elif len(a) < 3 or len(c) < 2 or len(d) > 3 or len(d) < 1:
            raise Exception("Invalid email format")
        else:
            print("Valid email")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def phone_check(phoneno):
    """this function checks validitty of the phone number provided 

    Args:
        phoneno (str): phone number that needs to be checked


    Returns:
        boolean:returns true if phone number is vald , else it returns False
    """
    try:
        chck = "1234567890"
        if len(phoneno) != 10:
            raise Exception("Phone number should have exactly 10 digits")
        elif any(i not in chck for i in phoneno):
            raise Exception("Phone number cannot contain characters other than numbers")
        else:
            print("Valid phone number")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print(email_check("w@l.c"))
    print(phone_check("1234567890"))