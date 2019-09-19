import aiohttp_jinja2
import jinja2
from aiohttp import web
from pathlib import Path

from services.romans.src.utils.roman import Roman
from services.gen_pwd.src.utils.password_generator import Generator
from services.classifiy_pwd.src.utils.classifier import Classifier
from services.gen_hash.src.utils.hash_generator import HashGenerator
from services.cpf_validate.src.utils.validator import Validator
from services.zero_distance.src.utils.counter import Counter


class Setup:

    def __init__(self):
        self.app = web.Application()
        self.templates = '{}/templates'.format(Path(__file__).parent)
        aiohttp_jinja2.setup(app=self.app, loader=jinja2.FileSystemLoader([self.templates]))

        self.app.router.add_route('GET', '/', Wrapper.home)
        self.app.router.add_route('GET', '/zero_distance', Wrapper.zero_distance_page)
        self.app.router.add_route('GET', '/zero_distance_resp/{string}', Wrapper.zero_distance_response)
        self.app.router.add_route('GET', '/roman', Wrapper.romans_page)
        self.app.router.add_route('GET', '/roman_resp/{number}', Wrapper.romans_response)
        self.app.router.add_route('GET', '/gen_pwd', Wrapper.gen_pwd_page)
        self.app.router.add_route('GET', '/gen_pwd_resp', Wrapper.gen_pwd_response)


class Wrapper:

    @classmethod
    @aiohttp_jinja2.template(template_name='index.html')
    async def home(cls, request):
        return {'app': request.app}

    @classmethod
    @aiohttp_jinja2.template(template_name='roman.html')
    async def romans_page(cls, request):
        return {'app': request.app}

    @classmethod
    @aiohttp_jinja2.template(template_name='roman_response.html')
    async def romans_response(cls, request):
        number = request.match_info.get('number')
        return {'app': request.app,
                'result': Roman.convert_digits(number=number)}

    @classmethod
    @aiohttp_jinja2.template(template_name='zero_dist.html')
    async def zero_distance_page(cls, request):
        return {'app': request.app}

    @classmethod
    @aiohttp_jinja2.template(template_name='zero_dist_response.html')
    async def zero_distance_response(cls, request):
        return {'app': request.app,
                'result': Counter.count_zeroes(string=request.match_info.get('string'))}

    @classmethod
    @aiohttp_jinja2.template(template_name='gen_pwd.html')
    async def gen_pwd_page(cls, request):
        return {'app': request.app}

    @classmethod
    @aiohttp_jinja2.template(template_name='gen_pwd_resp.html')
    async def gen_pwd_response(cls, request):
        pwd = Generator.generate()
        _class = Classifier.classify(pwd=pwd)
        md5_hash = HashGenerator.generate_md5(string=pwd)
        sha_hash = HashGenerator.generate_sha256(string=pwd)

        strength = {0: 'Weak',
                    1: 'Good',
                    2: 'Strong'}

        return {'app': request.app,
                "password": pwd,
                "class": strength[_class],
                "md5": md5_hash,
                "sha_256": sha_hash}

    @classmethod
    @aiohttp_jinja2.template(template_name='')
    async def validate_cpf(cls, request):
        cpf = request.match_info.get('cpf')
        return web.Response(text=str(Validator.validate(input_string=cpf)))