import os
import shutil
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="debug.log", format="%(asctime)s %(message)s", level=logging.DEBUG
)


def main():
    copy_directory("static", "public")


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


if __name__ == "__main__":
    main()
