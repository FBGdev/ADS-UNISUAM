def email_valido(email):
    if "@" not in email or "." not in email:
        return False

    if email.startswith("@") or email.startswith("."):
        return False

    if email.endswith("@") or email.endswith("."):
        return False

    if email.count("@") != 1:
        return False

    parte_antes_arroba, parte_depois_arroba = email.split("@")

    if parte_antes_arroba == "" or parte_depois_arroba == "":
        return False

    return "." in parte_depois_arroba


def telefone_valido(telefone):
    return telefone.isdigit() and len(telefone) >= 10


def main():
    email_usuario = input("Digite seu e-mail: ").strip()
    telefone_usuario = input("Digite seu telefone: ").strip()

    if email_valido(email_usuario):
        print("E-mail valido.")
    else:
        print("E-mail invalido.")

    if telefone_valido(telefone_usuario):
        print("Telefone valido.")
    else:
        print("Telefone invalido.")


if __name__ == "__main__":
    main()
