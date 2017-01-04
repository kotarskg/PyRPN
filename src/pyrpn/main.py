# -*- coding: utf-8 -*-

import argparse

from pyrpn import rpn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("eval", nargs='+', help='expression to be evaluated')
    args = parser.parse_args()
    value = rpn.eval_rpn(args.eval)
    print(value)

if __name__ == '__main__':
    main()