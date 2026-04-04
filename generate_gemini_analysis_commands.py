import shlex

def generate_gemini_cli_commands_from_file(rules_file="rules.txt"):
    """
    Lee reglas de un archivo y genera comandos gemini-cli ask para cada regla.
    """
    commands = []
    try:
        with open(rules_file, 'r', encoding='utf-8') as f:
            rules = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo de reglas '{rules_file}' no fue encontrado.")
        return []

    for i, rule in enumerate(rules):
        # Intentar determinar una categoría simple para el prompt si la regla lo indica
        category = "Regla General"
        if "Estilo y Gramática" in rule:
            category = "Estilo y Gramática"
        elif "Formato (LaTeX)" in rule:
            category = "Formato (LaTeX)"
        elif "Referencias" in rule:
            category = "Referencias"
        elif "Contenido y Presentación" in rule:
            category = "Contenido y Presentación"
        elif "Sobre el uso de gerundios" in rule:
            category = "Sobre el uso de gerundios"
        elif "Estructura de los capítulos" in rule:
            category = "Estructura de los capítulos"
        elif "Descripcion del Proyecto" in rule:
            category = "Descripción del Proyecto"

        # Ajustar el prompt para que sea específico y claro para el agente
        # Escapar la regla usando shlex.quote para asegurar que se manejen correctamente los espacios y caracteres especiales
        escaped_rule = shlex.quote(rule)
        
        prompt = (
            f"Analiza los archivos Chapters/Chapter1.tex, Chapters/Chapter2.tex y Chapters/Chapter3.tex "
            f"para encontrar violaciones de la siguiente regla: {escaped_rule} "
            f"({category}). Si encuentras violaciones, describe dónde están y cómo se pueden arreglar. "
            f"Si no encuentras violaciones, indícalo. Asegúrate de dar el contexto suficiente para las correcciones."
        )
        # shlex.quote también se usa para el prompt completo para asegurar el comando gemini-cli
        commands.append(f'gemini-cli ask {shlex.quote(prompt)}')
    return commands

if __name__ == "__main__":
    cli_commands = generate_gemini_cli_commands_from_file()

    for command in cli_commands:
        print(command)
