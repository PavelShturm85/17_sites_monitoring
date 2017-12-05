import requests
import sys
from datetime import datetime
from whois import whois


def load_urls4check(enter_file):
    with open(enter_file, 'r') as urls4check:
        return urls4check.read().splitlines()


def is_server_respond_with_200(domain_list):
    server_respond_with_200_list = []
    for url in domain_list:
        code = requests.get('{}'.format(url)).status_code
        if code == 200:
            server_respond_with_200_list.append(url)
    return server_respond_with_200_list


def get_domain_expiration_normal(domain_list):
    domain_expiration_normal = []
    for url in domain_list:
        delta = whois(url).expiration_date - datetime.now()
        if delta.days >= 30:
            domain_expiration_normal.append(url)
    return domain_expiration_normal


def print_result(domains_list, domain_properties):
    for url in domains_list:
        print('Domain:{} {}!'.format(url, domain_properties))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')

    enter_file = load_urls4check(input_file_name)
    expiration_normal = get_domain_expiration_normal(enter_file)
    respond_200 = is_server_respond_with_200(enter_file)

    actualy_domain = list(set(expiration_normal) & set(respond_200))
    expiration_not_normal = list(set(enter_file) - set(expiration_normal))
    not_respond_200 = list(set(enter_file) - set(respond_200))

    print_result(actualy_domain, 'is OK')
    print_result(expiration_not_normal, 'has problem with expirationdate')
    print_result(not_respond_200, 'is NOT ok')
