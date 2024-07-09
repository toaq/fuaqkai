init:
	pdm install
	pdm run pre-commit install

build:
	podman-compose build

up:
	podman-compose up -d

down:
	podman-compose down

stop:
	podman-compose stop

logs:
	podman-compose logs

local:
	pdm run python -m fuaqkai
