import os
import re
from obsidiantools import ObsidianMD

def extractTags(filename):
    """Extracts Obsidian Markdown file tags from a given file.
    Args:
    file_path (str): The path to the file to extract tags from.
    Returns:
    list: A list of extracted tags.
    """
    obsidian_md = ObsidianMD(filename)
    tags = obsidian_md.get_tags()
    print(f"The file {filename} has tags {tags}")
    return tags

#def extractTags(filename):
#    """Extracts tags from a Markdown file."""  # Added docstring for clarity
#
#    tags = []
#    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
#        for line in file:
#            line = line.strip()
#            
#            if re.match(r'^#+\s+(\w+)', line):  # Updated regular expression
#                tag = re.match(r'^#+\s+(\w+)', line).group(1)  # Extract captured tag
#            #    tags.append(tag) 
#                print(f"Gemeni Code Thinks this is a tag {line}")
#            tag_match = re.match(r'^\s*#([^# ].+)$', line)
#            if tag_match:
#                tag = tag_match.group(1)
#                tags.append(tag)
#                print(f"OpenAI selected this {tag}")           
#    return tags

def makeIndex(folderToIndex, folderForIndexes):
    """Generates a Markdown table of notes with file links and tags and saves it to the required folder."""

    tableHeader1 = "| --- File --- | --- Tags --- | ---- Notes --- |\n"
    tableHeader2 = "| ------------ | ------------ | -------------- |\n"
    tableRows = []
    tableRows.append(tableHeader1)
    tableRows.append(tableHeader2)

    for filename in os.listdir(folderToIndex):
        print(f"Looking at File: {filename} ({'Markdown File' if filename.endswith('.md') else 'Not a Markdown File'})")
        if filename.endswith(".md"):
            filepath = os.path.join(folderToIndex, filename)

            tags = extractTags(filepath)  # Use our tag extraction function

            tableRows.append(f"| [[{filename}]] | {', '.join(tags) if tags else ''} |   |\n")
            indexFilename = os.path.basename(folderToIndex) + "-index.md"
            indexFilePath = os.path.join(folderForIndexes, indexFilename)
            with open(indexFilePath, 'w', encoding='utf-8') as indexFile:
                indexFile.writelines(tableRows)

folderForIndexes = r"D:\Obsidian Vaults\Second Brain\Indexes and Tasks"
foldersToIndex = [
    r"D:\Obsidian Vaults\Second Brain\Notes",
    r"D:\Obsidian Vaults\Second Brain\Diaries"
]
for folderToIndex in foldersToIndex:
    makeIndex(folderToIndex, folderForIndexes)