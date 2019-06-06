

MBF Biolucida Client
====================

A small client for testing interaction with the MBF Biolucida API.

Usage
-----

Create a configuration file with your credentials in the following format::

  [USERINFO]
  Username = Bob
  Password = BestPasswordEver
  Token = Gesture

The credentials file created above with the correct information should be saved in a directory::

  .secrets_dir

at the location of the **biolucidaclient.py** file.

Then use the client with the following command::

  python biolucidaclient.py bobs.info

Where **bobs.info** is the name of file with Bob's credentials saved to the **.secrets_dir**.
