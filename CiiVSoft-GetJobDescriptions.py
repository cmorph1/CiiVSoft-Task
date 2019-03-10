import http.client
import base64
import codecs


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
    data = str(connect_and_get('ciivsoft.getsandbox.com', '/jobs'))
    strings = data.split('"')
    jd1_code = strings[7]
    jd2_code = strings[9]
    jd1, jd2 = base64.b64decode(jd1_code).decode('utf-8'), base64.b64decode(jd2_code).decode('utf-8')
    write_job_description('job description 1.txt', jd1)
    write_job_description('job description 2.txt', jd2)
