#!/usr/bin/env python
# coding: utf-8
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

from datetime import datetime
import os
import sys
import re
import argparse


TODAY = datetime.today().strftime("%Y%m%d")
GENERATOR_MESSAGES = {
    'error': 'Generator failed to generate files',
    'message': "Generating Folder...",
    'lang': "Language found: %s",
    'lang_error': "%s generator wasn't found",
    'exists': "Dojo path already exists!",
}


class GeneratorException(Exception):
    value = GENERATOR_MESSAGES['error']
    def __str__(self):
        return repr(self.value)


class GeneratorNotFoundError(GeneratorException):
    def __init__(self, language):
        self.value = GENERATOR_MESSAGES['lang_error'] % language


class GeneratorPathExistsError(GeneratorException):
    value = GENERATOR_MESSAGES['exists']


join = lambda a, b: os.path.join(os.path.abspath(a), b)


def sprint(text, show):
    if show:
        print(text)


def list_to_args(args, show=True):
    opts = args.split(' ')
    if len(opts) < 2:
        raise GeneratorException()
    n = argparse.Namespace()
    n.language, n.problem = opts[:2]
    n.extra = opts[2:]
    return n


class Generator(object):

    def __init__(self, args):
        self.language = args.language
        self.problem = args.problem
        self.extra =  ('_' + '_'.join(args.extra)) if args.extra else ''

        self.today = TODAY

        self.folder_name = "{date}{_extra}_{language}_{problem}".format(
            date=TODAY,
            _extra=self.extra,
            language=self.language,
            problem=self.problem,
        )

        self.folder_path = join(os.path.curdir, self.folder_name)
        self.generator_path = join(
            os.path.dirname(__file__), "generators/%s/" % (self.language))

        splitted_name =  self.problem.split('_')

        snake_case = self.problem
        pascal_case = ''.join(part.capitalize() for part in splitted_name)
        down_case = ''.join(splitted_name)
        camel_case = (
            splitted_name.pop(0) +
            ''.join(part.capitalize() for part in splitted_name)
        )

        self.cases = {
            '#_#dojogen#_#' : snake_case,
            '#_#class_dojogen#_#' : pascal_case,
            '#_#down_dojogen#_#' : down_case,
            '#_#camel_dojogen#_#' : camel_case,
        }

        self.generated = False


    def replace(self, text):
        for sub, replace in self.cases.iteritems():
            text = re.sub(sub, replace, text)
        return text

    def copy_and_rename(self, current, folder_name, original):
        isdir = lambda x: os.path.isdir(x) and not os.path.islink(x)

        folder_path = join(current, folder_name)
        os.mkdir(folder_path)
        file_list = os.listdir(original)
        for infile in file_list:
            gen_path = join(original, infile)
            if isdir(gen_path):
                self.copy_and_rename(folder_path, infile, gen_path)
            else:
                new_path = join(folder_path,self.replace(infile))
                with open(new_path, 'w') as w:
                    with open(gen_path, 'r') as r:
                        for line in r:
                            w.write(self.replace(line))

    def generate(self, show=True):
        if not os.path.exists(self.folder_path):
            sprint(GENERATOR_MESSAGES['message'], show)

            if os.path.exists(self.generator_path):
                sprint(GENERATOR_MESSAGES['lang'] % (self.language), show)
                self.copy_and_rename(
                    os.path.curdir, self.folder_name, self.generator_path)
                self.generated = True
            else:
                raise GeneratorNotFoundError(self.language)
        else:
            self.generated = True
            raise GeneratorPathExistsError()



def generate(generate, directory):
    if generate:
        generator = Generator(list_to_args(generate))
        try:
            generator.generate()
        finally:
            if generator.generated:
                return generator.folder_path
    return directory


def generate_mode(args):
    generator = Generator(args)
    generator.generate()


def help_mode(args):
    help_path = join(
        os.path.dirname(__file__), "generators/help/%s" % (args.language))
    if os.path.exists(help_path):
        with open(help_path, 'r') as f:
            print(f.read())
    else:
        raise GeneratorNotFoundError(args.language)


def lang_mode(args):
    gens = join(os.path.dirname(__file__), "generators/")
    for name in os.listdir(gens):
        if os.path.isdir(join(gens, name)) and name != 'help':
            print(name)

if __name__ == '__main__':

    gen_msg = '''Generates directory for coding dojo following the pattern:
        {}[_extra]_language_problem\n'''.format(TODAY)
    help_msg = 'Describes how to prepare the environment for a language'
    lang_msg = 'Shows existing generators'
    dgen_msg, dhelp_msg, dlang_msg = gen_msg, help_msg, lang_msg

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    for name in ['generate', 'gen', 'g']: # Aliases on Python 2.x
        parser_gen = subparsers.add_parser(
            name, description=gen_msg, help=dgen_msg)
        parser_gen.add_argument(
            'language', type=str, help='Programming Language')
        parser_gen.add_argument(
            'problem', type=str, help='Problem Name')
        parser_gen.add_argument(
            'extra', type=str, nargs='*', default='', help='Extra identifier')
        parser_gen.set_defaults(func=generate_mode)
        dgen_msg = '...'

    for name in ['help', 'man', 'h']: # Aliases on Python 2.x
        parser_help = subparsers.add_parser(
            name, description=help_msg, help=dhelp_msg)
        parser_help.add_argument(
            'language', type=str, help='Programming Language')
        parser_help.set_defaults(func=help_mode)
        dhelp_msg = '...'

    for name in ['language', 'l']: # Aliases on Python 2.x
        parser_lang = subparsers.add_parser(
            name, description=lang_msg, help=dlang_msg)
        parser_lang.set_defaults(func=lang_mode)
        dlang_msg = '...'

    args, _ = parser.parse_known_args()
    try:
        args.func(args)
    except GeneratorException as err:
        print("Error: {0}".format(err))
