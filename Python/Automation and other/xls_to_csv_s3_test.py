import unittest
from unittest.mock import patch, MagicMock, call
import os
import sys
import pandas as pd
from botocore.exceptions import NoCredentialsError
import xls_to_csv_s3

class TestUploadFilesToS3(unittest.TestCase):
    
    @patch('xls_to_csv_s3.boto3.client')
    @patch('xls_to_csv_s3.os.listdir')
    @patch('xls_to_csv_s3.os.path.join')
    def test_upload_csv_files_success(self, mock_join, mock_listdir, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_listdir.return_value = ['test.csv']
        mock_join.return_value = '/folder/test.csv'
        
        xls_to_csv_s3.upload_files_to_s3('/folder', 'test-bucket')
        
        mock_s3.upload_file.assert_called_once_with('/folder/test.csv', 'test-bucket', 'test.csv')
    
    @patch('xls_to_csv_s3.boto3.client')
    @patch('xls_to_csv_s3.os.listdir')
    @patch('xls_to_csv_s3.os.path.join')
    def test_upload_csv_no_credentials(self, mock_join, mock_listdir, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_s3.upload_file.side_effect = NoCredentialsError()
        mock_listdir.return_value = ['test.csv']
        mock_join.return_value = '/folder/test.csv'
        
        with patch('builtins.print') as mock_print:
            xls_to_csv_s3.upload_files_to_s3('/folder', 'test-bucket')
            mock_print.assert_called_with("AWS Credentials not available.")
    
    @patch('xls_to_csv_s3.boto3.client')
    @patch('xls_to_csv_s3.os.listdir')
    @patch('xls_to_csv_s3.os.path.join')
    @patch('xls_to_csv_s3.pd.ExcelFile')
    @patch('xls_to_csv_s3.pd.read_excel')
    @patch('xls_to_csv_s3.os.remove')
    @patch('xls_to_csv_s3.os.path.exists')
    def test_upload_excel_files_success(self, mock_exists, mock_remove, mock_read_excel, 
                                       mock_excel_file, mock_join, mock_listdir, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_listdir.return_value = ['test.xlsx']
        mock_join.side_effect = lambda x, y: f"{x}/{y}"
        
        mock_xls = MagicMock()
        mock_xls.sheet_names = ['Sheet1', 'Sheet2']
        mock_excel_file.return_value = mock_xls
        
        mock_df = MagicMock()
        mock_read_excel.return_value = mock_df
        mock_exists.return_value = True
        
        xls_to_csv_s3.upload_files_to_s3('/folder', 'test-bucket')
        
        assert mock_s3.upload_file.call_count == 2
        assert mock_remove.call_count == 2
    
    @patch('xls_to_csv_s3.boto3.client')
    @patch('xls_to_csv_s3.os.listdir')
    @patch('xls_to_csv_s3.os.path.join')
    @patch('xls_to_csv_s3.pd.ExcelFile')
    def test_upload_excel_file_processing_error(self, mock_excel_file, mock_join, 
                                                mock_listdir, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_listdir.return_value = ['test.xlsx']
        mock_join.return_value = '/folder/test.xlsx'
        mock_excel_file.side_effect = Exception("Invalid Excel file")
        
        with patch('builtins.print') as mock_print:
            xls_to_csv_s3.upload_files_to_s3('/folder', 'test-bucket')
            mock_print.assert_called_with("Error processing test.xlsx: Invalid Excel file")
    
    @patch('xls_to_csv_s3.boto3.client')
    @patch('xls_to_csv_s3.os.listdir')
    def test_empty_folder(self, mock_listdir, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_listdir.return_value = []
        
        xls_to_csv_s3.upload_files_to_s3('/folder', 'test-bucket')
        
        mock_s3.upload_file.assert_not_called()
    
    @patch('xls_to_csv_s3.boto3.client')
    @patch('xls_to_csv_s3.os.listdir')
    @patch('xls_to_csv_s3.os.path.join')
    def test_upload_generic_exception(self, mock_join, mock_listdir, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        mock_s3.upload_file.side_effect = Exception("S3 error")
        mock_listdir.return_value = ['test.csv']
        mock_join.return_value = '/folder/test.csv'
        
        with patch('builtins.print') as mock_print:
            xls_to_csv_s3.upload_files_to_s3('/folder', 'test-bucket')
            mock_print.assert_called_with("Error uploading test.csv: S3 error")


if __name__ == '__main__':
    unittest.main()