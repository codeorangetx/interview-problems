# !/usr/bin/python

'''
2016 KPCB Engineering Fellows Program Application

Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). 
Your data structure should be optimized for algorithmic runtime and memory usage. 
You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

If your language provides a built-in hashing function for strings (ex. `hashCode` in Java or `__hash__` in Python) you are welcome to use that. 
If not, you are welcome to do something naive, or use something you find online with proper attribution.
'''

class HashMap(object):
    """docstring for HashMap"""
    def __init__(self, arg):
        super(HashMap, self).__init__()
        self.arg = arg

    def set(key, value):
        '''
        Returns an instance of the class with pre-allocated space for the given number of objects
        '''
        return

    def get(key):
        '''
        Returns the value associated with the given key, or null if no value is set.
        '''
        return

    def delete(key): 
        '''
        Deletes the value associated with the given key, returning the value on success or null if the key has no value.
        '''
        return

    def load(): 
        '''
        Returns a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. 
        Since the size of the dat structure is fixed, this should never be greater than 1.
        '''

