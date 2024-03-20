import os

def generate_notes_table(notes_folder_path):
    """Generates a Markdown table of notes with file links and tags."""

    table_header = "| File | Tags | Notes |\n|---|---|---|\n"
    table_rows = ""

    for filename in os.listdir(notes_folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(notes_folder_path, filename)
            with open(filepath, 'r') as file:
                tags = []
                for line in file:
                    if line.startswith("#"):
                        tags.append(line.strip()[1:])  # Extract tags
                    else:
                        break  # Stop after first non-tag line

            file_link = f"[[{filename}]]"
            tags_column = ", ".join(tags) if tags else ""
            table_rows += f"| {file_link} | {tags_column} | |\n"

    return table_header + table_rows

notes_folder_path = "path/to/your/Notes/folder"  # Replace with your actual folder path
table_output = generate_notes_table(notes_folder_path)

# Save the table to a Markdown file
with open("notes_reference.md", "w") as f:
    f.write(table_output)
