import yaml

from biological_age.data.make_interim import (
    run_make_interim
)


def load_config(config_path: str = "config.yaml"):

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config


if __name__ == "__main__":

    config = load_config()

    run_make_interim(config)
