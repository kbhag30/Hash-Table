# Hash-Table

Hash Table Implementation

Description

This project implements a hash table from scratch using Python. A hash table is a data structure that stores information as key-value pairs and uses a hashing function to efficiently organize and retrieve data.

The implementation uses a custom hashing function that calculates a hash value by summing the Unicode values of each character in a string key.

Features

Custom Hash Function: Uses Python's ord() function to calculate the sum of the Unicode values of a string's characters.

Add Key-Value Pairs: Stores key-value pairs in a dictionary organized by their hash values.

Collision Handling: Supports multiple keys that produce the same hash value by storing them in a shared nested dictionary.

Lookup Values: Retrieves a value associated with a specified key.

Remove Entries: Removes a key-value pair without raising an error if the key does not exist.

Missing-Key Handling: Returns None when a requested key cannot be found.

