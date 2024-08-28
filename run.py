"Main file to run cyber security data data science workflow."
import logging
from pathlib import Path

from src.input import read_cybersecurity_data
from src.transform import transform_data

data_folder = Path(".") / "data"
file_path = data_folder / "CloudWatch_Traffic_Web_Attack.csv"

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s :: %(levelname)-8s :: %(message)s"
)
logger = logging.getLogger()


def main():
    "Main function to run cybersecurity data science workflow."
    logger.info("Running Cybersecurity Data Science Workflow: %s", file_path)
    data = read_cybersecurity_data(file_path)
    logger.info(
        "Completed Running Cybersecurity Data Science Workflow, see outputs:"
    )
    data = transform_data(data)
    return data


if __name__ == "__main__":
    main()
