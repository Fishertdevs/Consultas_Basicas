import sqlite3

# Nombre del archivo de la base de datos
DATABASE_NAME = "main.db"

def create_table():
    """Crea la tabla 'users' si no existe."""
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        connection.commit()
        connection.close()
        print("Tabla 'users' creada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

def insert_custom_data():
    """Permite al usuario insertar datos personalizados en la tabla."""
    while True:
        name = input("Ingrese el nombre: ").strip()
        if not name:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue
        try:
            age = int(input("Ingrese la edad: "))
            if age <= 0:
                print("La edad debe ser un número positivo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")
    
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        connection.commit()
        connection.close()
        print(f"Datos del usuario '{name}' insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")

def query_data():
    """Consulta y muestra todos los datos de la tabla."""
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        connection.close()

        if rows:
            print("\nDatos en la tabla 'users':")
            print(f"{'ID':<5} {'Nombre':<20} {'Edad':<5}")
            print("-" * 30)
            for row in rows:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5}")
        else:
            print("\nLa tabla 'users' está vacía.")
    except sqlite3.Error as e:
        print(f"Error al consultar datos: {e}")

def delete_user():
    """Permite al usuario eliminar un registro por ID."""
    query_data()
    try:
        user_id = int(input("\nIngrese el ID del usuario que desea eliminar: "))
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        connection.commit()
        connection.close()
        if cursor.rowcount > 0:
            print(f"Usuario con ID {user_id} eliminado correctamente.")
        else:
            print(f"No se encontró un usuario con ID {user_id}.")
    except ValueError:
        print("Por favor, ingrese un número válido para el ID.")
    except sqlite3.Error as e:
        print(f"Error al eliminar datos: {e}")

def update_user():
    """Permite al usuario actualizar los datos de un registro existente."""
    query_data()
    try:
        user_id = int(input("\nIngrese el ID del usuario que desea actualizar: "))
        name = input("Ingrese el nuevo nombre: ").strip()
        if not name:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            return
        age = int(input("Ingrese la nueva edad: "))
        if age <= 0:
            print("La edad debe ser un número positivo. Intente nuevamente.")
            return
        
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
        connection.commit()
        connection.close()
        if cursor.rowcount > 0:
            print(f"Usuario con ID {user_id} actualizado correctamente.")
        else:
            print(f"No se encontró un usuario con ID {user_id}.")
    except ValueError:
        print("Por favor, ingrese valores válidos para el ID y la edad.")
    except sqlite3.Error as e:
        print(f"Error al actualizar datos: {e}")

def menu():
    """Muestra el menú principal y permite al usuario interactuar con la base de datos."""
    while True:
        print("\nMenú:")
        print("1. Crear tabla")
        print("2. Insertar datos personalizados")
        print("3. Consultar datos")
        print("4. Actualizar datos de un usuario")
        print("5. Eliminar un usuario")
        print("6. Salir")
        choice = input("Seleccione una opción: ").strip()

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_custom_data()
        elif choice == "3":
            query_data()
        elif choice == "4":
            update_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            print("\nSaliendo del programa...")
            print("Desarrollado por Harry Fishert")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()