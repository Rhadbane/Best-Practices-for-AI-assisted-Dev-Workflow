import json

def load_json_data(file_path: str) -> dict:
    """
    Charge les données d'un fichier JSON.

    Args:
        file_path (str): Le chemin d'accès au fichier JSON.

    Returns:
        dict: Les données chargées du fichier JSON.

    Raises:
        FileNotFoundError: Si le fichier n'est pas trouvé.
        json.JSONDecodeError: Si le fichier n'est pas un JSON valide.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{file_path}' n'a pas été trouvé.")
        raise
    except json.JSONDecodeError:
        print(f"Erreur: Le fichier '{file_path}' n'est pas un JSON valide.")
        raise




def filter_active_users(users_data: list[dict]) -> list[dict]:
    """
    Filtre une liste d'utilisateurs pour ne retenir que les utilisateurs actifs.

    Args:
        users_data (list[dict]): Une liste de dictionnaires représentant les utilisateurs.

    Returns:
        list[dict]: Une liste de dictionnaires d'utilisateurs actifs.
    """
    return [user for user in users_data if user.get("isActive", False)]




def extract_user_names(users: list[dict]) -> list[str]:
    """
    Extrait les noms d'une liste d'utilisateurs.

    Args:
        users (list[dict]): Une liste de dictionnaires d'utilisateurs.

    Returns:
        list[str]: Une liste des noms d'utilisateurs.
    """
    return [user.get("name", "") for user in users]




def process_user_data_refactored(file_path: str) -> list[str]:
    """
    Traite les données utilisateur à partir d'un fichier JSON pour extraire les noms des utilisateurs actifs.

    Args:
        file_path (str): Le chemin d'accès au fichier JSON contenant les données utilisateur.

    Returns:
        list[str]: Une liste des noms des utilisateurs actifs.
    """
    try:
        data = load_json_data(file_path)
        users = data.get("users", [])
        active_users = filter_active_users(users)
        active_user_names = extract_user_names(active_users)
        return active_user_names
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Exemple d'utilisation:
if __name__ == "__main__":
    # Créez un fichier de données d'exemple pour le test
    example_data = {
        "users": [
            {"id": 1, "name": "Alice", "isActive": True},
            {"id": 2, "name": "Bob", "isActive": False},
            {"id": 3, "name": "Charlie", "isActive": True},
            {"id": 4, "name": "David", "isActive": False}
        ]
    }
    with open("users_data.json", "w") as f:
        json.dump(example_data, f, indent=2)

    print("--- Test de la fonction originale ---")
    from data import process_user_data as original_process_user_data
    names_original = original_process_user_data("users_data.json")
    print(f"Noms des utilisateurs actifs (original): {names_original}")

    print("\n--- Test de la fonction refactorisée ---")
    names_refactored = process_user_data_refactored("users_data.json")
    print(f"Noms des utilisateurs actifs (refactorisé): {names_refactored}")

    # Test avec un fichier inexistant
    print("\n--- Test avec un fichier inexistant ---")
    names_non_existent = process_user_data_refactored("non_existent.json")
    print(f"Noms des utilisateurs actifs (fichier inexistant): {names_non_existent}")

    # Test avec un fichier JSON mal formé (simulé)
    with open("malformed_data.json", "w") as f:
        f.write("{'users': []") # JSON mal formé
    print("\n--- Test avec un fichier JSON mal formé ---")
    names_malformed = process_user_data_refactored("malformed_data.json")
    print(f"Noms des utilisateurs actifs (JSON mal formé): {names_malformed}")


