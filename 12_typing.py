from typing import TypeAlias

Int: TypeAlias = int

def process_user(num: Int):
    print(f'processing {num}')

process_user('Alice')


