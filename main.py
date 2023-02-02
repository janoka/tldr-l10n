import os
import deepl as deepl
import markdown
from markdownify import markdownify
from mdformat import text as mdformat
from dotenv import load_dotenv


def parse_source_folder():
    """Create non-existing target folder, according to the source folder"""
    # Import environment variables from .env file
    load_dotenv()

    # Initialize sources list
    sources = []

    # Get source folder
    source_folder = f"{os.getenv('TLDR_ROOT')}/pages"

    # Get subfolders in source folder
    sub_folders = [folder for folder in os.listdir(source_folder) if os.path.isdir(
        f"{source_folder}/{folder}")]

    # Get all files in source_folder and its subfolders
    for folder in sub_folders:
        files = [file for file in os.listdir(
            f"{source_folder}/{folder}") if os.path.isfile(f"{source_folder}/{folder}/{file}")]
        for file in files:
            sources.append(f"{source_folder}/{folder}/{file}")

    return sources


def readfile(file: str):
    """Read the markdown file"""
    markdown_file = open(file, "r")
    markdown_text = markdown_file.read()
    markdown_file.close()
    return markdown_text


def savefile(target: str, text: str):
    """Save the file"""
    with open(target, "w") as file:
        file.write(text)


def target(source: str):
    # Split the path to filename and sub folder name.
    # Example: /Users/username/tldr/pages/osx/gdf.md -> osx, gdf.md
    folder, md = source.split("/")[-2:]

    # Return the target folder string
    # Example: /Users/username/tldr/pages.hu/osx/gdf.md
    target_file = f"{os.getenv('TLDR_ROOT')}/pages.{os.getenv('TLDR_LANG')}/{folder}/{md}"

    # Create the target folder if it doesn't exist
    if not os.path.exists(os.path.dirname(target_file)):
        os.makedirs(os.path.dirname(target_file))

    return target_file


if __name__ == '__main__':
    sources = parse_source_folder()

    for source in sources[0:3900]:
        md = readfile(source)
        target_file = target(source)

        # Do the following if the file is not exist
        if not os.path.exists(target_file):
            # Convert markdown to html
            html = markdown.markdown(md)
            # Add translate="no" attribute to all <h1>, <pre>, and <code> tags
            html = html.replace('<h1>', '<h1 translate="no">')
            html = html.replace('<pre>', '<pre translate="no">')
            html = html.replace('<code>', '<code translate="no">')

            translator = deepl.Translator(os.getenv('DEEPL_API_KEY'))
            html = str(translator.translate_text(text=html,
                                                 tag_handling='html',
                                                 source_lang='en',
                                                 target_lang=os.getenv('TLDR_LANG'),
                                                 ignore_tags=['h1', 'pre', 'code']))
            # Convert html to markdown
            md_export = mdformat(markdownify(
                html, heading_style='atx', bullets='-'))
            savefile(target_file, md_export)
