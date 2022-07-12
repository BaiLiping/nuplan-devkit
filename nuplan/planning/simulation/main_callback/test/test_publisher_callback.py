import pathlib
import unittest
from unittest import TestCase
from unittest.mock import MagicMock, Mock, call, patch

from nuplan.planning.simulation.main_callback.publisher_callback import PublisherCallback, UploadConfig


class TestPublisherCallback(TestCase):
    """
    Tests PublisherCallback.
    """

    def setUp(self) -> None:
        """Setup mocks for the tests"""
        # Code execution
        fake_targets = {
            "metrics": {"upload": True, "save_path": "some/path/to/save"},
            "pictures": {"upload": True, "save_path": "some/path/to/pictures"},
        }
        self.fake_uploads = [
            UploadConfig("metrics", pathlib.Path("some/path/to/save"), pathlib.Path("user/image/path/save")),
            UploadConfig("pictures", pathlib.Path("some/path/to/pictures"), pathlib.Path("user/image/path/pictures")),
        ]
        self.publisher_callback = PublisherCallback("user", "image", fake_targets)

    def test_publisher_callback_init(self) -> None:
        """
        Tests if all the properties are set to the expected values in constructor.
        """
        # Expectations check
        self.assertEqual(self.fake_uploads, self.publisher_callback.upload_targets)

    @patch("os.getenv")
    @patch('nuplan.planning.simulation.main_callback.publisher_callback.pathlib')
    @patch('nuplan.planning.simulation.main_callback.publisher_callback.boto3')
    @patch('nuplan.planning.simulation.main_callback.publisher_callback.list_files')
    def test_on_run_simulation_end_push_to_s3(
        self, mock_files: Mock, mock_boto3: Mock, mock_pathlib: Mock, mock_getenv: Mock
    ) -> None:
        """
        Tests if the callback is called with the correct parameters.
        """
        mock_getenv.return_value = "env_var"
        fake_path = Mock()
        fake_path.iterdir.return_value = [True]
        fake_path.__truediv__ = lambda name, x: f"bucket/{x}"
        mock_pathlib.Path.return_value = fake_path
        mock_files.return_value = ["a", "b"]

        # Code execution
        self.publisher_callback.on_run_simulation_end()

        mock_boto3.client.assert_called()
        expected_calls = [
            call('some/path/to/save/a', 'env_var', 'user/image/path/save/a'),
            call('some/path/to/save/b', 'env_var', 'user/image/path/save/b'),
            call('some/path/to/pictures/a', 'env_var', 'user/image/path/pictures/a'),
            call('some/path/to/pictures/b', 'env_var', 'user/image/path/pictures/b'),
        ]
        mock_boto3.client.return_value.upload_file.assert_has_calls(expected_calls)

    @patch('nuplan.planning.simulation.main_callback.publisher_callback.pathlib', MagicMock())
    @patch('nuplan.planning.simulation.main_callback.publisher_callback.boto3')
    def test_no_push_without_results(self, mock_boto3: Mock) -> None:
        """
        Tests if the callback is called with the correct parameters.
        """
        # Code execution
        empty_publisher_callback = PublisherCallback("user", "image", {})
        empty_publisher_callback.on_run_simulation_end()

        mock_boto3.client.return_value.assert_not_called()


if __name__ == '__main__':
    unittest.main()
