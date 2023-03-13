# UDR-2-EVCO2

## Description

Translates the data retrieved from the UDR model into the format accepted by the
[EVCO2](https://github.com/Horizon-LEAD/EV_EMISSIONS_UPM) model.

## Installation

The `requirements.txt` and `Pipenv` files are provided for the setup of an environment where the module can be installed. The package includes a `setup.py` file and it can be therefore installed with a `pip install .` when we are at the same working directory as the `setup.py` file. For testing purposes, one can also install the package in editable mode `pip install -e .`.

After the install is completed, an executable `udr-2-evco2` will be available to the user.

Furthermore, a `Dockerfile` is provided so that the user can package the model.

To build the image the following command must be issued from the project's root directory:
```
docker build -t udr-2-evco2:latest .
```

## Usage
The executable's help message provides information on the parameters that are needed.
```
$ udr-2-evco2 -h
usage: udr-2-evco2 [-h] udr_output vehicle_type_flag out_dir

UDR-2-EVCO2

Translates the data retrieved from the UDR model into the format accepted by the EVCO2 model.

positional arguments:
  udr_output         The path of the UDR output (xlxs)
  vehicle_type_flag  if vehicle type flag == 1 for fleet of electric motorbikes,
                     otherwise we have fleet of electric VANs
  out_dir            The output directory

options:
  -h, --help         show this help message and exit
```

If the package installation has been omitted, the model can of course also be run with
`python -m src.udr2evco2.__main__ <args>`

### Examples
```
udr-2-evco2 \
    sample-data/input/udr_output.xlsx \
    1 \
    sample-data/output/
```

```
docker run --rm \
    -v ./sample-data:/data \
    registry.gitlab.com/inlecom/lead/models/udr-2-evco2:latest \
    /data/input/udr_output.xlsx \
    1 \
    /data/output/
```
