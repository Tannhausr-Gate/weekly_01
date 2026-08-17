class ManifestError(Exception):
   """
   A base exception for anything this module can raise
   """

class ManifestFileNotFoundError(ManifestError):
   """
   A specific subclass raised when the manifest file doesn't exist on disk
   """

