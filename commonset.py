import sys

def main(text, **kwargs):
    set_a = set(sys.argv[1:])
    set_b = set(['apple', 'banana', 'mango', 'orange'])
    
    for i in text:
        print(set_a & set_b)
    
    
main(sys.argv[1:])
