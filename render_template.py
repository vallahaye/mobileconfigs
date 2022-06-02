#!/usr/bin/env python3

import ast
import base64
import sys

import jinja2
from dotenv import dotenv_values


def b64encode(s: str) -> str:
  return base64.b64encode(s.encode('utf-8')).decode('utf-8')


def main():
  if len(sys.argv) < 2:
    sys.exit('fatal error: no template file')
  env = dotenv_values('.env')
  tmpl_loader = jinja2.FileSystemLoader('.')
  tmpl_env = jinja2.Environment(loader=tmpl_loader, autoescape=True)
  tmpl_env.filters['b64encode'] = b64encode
  tmpl = tmpl_env.get_template(sys.argv[1])
  tmpl_vars = {}
  for name, val in env.items():
    if name.endswith('[]'):
      name = name[:-2]
      try:
        val = ast.literal_eval(val)
        if not isinstance(val, list):
          raise ValueError('not a list')
      except (SyntaxError, ValueError):
        sys.exit(f'fatal error: the variable {name} must be a list literal')
    name = name.lower()
    tmpl_vars[name] = val
  print(tmpl.render(**tmpl_vars))


if __name__ == '__main__':
  main()
