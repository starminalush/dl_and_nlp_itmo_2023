import tempfile
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from kaggle import api  # noqa: E402

api.authenticate()


def download_dataset_from_kaggle(
    dataset_name: str, output_path: str | Path | None = None
) -> Path | str:
    """Download external dataset from kaggle by dataset name.

    Args:
        dataset_name: Kaggle dataset name.
        output_path: Downloaded dataset path.

    Returns:
        Downloaded dataset path.
    """
    dataset_output_path = output_path or tempfile.TemporaryDirectory()
    api.dataset_download_files(dataset_name, path=dataset_output_path, unzip=True)
    return dataset_output_path
