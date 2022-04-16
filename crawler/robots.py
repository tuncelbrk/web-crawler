import pandas as pd


def get_sitemaps(robots):
    """Parse a robots.txt file and return a Python list containing any sitemap URLs found.

    Args:
        robots (string): Contents of robots.txt file.

    Returns:
        data (list): List containing each sitemap found.
    """

    data = []
    lines = str(robots).splitlines()

    for line in lines:
        if line.startswith('Sitemap:'):
            split = line.split(':', maxsplit=1)
            data.append(split[1].strip())

    return data


def to_dataframe(robots):
    """Parses robots.txt file contents into a Pandas DataFrame.

    Args:
        robots (string): Contents of robots.txt file.

    Returns:
        df (list): Pandas dataframe containing robots.txt directives and parameters.
    """

    data = []
    lines = str(robots).splitlines()
    for line in lines:

        if line.strip():
            if not line.startswith('#'):
                split = line.split(':', maxsplit=1)
                data.append([split[0].strip(), split[1].strip()])

    return pd.DataFrame(data, columns=['directive', 'parameter'])
