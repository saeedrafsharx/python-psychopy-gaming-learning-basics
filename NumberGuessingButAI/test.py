def generate_initial(full_string):
    """Generate an initial using first symbol.
    
    Parameters
    ----------
    full_string : str
    
    Returns
    ----------
    str : single symbol
    """
    return full_string[0]

...
initial = generate_initial("test")
...
initial_for_file = generate_initial(filename)
...
initial_for_website = generate_initial(first_name)
...