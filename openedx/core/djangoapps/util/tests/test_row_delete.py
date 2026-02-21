
from unittest.mock import MagicMock
from django.test import TestCase
from openedx.core.djangoapps.util.row_delete import delete_rows

class DeleteRowsTest(TestCase):
    def setUp(self):
        self.mock_mgr = MagicMock()
        self.mock_item = MagicMock()
        self.mock_item.id = 1
        self.mock_item.max_id = 100
        self.mock_mgr.raw.return_value = [self.mock_item]

    def test_delete_rows_valid(self):
        """
        Test delete_rows with valid table and column names.
        """
        table_name = "auth_user"
        primary_id_name = "id"

        delete_rows(self.mock_mgr, table_name, primary_id_name, chunk_size=100, sleep_between=0)

        # Verify calls
        self.assertTrue(self.mock_mgr.raw.called)
        first_call = self.mock_mgr.raw.call_args_list[0]
        self.assertIn("SELECT MIN(id) as id, MAX(id) as max_id FROM auth_user", first_call[0][0])

        # With max_id=100 and chunk_size=100, range is [1, 100]. Count is 100.
        # deletions_now = min(100, 100) = 100.
        # upper_id = 1 + 100 = 101.
        second_call = self.mock_mgr.raw.call_args_list[1]
        self.assertIn("DELETE FROM auth_user WHERE id >= 1 AND id < 101", second_call[0][0])

    def test_delete_rows_invalid_table_name(self):
        """
        Test delete_rows raises ValueError with invalid table name.
        """
        table_name = "users; DROP TABLE users; --"
        primary_id_name = "id"

        with self.assertRaises(ValueError):
            delete_rows(self.mock_mgr, table_name, primary_id_name, chunk_size=100, sleep_between=0)

    def test_delete_rows_invalid_primary_id(self):
        """
        Test delete_rows raises ValueError with invalid primary_id_name.
        """
        table_name = "auth_user"
        primary_id_name = "id OR 1=1"

        with self.assertRaises(ValueError):
            delete_rows(self.mock_mgr, table_name, primary_id_name, chunk_size=100, sleep_between=0)
