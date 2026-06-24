# env/Dockerfile — optional: wrap the prebuilt LeRobot GPU image.
#
# Using the prebuilt image skips dependency-resolution pain for the SmolVLA stack.
# Build:  docker build -f env/Dockerfile -t vlamem:dev .
# Run:    docker run --gpus all -it -v "$PWD":/workspace vlamem:dev

FROM ioaitech/lerobot-gpu:v0.5.0

WORKDIR /workspace

# Support libraries + the research package (editable).
COPY env/requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /workspace
RUN python -m pip install --no-cache-dir -e ".[dev]"

# Default to an interactive shell; experiments are launched explicitly.
CMD ["/bin/bash"]
