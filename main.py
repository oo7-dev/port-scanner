import argparse
import socket
import time
from scanner import scan_ports
from banner import grab_banner
from colorama import Fore, init

init(autoreset=True)


def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except:
        print(Fore.RED + "Invalid domain or IP")
        return None


def main():
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("-p", "--ports", required=True, help="Port range (example: 1-100)")
    parser.add_argument("-o", "--output", help="Save results to file")

    args = parser.parse_args()

    target = args.target
    port_range = args.ports
    output_file = args.output

    try:
        start_port, end_port = map(int, port_range.split("-"))
    except:
        print(Fore.RED + "Invalid port range format. Use start-end (example: 1-100)")
        return

    ip = resolve_target(target)

    if not ip:
        return

    print(Fore.YELLOW + f"\nScanning {target} ({ip}) from port {start_port} to {end_port}...\n")

    start_time = time.time()

    open_ports = scan_ports(ip, start_port, end_port)
    results = []

    if open_ports:
        print(Fore.GREEN + "Open Ports Found:\n")

        for port in open_ports:
            print(Fore.GREEN + f"[OPEN] Port {port}")
            banner = grab_banner(ip, port)

            if banner == "No banner available":
                info = f"Port {port}: OPEN | Banner not detected"
                print(Fore.RED + "Service Info: Banner not detected")
            else:
                info = f"Port {port}: OPEN | {banner[:100]}"
                print(Fore.CYAN + f"Service Info: {banner[:100]}")

            results.append(info)
            print()

    else:
        print(Fore.RED + "No open ports found.")

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print(Fore.YELLOW + f"\nScan completed in {duration} seconds")
    print(Fore.YELLOW + f"Total open ports: {len(open_ports)}")

    # Save to file if requested
    if output_file:
        try:
            with open(output_file, "w") as f:
                f.write(f"Scan results for {target} ({ip})\n")
                f.write(f"Port range: {start_port}-{end_port}\n")
                f.write(f"Scan time: {duration} seconds\n\n")

                for line in results:
                    f.write(line + "\n")

            print(Fore.YELLOW + f"Results saved to {output_file}")

        except:
            print(Fore.RED + "Error saving results to file")


if __name__ == "__main__":
    main()