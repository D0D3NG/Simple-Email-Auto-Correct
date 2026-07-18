
#SIMPLE EMAIL CREATOR WITH AUTOMATIC CLEANUP

#Input user birth name and email, removing whitespaces and numbers in the registered name
fn = input("What is your First Name? ").title().lstrip().strip("1" "2" "3" "4" "5" "6" "7" "8" "9" "0").rstrip()
ln = input("What is your Last Name? ").title().lstrip().strip("1" "2" "3" "4" "5" "6" "7" "8" "9" "0").rstrip()
email = input("What is your Email? ").lower().strip()

#if user inputs an invalid email (eg: typo in email or unsupported email)
if "@gmail.com" not in email and "@yahoo.com" not in email and "@outlook.com" not in email: #supported email domains
    print("Invalid email, please try again.")
else: 
    print(f"Account created for {fn} {ln} ({email})") #output when things go as intended
