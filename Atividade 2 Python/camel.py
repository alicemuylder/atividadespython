def camel_to_snake(variable_name):
    snake_case = [variable_name[0].lower()]
    for char in variable_name[1:]:
        if char.isupper():
            snake_case.append('_')
            snake_case.append(char.lower())
        else:
            snake_case.append(char)
    return ''.join(snake_case)

def main():
    variable_name_camel = input("Digite o nome da variável em Camel Case: ")
    variable_name_snake = camel_to_snake(variable_name_camel)

    print(f"Nome da variável em Snake Case: {variable_name_snake}")

if __name__ == "__main__":
    main()