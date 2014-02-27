import unittest
import byu_ws_sdk as oit
import getpass


class TestOITWebServicesLibraryInput(unittest.TestCase):

    def test_ws_session(self):
        net_id = raw_input('NetId: ')
        password = getpass.getpass()
        res = oit.get_ws_session(net_id, password, verify=False)
        self.assertTrue('personId' in res)


if __name__ == "__main__":
    unittest.main()
