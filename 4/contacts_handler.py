def validate_args(args: list, expected_length: int) -> None:
    if len(args) != expected_length:
        raise ValueError(f"Exactly {expected_length} argument(s) are required.")


def add_contact(args: list, contacts: dict) -> str:
    try:
        validate_args(args, 2)
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while adding contact: {type(e).__name__}, {e}"


def change_contact(args: list, contacts: dict) -> str:
    try:
        validate_args(args, 2)
        name, phone = args
        if name not in contacts:
            return "Contact does not exist."
        contacts[name] = phone
        return "Contact updated."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while changing contact: {type(e).__name__}, {e}"


def get_contact(args: list, contacts: dict) -> str:
    try:
        validate_args(args, 1)
        name = args[0]
        if name not in contacts:
            return "Contact does not exist."
        return contacts[name]
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while getting contact: {type(e).__name__}, {e}"


def get_all_contacts(contacts: dict) -> str:
    if not contacts:
        return "Contacts are empty."

    contacts_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return f"Contacts:\n{contacts_list}"
