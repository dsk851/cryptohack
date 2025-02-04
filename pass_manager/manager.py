import sqlite3
from cryptography.fernet import Fernet

def init_db():
    con = sqlite3.connect("password.db")
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def add_password(site, username, password):
    encrypted_password = CIPHER.encrypt(password.encode())
    con = sqlite3.connect("password.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO passwords (site, username, password) VALUES (?,?,?)", (site, username, encrypted_password))
    con.commit()
    con.close()
    print(f"🔒 Mot de passe enregistré pour {site}")


def get_password(site):
    con = sqlite3.connect("password.db")
    cursor = con.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE site=?", (site,))

    result = cursor.fetchone()
    con.close()

    if result:
        username, encrypted_password = result
        decrypted_password = CIPHER.decrypt(encrypted_password).decode()
        print(f"✅ Identifiant : {username}\n🔑 Mot de passe : {decrypted_password}")
    else:
        print("❌ Site non trouvé.")


def delete_password(site):
    con = sqlite3.connect("password.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM passwords WHERE site=?", (site,))
    result = cursor.rowcount
    con.commit()
    con.close()
    if result > 0 :
        print(f"🗑 Mot de passe supprimé pour {site}")
    else:
        print("Site non trouve")


def main():
    # print(f"\n the key : {KEY} and the cihper :{CIPHER}")
    while True:
        print("\n--- Password Manager ---")
        print("1. Ajouter un mot de passe")
        print("2. Récupérer un mot de passe")
        print("3. Supprimer un mot de passe")
        print("4. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            site = input("Site : ")
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            add_password(site, username, password)

        elif choice == "2":
            site = input("Site : ")
            get_password(site)

        elif choice == "3":
            site = input("Site : ")
            delete_password(site)

        elif choice == "4":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    init_db()
    generate_key()

    KEY = load_key()
    CIPHER = Fernet(KEY)
    main()
