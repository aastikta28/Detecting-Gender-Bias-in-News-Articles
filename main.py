# -*- coding: utf-8 -*-
import extract_names_from_json

def main():
    user_input = input("Enter year: ")
    extract_names_from_json.extract_json(str(user_input))
    
if __name__ == '__main__':
    main()
