from tools import configs
from tools.services import format_service


def main():
    for font_size in configs.font_sizes:
        format_service.format_parts(font_size)


if __name__ == '__main__':
    main()
