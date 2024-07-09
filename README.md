# mı fuaqkaı

mı fuaqkaı is a Discord bot for creating images of Deranı.

Requires Python 3.12.* and pdm.

## Development setup

Run `make install` to get the basic dependencies and pre-commit checks.

For a development environment, make sure you set your `.env`'s `TEST_SERVERS` key to have a server so that slash commands work better, separated by `,`.

To start the bot, use `make local`.

## Production setup

Requires Podman and Podman Compose as well.

Run `make build` first, then you can `make up` to start the bot. For other commands, see the Makefile.
