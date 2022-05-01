import subprocess
import click


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return string is reachable
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        print("ok")  # return True
    else:
        print("not ok")  # return False


def ping_ip_addresses(ip_addresses, count):
    ok = []
    not_ok = []
    with click.progressbar(ip_addresses, label="Pinging IP-addresses") as bar:
        for ip in bar:
            if ping_ip(ip, count):
                ok.append(ip)
            else:
                not_ok.append(ip)
    return ok, not_ok


@click.command()
@click.argument("ip_addresses", nargs=-1, required=True)
@click.option(
    "--count",
    "-c",
    default=3,
    help="Number ICMP requests",
    type=click.IntRange(1, 10),
    show_default=True,
)
def main(ip_addresses, count):
    """
    Ping IP_ADDRESS and return string is reachable
    """
    print(ip_addresses, count)
    ok, not_ok = ping_ip_addresses(ip_addresses, count)
    for ip in ok:
        print(f"IP-адрес {ip:15} пигнуется")
    for ip in not_ok:
        print(f"IP-адрес {ip:15} не пигнуется")


if __name__ == "__main__":
    main()
