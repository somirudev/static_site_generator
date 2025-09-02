import os
import sys
import shutil
import logging
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="debug.log", format="%(asctime)s %(message)s", level=logging.DEBUG
)


def main():
    if os.getenv("GITHUB_ACTIONS") == "true":
        argument_loc = 2
    else:
        argument_loc = 1
    if len(sys.argv) > argument_loc:
        basepath = sys.argv[argument_loc]
    else:
        basepath = "/"
    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


def copy_directory(source, destination):
    if os.path.exists(destination):
        logger.info(f"deleting {destination} contents")
        shutil.rmtree(destination)
    os.mkdir(destination)
    source_directory_files = os.listdir(source)
    for file in source_directory_files:
        source_filepath = os.path.join(source, file)
        destination_filepath = os.path.join(destination, file)
        if os.path.isfile(source_filepath):
            logger.info(f"copying {source_filepath} to {destination_filepath}")
            shutil.copy(source_filepath, destination_filepath)
        else:
            logger.info(f"making directory: {destination_filepath}")
            os.mkdir(destination_filepath)
            copy_directory(source_filepath, destination_filepath)


def generate_pages_recursive(source, template_path, destination, basepath):
    if not os.path.exists(destination):
        os.mkdir(destination)
    source_directory_files = os.listdir(source)
    for file in source_directory_files:
        source_filepath = os.path.join(source, file)
        destination_filepath = os.path.join(destination, file)
        if os.path.isfile(source_filepath):
            generate_page(
                source_filepath,
                template_path,
                destination_filepath[:-2] + "html",
                basepath,
            )
        else:
            logger.info(f"making directory: {destination_filepath}")
            os.mkdir(destination_filepath)
            generate_pages_recursive(
                source_filepath, template_path, destination_filepath, basepath
            )


def generate_page(from_path, template_path, dest_path, basepath):
    logger.info(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    page_with_title = template.replace("{{ Title }}", title)
    page_with_html = page_with_title.replace("{{ Content }}", html)
    page_with_basepath = page_with_html.replace('href="/', f'href="{basepath}')
    page_with_sourcepath = page_with_basepath.replace('src="/', f'src="{basepath}')
    try:
        if not os.path.exists(os.path.dirname(dest_path)):
            os.makedirs(os.path.dirname(dest_path))
    except OSError as err:
        if err.errno != 17:
            raise err
        pass
    with open(dest_path, "w") as f:
        f.write(page_with_sourcepath)


if __name__ == "__main__":
    main()
