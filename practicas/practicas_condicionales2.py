print("asignaturas optativas año 2026")
print("Asignaturas optativas disponibles:")
print("- Informática")
print("- Artes")
print("- Deportes")

asignatura = input("Elegí una asignatura optativa: ")

# Normalizamos el texto para evitar errores por mayúsculas
asignatura = asignatura.lower()

if asignatura == "informatica":
    print("Elegiste Informática: aprenderás programación y tecnología 💻")
elif asignatura == "artes":
    print("Elegiste Artes: desarrollarás tu creatividad 🎨")
elif asignatura == "deportes":
    print("Elegiste Deportes: actividad física y trabajo en equipo ⚽")
else:
    print("La asignatura ingresada no está disponible.")
