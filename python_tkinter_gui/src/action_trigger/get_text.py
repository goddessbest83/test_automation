import yaml


def get_text(text_box):
    text_box = {text_box : text_box.get()}
    with open('personal.yaml', 'w') as ym:
        yaml.dump(text_box(), ym)