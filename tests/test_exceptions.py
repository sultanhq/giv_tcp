import unittest

from GivTCP.givenergy_modbus_async.exceptions import CommunicationError, ExceptionBase


class ExceptionBaseTests(unittest.TestCase):
    def test_base_exception_uses_fallback_message(self):
        err = ExceptionBase()

        self.assertEqual("ExceptionBase", str(err))
        self.assertEqual("ExceptionBase", err.message)

    def test_subclass_can_be_created_without_message(self):
        err = CommunicationError()

        self.assertEqual("CommunicationError", str(err))
        self.assertEqual("CommunicationError", err.message)

    def test_explicit_message_is_preserved(self):
        err = CommunicationError("socket closed")

        self.assertEqual("socket closed", str(err))
        self.assertEqual("socket closed", err.message)


if __name__ == "__main__":
    unittest.main()
