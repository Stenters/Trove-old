import os
import shutil

MD_DIR = "Trove"
md_files = []
md_links = []
toc_string = """
# Welcome!
This is a basic landing page for the Trove Wiki

# Links
For pages, see below:
"""

def get_md_files():
    out = os.walk(MD_DIR)
    for group in out:
        for file in group[2]:
            if file.endswith('.md'):
                md_files.append(file)
    return md_files

def get_md_link(name):
    name.replace(" ", "_")
    return name

def main():
    for md in get_md_files():
        link = get_md_link(md)
        md_links.append(link)

    toc = open("index.md","w")
    toc.write(toc_string)

    for link in md_links:
        toc.write(f"[[{link}]]\n")


if __name__ == "__main__":
    main()
