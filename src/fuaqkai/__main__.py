import logging
import os

import hikari


BOT_TOKEN = os.environ["BOT_TOKEN"]
LOG_LEVEL = os.environ["LOG_LEVEL"].upper()
TEST_SERVERS = [int(n) for n in os.environ["TEST_SERVERS"].split(",") if n]

LOG = logging.getLogger()


def init_logger():
    """Initializes log formatting and level."""
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)
    datefmt = "%Y-%m-%d %H:%M:%S"
    fmt = logging.Formatter(
        "[{asctime}] [{levelname}] {name}: {message}", datefmt, style="{"
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    root_logger.addHandler(stream_handler)


def main():
    assert BOT_TOKEN, "a token was not provided in the environment!"
    init_logger()

    bot: hikari.GatewayBot = hikari.GatewayBot(BOT_TOKEN)
    # client: arc.GatewayClient = arc.GatewayClient(bot)

    bot.run()
