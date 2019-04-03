import http.client
import base64
import codecs
import json


def connect_and_get(domain: str, path: str):
    conn = http.client.HTTPConnection(domain)
    headers = {'Content-type': 'application/json'}
    conn.request("GET", path, headers=headers)
    rs = conn.getresponse()
    source = rs.read()
    return source


def write_job_description(name: str, utf_file):
    file = codecs.open(name, "w", encoding="utf-8")
    file.write(utf_file)
    file.close()


if __name__ == '__main__':
    data = json.loads(connect_and_get('ciivsoft.getsandbox.com', '/jobs'))
    file_number = 1
    for job_descriptions in data['result']:
        write_job_description('job description {}.txt'.format(file_number),
                              (base64.b64decode(job_descriptions).decode('utf-8')))
        file_number += 1
