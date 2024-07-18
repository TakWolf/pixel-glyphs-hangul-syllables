from tools.configs import path_define, FontSize


def make_patterns(font_size: FontSize):
    outputs_dir = path_define.outputs_dir.joinpath(str(font_size), 'AC00-D7AF Hangul Syllables')
    outputs_dir.mkdir(parents=True, exist_ok=True)
