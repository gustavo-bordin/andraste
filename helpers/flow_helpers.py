def _convert_class_to_kebab(class_name):
    converted_name = ''

    for index, character in enumerate(class_name):
        if character.isupper() and index != 0 and class_name[index - 1].islower():
            converted_name  += f'-{character}'
        else:
            converted_name += character

    return converted_name.lower()
        
def get_queue_name(crawler_class):
    class_name = crawler_class.__name__
    class_kebab_case = _convert_class_to_kebab(class_name)
    queue_name = f"{class_kebab_case}.inputs"

    return queue_name