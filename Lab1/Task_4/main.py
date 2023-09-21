def generate_html_table(num_rows: int) -> str:
    """This function takes the number of rows and returns a string
    that represents an HTML code for the <table> that creates gradient on the page.

    :param num_rows: number of rows in the table
    :return: string representing contents of `.html` file with the table
    """
    html = "<body style='margin: 0'>\n\t<table style='border-spacing: 0; width: 100vw; height: 100vh'>"

    for i in range(num_rows):
        alpha = float(i) / num_rows
        html += f"\n\t\t<tr style='height: {1. / num_rows}px; background-color: rgba(0, 0, 0, {alpha})'><td></td></tr>"

    html += "\n\t</table>\n</body>"

    return html


def main():
    n_rows: int = 300
    html_table: str = generate_html_table(n_rows)

    with open("gradient_table.html", "w+") as f:
        f.write(html_table)


if __name__ == "__main__":
    main()
