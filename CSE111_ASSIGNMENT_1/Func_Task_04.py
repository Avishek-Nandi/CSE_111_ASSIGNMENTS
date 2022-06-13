# Solution to Task 4 (Functions)

def domain_changer(mail, new, old=None):
    status = "Unchanged" if old is None else "Changed"
    mail = (mail[:-len(old)] + new) if old is not None else mail
    print(f"{status}: {mail}")


if __name__ == "__main__":
    user = [i.strip("' ") for i in input().strip("() ").split(",")]
    try:
        mail, new, old = user
        domain_changer(mail, new, old)
    except:
        mail, new = user
        domain_changer(mail, new)

