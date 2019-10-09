#!/usr/bin/env python
# coding: utf-8


import dhlab.nbtext as nb
import requests

def matrix_cosine(merge_coll, top=200):
    from scipy.spatial.distance import cosine

    stack = []
    res = dict()
    for i in merge_coll:
        res[i] = dict()
        for j in merge_coll:
            res[i][j] = 1 - cosine(merge_coll[i][:top].fillna(0), merge_coll[j][:top].fillna(0))  

    return res


adress = """http://gtweb.uit.no/cgi-bin/smi/smi.cgi?text=leat&pos=V&mode=full&action=paradigm&lang=sme&plang=sme&json=true"""


def sami_word(word='ja', pos='V', mode='full', action = 'paradigm', lang='sme'):
    params = {
        'text': word,
        'pos' : pos,
        'mode' : mode,
        'action' : action,
        'lang' : lang,
        'json' : 'true'
    }
    query_res = requests.get("http://gtweb.uit.no/cgi-bin/smi/smi.cgi" ,params=params)
    try:
        res = query_res.json()
    except:
        res = {}
    return res


