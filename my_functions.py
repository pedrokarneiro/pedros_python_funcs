# My Python functions.
# Not tested yet.

# Returns status message based on the given status code.
def get_mensage(my_status_code):
    if my_status_code == 100: my_mensage = 'CONTINUE'
    elif my_status_code == 101: my_mensage = 'SWITCHING PROTOCOLS'
    elif my_status_code == 200: my_mensage = 'OK'
    elif my_status_code == 201: my_mensage = 'CREATED'
    elif my_status_code == 202: my_mensage = 'ACCEPTED'
    elif my_status_code == 203: my_mensage = 'NON-AUTHORITATIVE INFORMATION'
    elif my_status_code == 204: my_mensage = 'NO CONTENT'
    elif my_status_code == 205: my_mensage = 'RESET CONTENT'
    elif my_status_code == 206: my_mensage = 'PARTIAL CONTENT'
    elif my_status_code == 300: my_mensage = 'MULTIPLE CHOICES'
    elif my_status_code == 301: my_mensage = 'MOVED PERMANENTLY'
    elif my_status_code == 302: my_mensage = 'FOUND'
    elif my_status_code == 303: my_mensage = 'SEE OTHER'
    elif my_status_code == 304: my_mensage = 'NOT MODIFIED'
    elif my_status_code == 307: my_mensage = 'TEMPORARY REDIRECT'
    elif my_status_code == 308: my_mensage = 'PERMANENT REDIRECT'
    elif my_status_code == 400: my_mensage = 'BAD REQUEST'
    elif my_status_code == 401: my_mensage = 'NAO AUTORIZADO'
    elif my_status_code == 403: my_mensage = 'PROIBIDO'
    elif my_status_code == 404: my_mensage = 'NOT FOUND'
    elif my_status_code == 405: my_mensage = 'METHOD NOT ALLOWED'
    elif my_status_code == 406: my_mensage = 'NOT ACCEPTABLE'
    elif my_status_code == 407: my_mensage = 'PROXY AUTHENTICATION REQUIRED'
    elif my_status_code == 408: my_mensage = 'REQUEST TIMEOUT'
    elif my_status_code == 409: my_mensage = 'CONFLICT'
    elif my_status_code == 410: my_mensage = 'GONE'
    elif my_status_code == 411: my_mensage = 'LENGTH REQUIRED'
    elif my_status_code == 412: my_mensage = 'PRECONDITION FAILED'
    elif my_status_code == 413: my_mensage = 'PAYLOAD TOO LARGE'
    elif my_status_code == 414: my_mensage = 'URI TOO LONG'
    elif my_status_code == 415: my_mensage = 'UNSUPPORTED MEDIA TYPE'
    elif my_status_code == 416: my_mensage = 'RANGE NOT SATISFIABLE'
    elif my_status_code == 417: my_mensage = 'EXPECTATION FAILED'
    elif my_status_code == 426: my_mensage = 'UPGRADE REQUIRED'
    elif my_status_code == 428: my_mensage = 'PRECONDITION REQUIRED'
    elif my_status_code == 429: my_mensage = 'TOO MANY REQUESTS'
    elif my_status_code == 431: my_mensage = 'REQUEST HEADER FIELDS TOO LARGE'
    elif my_status_code == 451: my_mensage = 'UNAVAILABLE FOR LEGAL REASONS'
    elif my_status_code == 500: my_mensage = 'INTERNAL SERVER ERROR'
    elif my_status_code == 501: my_mensage = 'NOT IMPLEMENTED'
    elif my_status_code == 502: my_mensage = 'BAD GATEWAY'
    elif my_status_code == 503: my_mensage = 'SERVICE UNAVAILABLE'
    elif my_status_code == 504: my_mensage = 'GATEWAY TIMEOUT'
    elif my_status_code == 505: my_mensage = 'HTTP VERSION NOT SUPPORTED'
    elif my_status_code == 511: my_mensage = 'NETWORK AUTHENTICATION REQUIRED'
    else: my_mensage = 'ERROR ' + str(my_status_code)
    return my_mensage
#end get_mensage

# Performs an insertion of a line according to the SQL INSERT instruction passed as argument.
# Default parameter: my_charset='UTF-8'
def insert_line(insert_sql, my_host, my_user, my_password, my_database, my_charset='UTF-8'):
    print '*****************'
    print insert_sql
    print '*****************'
    insert_conn = pymssql.connect(host=my_host, user=my_user, password=my_password, database=my_database)
    insert_cursor = insert_conn.cursor()
    insert_cursor.execute(insert_sql)
    insert_conn.commit()
    insert_conn.close()
#end insert_line
