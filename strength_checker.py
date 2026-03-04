#!/usr/bin/env python3

import string
import secrets
import argparse


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "WEAK"
    elif score == 3:
        return "MEDIUM"
    else:
        return "STRONG"


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def banner():
    print("""
====================================
        PASSWORD SECURITY TOOL
====================================
Check password strength or generate
secure random passwords
====================================
""")


def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker and Generator")

    parser.add_argument("-c", "--check", help="Check password strength")
    parser.add_argument("-g", "--generate", type=int, help="Generate secure password (length)")

    args = parser.parse_args()

    banner()

    if args.check:
        strength = check_strength(args.check)
        print(f"[+] Password: {args.check}")
        print(f"[+] Strength : {strength}")

    elif args.generate:
        password = generate_password(args.generate)
        print(f"[+] Generated Password: {password}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()