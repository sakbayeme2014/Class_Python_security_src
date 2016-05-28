gpg is the technic who is used from encrypt the e-mail message
rngd tools is the tools used for randomize your keys and give the Entropy, this technic is used with Linux , because in Linux you have one particular file who help
you to do this job. This file is /dev/urandom , it s not necessary with Linux to use one particular computer or another thinks to randomize your keys , its possible 
simple with your keyboard , or your mouse to generate the entropy. 

install rngd tools
download it at google.com
intel-rng-tools_0.9.1.orig.tar.gz

compile and run  
rngd -r /dev/urandom

creation gpgjeff path
mkdir /home/gpgjeff

Generation gpg keys
>>> import gnupg
>>> gpg_object = gnupg.GPG(gnupghome="/home/gpgjeff")
>>> data_object = gpg_object.gen_key_input(name_real="geoffroy_hega", name_email="geoffroy_hega@test.com", key_type="RSA", key_length=4096, passphrase="b750cd**++")
>>> key_object = gpg_object.gen_key(data_object)
>>> print key_object
73B8757896483B8218CAB3D56B58A221AD47E697
>>> print1 = str(key_object.fingerprint)
>>> 

processus export keys
>>> print1 = str(key_object.fingerprint)
>>> file_object = open("/home/gpgjeff/keyfile.asc", "a+")
>>> file_object = open("/home/gpgjeff/keyfile.asc", "wb")
>>> publickey = gpg_object.export_keys(print1)
>>> privatekey = gpg_object.export_keys(print1,secret=True)
>>> file_object.write(publickey)
>>> file_object.write(privatekey)


processus import keys
>>> from pprint import pprint
>>> file2_object = open("/home/gpgjeff/keyfile.asc", "rb")
>>> contents = file2_object.read()
>>> import_object = gpg_object.import_keys(contents)
>>> pprint(import_object.results)
[{'fingerprint': u'73B8757896483B8218CAB3D56B58A221AD47E697',
  'ok': u'0',
  'text': 'Not actually changed\n'}]

processus list keys
>>> publickey = gpg_object.list_keys()
>>> privatekey = gpg_object.list_keys(True)
>>> pprint(publickey)
[{'algo': u'1',
  'date': u'1463975604',
  'dummy': u'',
  'expires': u'',
  'fingerprint': u'73B8757896483B8218CAB3D56B58A221AD47E697',
  'keyid': u'6B58A221AD47E697',
  'length': u'4096',
  'ownertrust': u'u',
  'subkeys': [],
  'trust': u'u',
  'type': u'pub',
  'uids': [u'geoffroy_hega <geoffroy_hega@test.com>']}]
>>> pprint(privatekey)
[{'algo': u'1',
  'date': u'1463975604',
  'dummy': u'',
  'expires': u'',
  'fingerprint': u'73B8757896483B8218CAB3D56B58A221AD47E697',
  'keyid': u'6B58A221AD47E697',
  'length': u'4096',
  'ownertrust': u'',
  'subkeys': [],
  'trust': u'',
  'type': u'sec',
  'uids': [u'geoffroy_hega <geoffroy_hega@test.com>']}]

>>> file3_object = open("/home/gpgjeff/cleartext.txt", "rb")
>>> encrypted_object = gpg_object.encrypt_file(file3_object, recipients = ['geoffroy_hega@test.com'], output="/home/gpgjeff/encrypt_file.gpg")
>>> print "ok", encrypted_object.ok
ok True
>>> print "status", encrypted_object.status
status encryption ok
>>> print "stderr", encrypted_object.stderr
stderr gpg: WARNING: unsafe permissions on homedir `/home/gpgjeff
[GNUPG:] BEGIN_ENCRYPTION 2 9
[GNUPG:] END_ENCRYPTION

>>> file4_object = open("/home/gpgjeff/encrypt_file.gpg", "rb")
>>> decrypt_object = gpg_object.decrypt_file(file4_object, passphrase="b750cd**++", output="/home/gpgjeff/decrypted_files.gpg")
>>> print "ok", decrypt_object.ok
ok True
>>> print "status", decrypt_object.status
status decryption ok
>>> print "stderr", decrypt_object.stderr
stderr gpg: WARNING: unsafe permissions on homedir `/home/gpgjeff 

[GNUPG:] ENC_TO 6B58A221AD47E697 1 0
[GNUPG:] USERID_HINT 6B58A221AD47E697 geoffroy_hega <geoffroy_hega@test.com>
[GNUPG:] NEED_PASSPHRASE 6B58A221AD47E697 6B58A221AD47E697 1 0
[GNUPG:] GOOD_PASSPHRASE
gpg: encrypted with 4096-bit RSA key, ID AD47E697, created 2016-05-23
      "geoffroy_hega <geoffroy_hega@test.com>"
[GNUPG:] BEGIN_DECRYPTION
[GNUPG:] PLAINTEXT 62 1463981378 
[GNUPG:] DECRYPTION_OKAY
[GNUPG:] GOODMDC
[GNUPG:] END_DECRYPTION

