import click
import yaml


def print_strings(yaml_file):
    for dct in yaml_file:
        for k, v in dct.items():
            print(f"Parameters value {k}, {v}")


@click.command()
@click.option("--write-to-file", "-w", type=click.File("w"))
@click.option("--yaml-file", "-y", type=click.File("r"), required=True)
def main(yaml_file, write_to_file):

    # just for testing
    file_title = click.prompt("Enter title of new file", type=click.Choice([
        'My title', 'My title 1']))
    write_to_file.write(f"{file_title}\n\n")
    clean = click.confirm("вывести содержимое файла очистив экран?")

    if clean:
        click.clear()

    yf = yaml.safe_load(yaml_file)
    print_strings(yf)
    for elem in yf:
        for k, v in elem.items():
            write_to_file.write(f"{v}: {k} \n")


if __name__ == "__main__":
    main()
