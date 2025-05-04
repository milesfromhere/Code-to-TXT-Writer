import os

# Путь к корню проекта WPF
project_root = r"C:\путь"  # <-- Путь к проекту
output_file = r"C:\путь"  # <-- Выходной файл

# Включаемые расширения 
included_extensions = {'.cs', '.xaml','xaml.cs' , '.xml'}

# Исключаемые расширения
excluded_suffixes = {'.g.cs', '.designer.cs', '.AssemblyInfo.cs'}

with open(output_file, 'w', encoding='utf-8') as out_file:
    for root, _, files in os.walk(project_root):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext.lower() in included_extensions:
                if any(file.endswith(suffix) for suffix in excluded_suffixes):
                    continue
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        out_file.write(f"\n--- FILE: {file_path} ---\n")
                        out_file.write(f.read())
                        out_file.write("\n\n")
                except Exception as e:
                    print(f"Ошибка при чтении {file_path}: {e}")
