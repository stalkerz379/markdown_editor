class FormatterBase:

    def __init__(self, name: str, format_: str):
        self.name = name
        self.format_ = format_  # format_ basically expect a string in a format of e.g. regex r".*%str.*"

    def __format__(self) -> str:
        """Method will take a given format and find %str pattern and replace all occurrences with a string.
        Return new string in a given format. E.g. format is "**%str**" (bold text), string "bold text" -
        method will return "**bold text**" as a result"""
        string = input('Text: ').strip()
        formatted_string = self.format_.replace("%str", string)
        return formatted_string


class PlainTextFormatter(FormatterBase):
    def __format__(self):
        string = input('Text: ')
        formatted_string = self.format_.replace("%str", string)
        return formatted_string


class BoldFormatter(FormatterBase):
    pass


class ItalicFormatter(FormatterBase):
    pass


class InlineCodeFormatter(FormatterBase):
    pass


class LinkFormatter(FormatterBase):
    def __format__(self):
        label = input('Label: ')
        url = input('URL: ')
        return f"[{label}]({url})"


class HeaderFormatter(FormatterBase):
    def __format__(self):
        try:
            header_lvls = {1: '#', 2: '##', 3: '###', 4: '####', 5: '#####', 6: '######'}
            lvl = int(input('Level: '))
            if lvl not in header_lvls.keys():
                raise ValueError
            string = input("Text: ")
            return f"{self.format_.replace('%str', lvl * '#')} {string}\n"
        except ValueError:
            print('The level should be within the range of 1 to 6')
            return self.__format__()


class NewLineFormatter(FormatterBase):
    def __format__(self):
        return self.format_    # this method will return the \n given in the format attribute, overwrites parent method


class OrderListFormatter(FormatterBase):
    def __format__(self):
        formatted_text = ""
        try:
            rows = int(input('Number of rows: '))
            if rows <= 0:
                raise ValueError
            for row in range(1, rows + 1):
                user_str = input(f'Row #{row}: ')
                formatted_text += f'{row}. {user_str}\n'
            return formatted_text
        except ValueError:
            print("The number of rows should be greater than zero")
            return self.__format__()


class UnorderedListFormatter(FormatterBase):
    def __format__(self):
        formatted_text = ""
        try:
            rows = int(input('Number of rows: '))
            if rows <= 0:
                raise ValueError
            for row in range(1, rows + 1):
                user_str = input(f'Row #{row}: ')
                formatted_text += f'* {user_str}\n'
            return formatted_text
        except ValueError:
            print("The number of rows should be greater than zero")
            return self.__format__()


class MarkdownEditor:
    SPECIAL_OPTIONS = ['!help', '!done']

    def __init__(self):
        self.file_path = 'output.md'
        self.formatters = {}
        self.buffer = []

    def add_formatter(self, formatters: list[FormatterBase]) -> None:
        for formatter in formatters:
            if isinstance(formatter, FormatterBase):
                self.formatters.setdefault(formatter.name, formatter)
            else:
                print(f'Sorry, the formatter should be an instance of <class FormatterBase>. Given {type(formatter)}')

    def write(self) -> None:
        with open(self.file_path, 'w+', encoding='utf-8') as f_out:
            for line in self.buffer:
                print(line, sep='', end='', file=f_out)
        exit()

    def help(self):
        print('Available commands:', *self.formatters.keys())
        print('Special commands:', *MarkdownEditor.SPECIAL_OPTIONS)

    def get_formatter(self, formatter_name: str) -> FormatterBase:
        return self.formatters.get(formatter_name)

    def menu(self):
        optns = {'!done': self.write, '!help': self.help}
        options = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'new-line', 'ordered-list',
                   'unordered-list']
        user_option = input('Choose a formatter: ').strip().lower()
        if user_option in options:
            formatter = self.get_formatter(user_option)
            formatted_text = formatter.__format__()
            self.buffer.append(formatted_text)
            print(*self.buffer, sep='')
        elif user_option in MarkdownEditor.SPECIAL_OPTIONS:
            optns.get(user_option)()
        else:
            print('Unknown formatting type or command')


def setup_formatters() -> list[FormatterBase]:
    plain_text_formatter = PlainTextFormatter(name='plain', format_="%str")
    bold_text_formatter = BoldFormatter(name='bold', format_="**%str**")
    italic_formatter = ItalicFormatter(name='italic', format_='*%str*')
    inline_code_formatter = InlineCodeFormatter(name='inline-code', format_='`%str`')
    new_line_formatter = NewLineFormatter(name='new-line', format_='\n')
    header_formatter = HeaderFormatter(name='header', format_='%str')
    ordered_list_formatter = OrderListFormatter(name='ordered-list', format_='1 %str')
    unordered_list_formatter = UnorderedListFormatter(name='unordered-list', format_='* %str')
    link_formatter = LinkFormatter(name='link', format_='[%str](%str)')
    formatters = [plain_text_formatter, bold_text_formatter, italic_formatter, inline_code_formatter,
                  new_line_formatter, header_formatter, link_formatter, unordered_list_formatter,
                  ordered_list_formatter]
    return formatters


if __name__ == "__main__":
    formatters = setup_formatters()
    editor = MarkdownEditor()
    editor.add_formatter(formatters)
    while True:
        editor.menu()

