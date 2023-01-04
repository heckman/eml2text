#!/usr/bin/env python3

# eml2text
# v0.1
#
# takes the name of an eml file as its only argument
# and prints the body of the email as plain-text to stdout

from email import policy,  message_from_file
from sys import argv, exit, stderr

def read_message(fp):
    return message_from_file(fp, policy=policy.default)

def headers_of_message(message):
    return (
        f'Date: {message["date"]}\n'
        f'From: {message["from"]}\n'
        f'To: {message["to"]}\n'
        f'Subject: {message["subject"]}\n'
    )

def body_of_message(message):
    return message.get_body(preferencelist=('plain',)).get_content()

def format_message(message):
    return '\n'.join((
            headers_of_message(message),
            body_of_message(message)
        ))

try:
    with open(argv[1]) as fp:
        print(format_message(read_message(fp)))
except OSError as e:
    print(f"Unable to open {argv[1]}", file=stderr)
    exit(1)
except IndexError as e:
    print(F"Usage: {argv[0]} <EML_FILE>")
    exit(1)
