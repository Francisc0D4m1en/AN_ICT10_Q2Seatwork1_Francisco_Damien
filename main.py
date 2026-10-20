from pyscript import document, display

my_list = ["Aldrich Mandani", "Ruel Roque", "John F. Kennedy", "Napoleon Bonaparte"]

def applicant_search(e):
    first_name = document.getElementById("user_input").value.strip()
    last_name = document.getElementById("user_input2").value.strip()
    full_name = f"{first_name} {last_name}".title()  # Joins both inputs and converts to title case.
    message = document.getElementById("message")

    if full_name.lower() in [n.lower() for n in my_list]:  # Checks against list, ignoring case variance.
        message.innerHTML = f"Congratulations, {full_name}! You are qualified to join the SS Club."  # F string is used to convert full_name variable ino string for display.
    else:
        message.innerHTML = f"Apologies, {full_name}, you do not meet the qualifications required to join the SS Club."
        
    document.getElementById("user_input").value = ""
    document.getElementById("user_input2").value = ""

