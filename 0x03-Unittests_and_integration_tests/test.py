#!/usr/bin/python3

access_nested_map = __import__('utils').access_nested_map

n = {"a": 1}
path=("a",)
print(access_nested_map(n, path))

n={"a": {"b": 2}}
path=("a",)
print(access_nested_map(n, path))

n={"a": {"b": 2}}
path=("a", "b")
print(access_nested_map(n, path))
