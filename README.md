# CyberpunK-manim

## Prerequisites 
It is recommended to use a virtual environment, e.g. miniconda environment.
- Miniconda Installed: https://docs.anaconda.com/miniconda/install/#quick-command-line-install. The following installation instruction is for **Linux**. Please **setup conda or any other venv** before go into the next step.
    ```bash
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm ~/miniconda3/miniconda.sh
    ```
    After installing, close and reopen your terminal application or refresh it by running the following command:
    ```bash
    source ~/miniconda3/bin/activate
    conda init --all
    ```
- Use `conda` to create a `python3.12` virtual environment (`manim-community`), and install required packages:
    ```bash
    conda create -n manim-community python=3.12
    conda activate manim-community
    pip3 install -e .
    ```

## Instruction
To build any manim-slides, for example, do:
```bash
cd example/
python example.py
```