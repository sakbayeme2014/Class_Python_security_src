Generate keys
>>> import gnupg
>>> gpg_object = gnupg.GPG(gnupghome="/home/gpgjeff")
>>> data_object = gpg_object.gen_key_input(name_real="geoffroy_hega", name_email="geoffroy@test.com", key_type="RSA", key_length=4096, passphrase="b750cd**++")
>>> key_object = gpg_object.gen_key(data_object)
>>> print key_object
DAD7F3765D705F44CCBF16D5D7E9FD00D85C1581
>>> print1 = str(key_object.fingerprint)

export keys
>>> file_object = open("/home/gpgjeff/keyfile.asc", "a+")
>>> file_object = open("/home/gpgjeff/keyfile.asc", "wb")
>>> publickey = gpg_object.export_keys(print1)
>>> privatekey = gpg_object.export_keys(print1, secret=True)
>>> from pprint import pprint
>>> file_object.write(publickey)
>>> file_object.write(privatekey)

import keys
>>> file2_object = open("/home/gpgjeff/keyfile.asc", "rb")
>>> contents = file2_object.read()
>>> import_object = gpg_object.import_keys(contents)
>>> pprint(import_object.results)
[{'fingerprint': u'DAD7F3765D705F44CCBF16D5D7E9FD00D85C1581',
  'ok': u'0',
  'text': 'Not actually changed\n'}]

list keys
>>> publickey = gpg_object.list_keys()
>>> privatekey = gpg_object.list_keys(True)
>>> pprint(publickey)
[{'algo': u'1',
  'date': u'1464065634',
  'dummy': u'',
  'expires': u'',
  'fingerprint': u'DAD7F3765D705F44CCBF16D5D7E9FD00D85C1581',
  'keyid': u'D7E9FD00D85C1581',
  'length': u'4096',
  'ownertrust': u'u',
  'subkeys': [],
  'trust': u'u',
  'type': u'pub',
  'uids': [u'geoffroy_hega <geoffroy@test.com>']}]
>>> pprint(privatekey)
[{'algo': u'1',
  'date': u'1464065634',
  'dummy': u'',
  'expires': u'',
  'fingerprint': u'DAD7F3765D705F44CCBF16D5D7E9FD00D85C1581',
  'keyid': u'D7E9FD00D85C1581',
  'length': u'4096',
  'ownertrust': u'',
  'subkeys': [],
  'trust': u'',
  'type': u'sec',
  'uids': [u'geoffroy_hega <geoffroy@test.com>']}]

encryption string process
>>> string = " i like coding in python "
>>> encrypt_string = gpg_object.encrypt(string, "geoffroy_hega@test.com")
>>> data_encrypt = str(encrypt_string)
>>> print "ok:", encrypt_string.ok
ok: False
>>> string = " i like coding in python "
>>> encrypt_string = gpg_object.encrypt(string, "geoffroy@test.com")
>>> data_encrypt = str(encrypt_string)
>>> print "ok", encrypt_string.ok
ok True
>>> print "status", encrypt_string.status
status encryption ok
>>> print "stderr", encrypt_string.stderr
stderr gpg: WARNING: unsafe permissions on homedir `/home/gpgjeff
[GNUPG:] BEGIN_ENCRYPTION 2 9
[GNUPG:] END_ENCRYPTION

>>> print "encrypt_string", encrypt_string
encrypt_string -----BEGIN PGP MESSAGE-----
Version: GnuPG v1.4.10 (GNU/Linux)

hQIMA9fp/QDYXBWBAQ/6AvMDLUyUsg56p3LKYhXaPb+Kc6ayzapKPPLzjsrI7m7/
dW/6Q9zRHj/OYgc0YNuQfFsmsy+x8WAN5sjBPLjGaleLCewXogTU8XzblltuNv93
PNEZxPLFCbw8rqJcCGz6767OT2Qpe5t0KkqrLv8XUJAQiRMWK8AnQQhuC/+9twdE
5cSARULcSR7KTtdMj3n2Z1+3Ecd6LBVrS+KHasbOb3ial2W10mMQBLv+KLdZ4cip
FZNa73zBD2IuT/5ARF8frJLjIYaeQf3BA+zsqC8vdUTOPpnmosDp6GaxMxh29aD4
Z1RowUT5iRm9BIBzFW2lySICwo8gHV6Crbeimu4u2U327s1FHoKQ+7tpqySgz30u
xit17QWVqszzWKKND9/nkpfSCKp6zfsOiTr6GYlJoINMyUuvpLMsnsS4FzwVfEKF
RRlGXgGqPeWewhoFj86g0HO5rpEYop6NYBWldWoC3g6MH1l4YsIbD+mnRYVgqCGM
iexzVY14Tox0ehPTq733IgM4upc7XKiD7J2EqYS8yIKJS2BArPRdIyYb7qMResIX
cy7G0+LYWaBZe32OhP0exQxeZ+8Hg4pny6ww2TK4fp+Wam9x4FuNrhipewTl+X4k
AzG5tRl9aAAEM92xFj/8eHnq/qf/Q/7yGprUPA5XkskkY7+NT3EiMYso3S6SIsfS
VAEeYXODeFUy75rtzuA5COqhLtZnSrgC4gzl/1M34T4xRfXf2RRB9uGRrv5G/6TG
P/3czjuLDxr3g5Ca8MRj8gVemof4cnqCQMSwEVCiDdS+VlQSUQ==
=s0hM
-----END PGP MESSAGE-----

>>> string = " i like coding in python"
>>> string_encrypt = gpg_object.encrypt(string, "geoffroy@test.com")
>>> data1_encrypt = str(string_encrypt)
>>> data2_decrypt = gpg_object.decrypt(data1_encrypt, passphrase="b750cd**++")
>>> print "ok", data2_decrypt.ok
ok True
>>> print "status", data2_decrypt.status
status decryption ok
>>> print "stderr", data2_decrypt.stderr
stderr gpg: WARNING: unsafe permissions on homedir `/home/gpgjeff
[GNUPG:] ENC_TO D7E9FD00D85C1581 1 0
[GNUPG:] USERID_HINT D7E9FD00D85C1581 geoffroy_hega <geoffroy@test.com>
[GNUPG:] NEED_PASSPHRASE D7E9FD00D85C1581 D7E9FD00D85C1581 1 0
[GNUPG:] GOOD_PASSPHRASE
gpg: encrypted with 4096-bit RSA key, ID D85C1581, created 2016-05-24
      "geoffroy_hega <geoffroy@test.com>"
[GNUPG:] BEGIN_DECRYPTION
[GNUPG:] PLAINTEXT 62 1464070571 
[GNUPG:] PLAINTEXT_LENGTH 24
[GNUPG:] DECRYPTION_OKAY
[GNUPG:] GOODMDC
[GNUPG:] END_DECRYPTION

>>> print "data2_decrypt", data2_decrypt.data
data2_decrypt  i like coding in python
