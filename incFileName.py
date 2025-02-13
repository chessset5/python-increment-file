def increment_filename(file_path: str, template: str = " ({counter})") -> str:
    """
    increment_filename increments given file

    Args:
        file_path (str): path to file
        template (str): python template. Please use `counter` for the increment argument<br>
            Defaults to " ({counter})".<br>
            ex: `' ({counter:03})'` to pad left with zeros.

    Returns:
        str: new file path
    """
    # Split the file path into directory, base name, and extension
    directory, base_name = os.path.split(file_path)
    name, ext = os.path.splitext(base_name)

    # Initialize the counter
    counter: int = 1

    # Generate new file name with increment
    while os.path.exists(file_path):
        increment: str = template.replace("{counter}", str(counter))
        new_name: str = f"{name}{increment}{ext}"
        file_path = os.path.join(directory, new_name)
        counter += 1
    return file_path
