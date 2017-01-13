#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import asyncio
from aiohttp import web
__author__ = 'JeffreyLuo'

'''
async web application.
'''

logging.basicConfig(level=logging.INFO)


def index(request):
    logging.info(request)
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='utf-8')


# 协程 老方法
# @asyncio.coroutine
# def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv

# 协程 新方法  推荐使用
async def init(lp):
    app = web.Application(loop=lp)
    app.router.add_route('GET', '/', index)
    srv = await lp.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
