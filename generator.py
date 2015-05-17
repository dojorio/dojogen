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


join = lambda a, b: os.path.join(os.path.abspath(a), b)


def sprint(text, show):
    if show:
        print(text)


def list_to_args(args, show=True):
    opts = args.split(' ')
    if len(opts) < 2:
        raise GENERATOR_MESSAGES['error']
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
            os.path.dirname(__file__), "generators/%s/" %(self.language))

        splitted_name =  self.problem.split('_')

        snake_case = self.problem
        pascal_case = ''.join(part.capitalize() for part in splitted_name)
        down_case = ''.join(splitted_name)
        camel_case = (
            splitted_name.pop(0) +
            ''.join(part.capitalize() for part in splitted_name)
        )

        self.cases = {
            '#_#dojotools#_#' : snake_case,
            '#_#class_dojotools#_#' : pascal_case,
            '#_#down_dojotools#_#' : down_case,
            '#_#camel_dojotools#_#' : camel_case,
        }


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
                raise GENERATOR_MESSAGES['lang_error'] % (self.language)
        else:
            self.generated = True
            raise GENERATOR_MESSAGES['exists']


    def generated(self):
        return ((not self.errors) or self.messages['exists'] in self.errors)


def generate(generate, directory):
    if generate:
        generator = Generator(list_to_args(generate))
        try:
            generator.generate()
        finally:
            if generator.generated:
                return generator.folder_path
    return directory


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Generates directory for coding dojo following the pattern:
            {}[_extra]_language_problem\n'''.format(TODAY))
    parser.add_argument('language', type=str,
                        help='Programming Language')
    parser.add_argument('problem', type=str,
                        help='Problem Name')
    parser.add_argument('extra', type=str, nargs='*', default='',
                        help='Extra identifier')
    args = parser.parse_args()
    generator = Generator(args)
    generator.generate()
