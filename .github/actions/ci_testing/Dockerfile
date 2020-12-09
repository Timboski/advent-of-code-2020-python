# Note: Should match .devcontainer/Dockerfile
FROM python:3.9.0
RUN pip install yapf flake8 parameterized
# Note: Not required for actions: rope, ipykernel

# Now add the code to run in CI
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]