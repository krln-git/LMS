
import sys
import unittest
from unittest import mock

class CleanXMLTest(unittest.TestCase):
    def test_check_roundtrip_command_injection_fixed(self):
        # Use patch.dict to avoid polluting global sys.modules for other tests
        with mock.patch.dict(sys.modules):
            # Mock dependencies
            sys.modules['django'] = mock.Mock()
            sys.modules['django.core'] = mock.Mock()
            sys.modules['django.core.management'] = mock.Mock()
            sys.modules['django.core.management.base'] = mock.Mock()
            sys.modules['fs'] = mock.Mock()
            sys.modules['fs.osfs'] = mock.Mock()
            sys.modules['lxml'] = mock.Mock()
            sys.modules['lxml.etree'] = mock.Mock()
            sys.modules['path'] = mock.Mock()
            sys.modules['xmodule'] = mock.Mock()
            sys.modules['xmodule.modulestore'] = mock.Mock()
            sys.modules['xmodule.modulestore.xml'] = mock.Mock()
            sys.modules['kombu'] = mock.Mock()
            sys.modules['kombu.utils'] = mock.Mock()
            sys.modules['lms.celery'] = mock.Mock()

            # Ensure the module is re-imported if it was already loaded
            module_name = 'lms.djangoapps.courseware.management.commands.clean_xml'
            if module_name in sys.modules:
                del sys.modules[module_name]

            from lms.djangoapps.courseware.management.commands.clean_xml import check_roundtrip

            with mock.patch('lms.djangoapps.courseware.management.commands.clean_xml.subprocess.call') as mock_subprocess, \
                 mock.patch('lms.djangoapps.courseware.management.commands.clean_xml.os.system') as mock_system, \
                 mock.patch('lms.djangoapps.courseware.management.commands.clean_xml.import_with_checks') as mock_import, \
                 mock.patch('lms.djangoapps.courseware.management.commands.clean_xml.export') as mock_export:

                mock_import.return_value = (True, mock.Mock())

                course_dir = 'course_dir; rm -rf /'
                export_dir = course_dir + '.rt'

                check_roundtrip(course_dir)

                mock_subprocess.assert_called_with(['diff', '-r', course_dir, export_dir])
                mock_system.assert_not_called()

if __name__ == '__main__':
    unittest.main()
