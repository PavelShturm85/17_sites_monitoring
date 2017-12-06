import requests
import sys
import argparse
from datetime import datetime
from whois import whois


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module for check sites health.')
    parser.add_argument(
        'domain_file', help='Where get file with domain.')
    parser.add_argument(
        '-d', '--days', default=30, type=int,
        help='Input days before expiration.')
    return parser


def load_urls4check(domain_file):
    with open(domain_file, 'r') as urls4check:
        return urls4check.read().splitlines()


def is_server_respond_with_200(domain_list):
    server_respond_with_200_list = []
    for url in domain_list:
        code = requests.get(url).status_code
        if code == 200:
            server_respond_with_200_list.append(url)
    return server_respond_with_200_list


def get_domain_expiration_normal(domain_list, days_before_expiration):
    domain_expiration_normal = []
    for url in domain_list:
        delta = whois(url).expiration_date - datetime.now()
        if delta.days >= days_before_expiration:
            domain_expiration_normal.append(url)
    return domain_expiration_normal


def print_health_domain(domains_list, domain_properties):
    for url in domains_list:
        print('Domain:{} {}!'.format(url, domain_properties))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    domain_file = load_urls4check(namespace.domain_file)
    expiration_normal = get_domain_expiration_normal(
        domain_file, namespace.days)
    respond_200 = is_server_respond_with_200(domain_file)

    actualy_domain = list(set(expiration_normal) & set(respond_200))
    expiration_not_normal = list(set(domain_file) - set(expiration_normal))
    not_respond_200 = list(set(domain_file) - set(respond_200))

    print_health_domain(actualy_domain, 'is OK')
    print_health_domain(expiration_not_normal,
                        'has problem with expiration date')
    print_health_domain(not_respond_200, 'is NOT ok')
