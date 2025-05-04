import os

# Путь к корню проекта WPF
project_root = r"C:\путь"  # <-- Путь к проекту
output_file = r"C:\путь"  # <-- Выходной файл

# Расширения файлов, которые будем учитывать (можно добавить или убрать по необходимости)
target_extensions = {'.cs', '.xaml', '.xml', 'xaml.cs'}

with open(output_file, 'w', encoding='utf-8') as out_file:
    for root, _, files in os.walk(project_root):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext.lower() in target_extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        out_file.write(f"\n--- FILE: {file_path} ---\n")
                        out_file.write(f.read())
                        out_file.write("\n\n")
                except Exception as e:
                    print(f"Ошибка при чтении {file_path}: {e}")
