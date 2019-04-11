"""
Ensembl module related exceptions
"""
from exceptions import AppException


class EnsemblServiceException(AppException):
    def __init__(self, value):
        super(EnsemblServiceException, self).__init__(value)


class EnsemblDownloadManagerException(AppException):
    def __init__(self, value):
        super(EnsemblDownloadManagerException, self).__init__(value)


if __name__ == '__main__':
    print("ERROR: This script is part of a pipeline collection and it is not meant to be run in stand alone mode")
