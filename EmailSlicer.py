# collect email from user
# split the email using the @, the first part as the user name, the second part is gonna be saved as domain
# split domain using ..


from tabnanny import check


def main():
    print("Welcome to the email slicer\n")
    email_input = input("Input your email address \n")
    check_for_www = email_input[0:4]
    email_input = slice(0, 5) if check_for_www == "www." else email_input
    email_input = str(email_input)
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print(f"Username: {username}\nDomain: {domain}\nExtension: {extension}")

if __name__ == '__main__':
    main()