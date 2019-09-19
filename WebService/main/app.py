from aiohttp import web

from main.setup.setup import Setup

if __name__ == '__main__':
    setup = Setup()
    web.run_app(app=setup.app)
