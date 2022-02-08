# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "batch_python_tutorial_ffmpeg.py"

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.

_BATCH_ACCOUNT_NAME = 'wenyitestbatch'
_BATCH_ACCOUNT_KEY = 'T2Ok2fe8D3W/hueQrZ/4IIAzcx5guNCezajSFK4hVdPfKwnSCzSgyW7H8GK55SSHnM3FO+Y0GfdByC9oH8ltkg=='
_BATCH_ACCOUNT_URL = 'https://wenyitestbatch.southeastasia.batch.azure.com'
_STORAGE_ACCOUNT_NAME = 'wenyibatchsa'
_STORAGE_ACCOUNT_KEY = 'toi9mLBgKO2LrkzFz590nXBqf1AM4tValCfu+pYaUeeAX1PLz482Vam7ZUCSN7dLz3N9/v0TwAZEADJbOAMJ2g=='
_POOL_ID = 'LinuxFfmpegPool'
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 5
_POOL_VM_SIZE = 'STANDARD_A1_v2'
_JOB_ID = 'LinuxFfmpegJob'
