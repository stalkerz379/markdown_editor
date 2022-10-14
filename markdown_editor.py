def markdown_editor_options():
    options = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'new-line', 'ordered-list', 'unordered-list']
    special_options = ['!help', '!done']
    return options, special_options


def plain_text():
    string = input("Text: ")
    formatted_text = string
    return formatted_text


def bold_text():
    string = input("Text: ")
    formatted_text = f'**{string }**'
    return formatted_text


def italic_text():
    string = input("Text: ")
    formatted_text = '*' + string + '*'
    return formatted_text


def inline_code():
    string = input("Text: ")
    formatted_text = '`' + string + '`'
    return formatted_text


def link():
    label = input('Label: ')
    url = input('URL: ')
    formatted_text = f'[{label}]({url})'
    return formatted_text


def header():
    try:
        header_lvls = {1: '#', 2: '##', 3: '###', 4: '####', 5: '#####', 6: '######'}
        lvl = int(input('Level: '))
        if lvl not in header_lvls.keys():
            raise ValueError
        string = input("Text: ")
        formatted_text = header_lvls[lvl] + ' ' + string + '\n'
        return formatted_text
    except ValueError:
        print('The level should be within the range of 1 to 6')
        return header()


def new_line():
    formatted_text = '\n'
    return formatted_text


def making_list(option):
    formatted_text = []
    counter = 1
    marker = 1 if option == 'ordered-list' else '*'
    try:
        rows = int(input('Number of rows: '))
        if rows <= 0:
            raise ValueError
        for row in range(rows):
            ask_list_element = input(f'Row #{counter}: ')
            formatted_text.append(f'{str(marker) if marker == "*" else str(marker) + "."} {ask_list_element}\n')
            if option == 'ordered-list':
                marker += 1
            else:
                marker = '*'
            counter += 1
    except ValueError:
        print("The number of rows should be greater than zero")
        return making_list(option)
    return formatted_text


def done(formatted_text):
    output_file = open('output.md', 'w+', encoding='utf-8')
    for line in formatted_text:
        output_file.write(line)
    output_file.close()


def choosing_function(option, whole_text):
    if option == 'plain':
        formatted_text = plain_text()
    elif option == 'bold':
        formatted_text = bold_text()
    elif option == 'italic':
        formatted_text = italic_text()
    elif option == 'inline-code':
        formatted_text = inline_code()
    elif option == 'link':
        formatted_text = link()
    elif option == 'header':
        formatted_text = header()
    elif option == 'new-line':
        formatted_text = new_line()
    elif option == 'ordered-list' or option == 'unordered-list':
        formatted_text = making_list(option)
        whole_text.extend(formatted_text)
        return whole_text
    whole_text.append(formatted_text)
    return whole_text


def main():
    options, special_options = markdown_editor_options()
    whole_text = []
    while True:
        user_option = input('Choose a formatter: ')
        if user_option in options:
            whole_text = choosing_function(user_option, whole_text)
            for item in whole_text:
                print(item, end='')
            print()
        elif user_option == '!help':
            print('Available formatters:', *options)
            print('Special commands:', *special_options)
        elif user_option == '!done':
            done(whole_text)
            exit()
        else:
            print('Unknown formatting type or command')

if __name__ == '__main__':
    main()
