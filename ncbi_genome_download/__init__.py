"""Download genome files from the NCBI"""
from .core import (
    download,
    SUPPORTED_TAXONOMIC_GROUPS,
    EFormats,
    EAssemblyLevels,
    EDefaults
)

__version__ = '0.3.0'
__all__ = [
    'download',
    'SUPPORTED_TAXONOMIC_GROUPS',
    'EFormats',
    'EAssemblyLevels',
    'EDefaults'
]
