'''
List Comprehension is a way to construct a new Python list from an iterable types: lists, 
tuples, and strings. All without using a for loop or the `.append()` list method.
'''
'''
In this project, you are going to build a program that takes a camelCase or PascalCase 
formatted string as input and converts that to a snake_case formatted string using two 
approaches. First, you'll use a for loop and then list comprehension to achieve the same 
results. You'll see how list comprehension can make your code more concise.

Start defining a new function named convert_to_snake_case() that accepts a string named 
pascal_or_camel_cased_string as input. For now, add a pass statement inside the function.
'''
# camelCase | PascalCase | snake_case

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    # NOTE: In list comprehension, there is no need to worry for appending the character back to to the list as 
    # the loop it self is already inserted within the list and action 'accordingly' on every itteration. 
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()