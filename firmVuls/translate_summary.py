#!/usr/bin/env python3

# Deps: python-devel postgresql-devel

import psycopg2
import time,os
from googletrans import Translator
from httpcore import SyncHTTPProxy
from httpcore._exceptions import ConnectError, ConnectTimeout, CloseError, ReadError, ReadTimeout

STARTPK = 65189
RETRY = 3
TRANSLATE = True
DBUPDATE = False


def getConn() -> object:
    return psycopg2.connect(host="localhost", port=5432,
                            database="OpManagerDB",
                            user="localuser",
                            password="localuser")


def translateTask(data: list) -> list:

    return dst


def _queryAll(cur: object) -> (int, list):
    """
    select vulid, summary from public.ncmfvvulnerabilitydetails;
    """
    cur.execute("select vulid, summary from public.ncmfvvulnerabilitydetails;")

    data = cur.fetchall()

    return len(data), data


def _query(pgcon: object, pk: int) -> list:
    """
    select vulid,summary from public.ncmfvvulnerabilitydetails where vulid=$pk;
    """
    raise NotImplementedError


def _update(cur: object, pk: int, data: str) -> int:
    cur.execute("Update public.ncmfvvulnerabilitydetails set summary = %s where id = %s", (data, pk))


if __name__ == "__main__":
    taskList = list()
    data = list()
    rlen = 0

    with getConn() as pgcon:
        with pgcon.cursor() as cur:
            rlen, data = _queryAll(cur)
            print("Total: %ld records." % rlen)

    # proxies = {'http':'http://127.0.0.1:1090'}
    proxies={"https": SyncHTTPProxy((b'http', b'127.0.0.1', 1090, b''))},
    # translator = Translator(service_urls=[
    #     'translate.google.cn',
    # ], proxies = proxies)

    translator = Translator(service_urls=[
        'translate.google.cn',
        'translate.google.com',
    ])

    idx = 0
    currentpk = 0
    _retryTimes = 0

    data = sorted(data, key = lambda x: x[0])

    if TRANSLATE:
        for row in data:
            _retry = True
            # Seek
            if STARTPK != 0 and row[0] < STARTPK:
                pass
            else:
                row = list(row)
                currentpk = row[0]
                while _retry:
                    try:
                        row[1] = translator.translate(row[1], src='en', dest='zh-CN').text
                        _retry = False
                        _retryTimes = 0
                    except (ConnectTimeout, ConnectError, CloseError, ReadTimeout) as ex:
                        _retry = True
                        _retryTimes = _retryTimes + 1
                        if _retryTimes > RETRY:
                            exit(-1)

                data[idx] = (row[0], row[1])
                # Save data to files
                with open('failsafe.txt', 'a') as fd:
                    fd.writelines("%s\n" % str(data[idx]))

                time.sleep(.05)  # 50ms / req.
                print("\rTranslated {:-6} of {:-6}, complete: {:2.2%}, currentpk: {:-6}, retry: {:-2} ".format(
                    idx, rlen, idx/rlen, currentpk, _retryTimes), end="")

            idx = idx + 1


        print("\nTranslate Done!\n")

    if DBUPDATE is False:
        exit(-1)

    with open('failsafe.txt', 'r') as fd:
        with getConn() as pgcon:
            with pgcon.cursor() as cur:
                line = fp.readline()
                idx = 1
                while line:
                    translated = eval(line)

                    # Update to Database
                    _update(pgcon, translated[0], translated[1])
                    pgcon.commit()

                    line = fp.readline()

                    idx = idx + 1
                    print("\rComplete: {:2.2%}".format(idx/rlen), end="")
