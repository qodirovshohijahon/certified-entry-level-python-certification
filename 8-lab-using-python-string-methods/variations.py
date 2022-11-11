#!/usr/bin/env python3

message = input("Enter a message: ")
print(f"Lowercase: {message.lower()}")
print(f"Uppercase: {message.upper()}")
print(f"Capitalized: {message.capitalize()}")
print(f"Title Case: {message.title()}")
splitted_message = message.split()
print("Words: ", splitted_message)
alph_first_word = splitted_message.sort()
print("Alphabetic First Word:", splitted_message[0])
print("Alphabetic Last Word:", splitted_message[-1])
