# Cloud_ComputeData.py

import os
from generate_key import generate_rsa_key
import rsa
from datetime import datetime

Position_file = "Data/Item_Region.txt"
Price_file = "Data/Price.txt"
Account_file = "Data/Account.txt"
History_file = "Data/Shopping_History.txt"
Face_file = "Data/face_encoding.txt"

pubkey_file = "Data/public.pem"
privkey_file = "Data/private.pem"


def _parser(filename: str) -> dict:
    result = dict()
    f = open(filename, "r")
    for line in f:
        l = line.strip().split("|")
        result[l[0].strip().lower()] = l[1].strip()
    return result


def get_pub_private_key():
    if not os.path.exists(pubkey_file) or not os.path.exists(privkey_file):
        generate_rsa_key(pubkey_file, privkey_file)

    with open(privkey_file) as privatefile:
        p = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(p)

    with open(pubkey_file) as pubkeyfile:
        p = pubkeyfile.read()
        pubkeyfile = rsa.PublicKey.load_pkcs1(p)

    return pubkeyfile, privkey


def getDataDict() -> ("position_dict", "price_dict", "id_dict"):
    pos_dict = _parser(Position_file)
    price_dict = _parser(Price_file)
    id_dict = _parser(Account_file)
    return (pos_dict, price_dict, id_dict)


def updateAccount(name: str, password: str) -> int:
    try:
        with open(Account_file, "a+") as f:
            f.write(name + "|" + password + "\n")
    except:
        return 1
    else:
        return 0


def getUserHistory(userID:str):
    with open(History_file) as f:
        items = []
        for line in f:
            line = line.strip().split("|")
            if line[0] == userID:
                items.append([line[i] for i in range(2,len(line),2)])
        return items


def updateUserHistory(hist: []):
    hist = [str(datetime.now())] + hist
    try:
        with open(History_file, "a+") as f:
            f.write('|'.join(hist) + "\n")
    except Exception as e:
        return (1, str(e))
    else:
        return (0, "")


def getFaceEncodings():
    with open(Face_file) as f:
        faces = []
        names = []
        for line in f:
            line = line.strip().split('|')
            faces.append(line[0])
            names.append(line[1])
        return faces, names

