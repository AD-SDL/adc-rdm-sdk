from gql import gql
from adc_sdk.queries import raw_queries


class ADCQuery:
    def __init__(self, query, path=None):
        self.raw_query = query
        self.query = gql(self.raw_query)
        self.path = path


# Auth
CURRENT_USER = ADCQuery(raw_queries.CURRENT_USER)
TOKENS = ADCQuery(raw_queries.TOKENS)
CREATE_TOKEN = ADCQuery(raw_queries.CREATE_TOKEN, "createToken")
DELETE_TOKEN = ADCQuery(raw_queries.DELETE_TOKEN, "deleteToken")

# Studies
STUDIES = ADCQuery(raw_queries.STUDIES)
STUDY = ADCQuery(raw_queries.STUDY)
CREATE_STUDY = ADCQuery(raw_queries.CREATE_STUDY, "createStudy")
STUDY_SUBSCRIPTION = ADCQuery(raw_queries.STUDY_SUBSCRIPTION)

# Study permissions
SET_PERMISSIONS = ADCQuery(raw_queries.SET_PERMISSIONS, "setPermissions")
REMOVE_PERMISSIONS = ADCQuery(raw_queries.REMOVE_PERMISSIONS, "deletePermissions")

# Samples
SAMPLES = ADCQuery(raw_queries.SAMPLES)
SAMPLE = ADCQuery(raw_queries.SAMPLE)
CREATE_SAMPLE = ADCQuery(raw_queries.CREATE_SAMPLE, "createSample")
ADD_FILES_TO_SAMPLE = ADCQuery(raw_queries.ADD_FILES_TO_SAMPLE, "addFilesToSample")
REMOVE_FILES_FROM_SAMPLE = ADCQuery(raw_queries.REMOVE_FILES_FROM_SAMPLE, "removeFilesFromSample")

# Investigations
INVESTIGATION = ADCQuery(raw_queries.INVESTIGATION)
CREATE_INVESTIGATION = ADCQuery(raw_queries.CREATE_INVESTIGATION, "createInvestigation")
INVESTIGATION_SUBSCRIPTION = ADCQuery(raw_queries.INVESTIGATION_SUBSCRIPTION)

# Job/Runs
JOB = ADCQuery(raw_queries.JOB)
CREATE_JOB = ADCQuery(raw_queries.CREATE_JOB, "createJob")
UPDATE_JOB = ADCQuery(raw_queries.UPDATE_JOB, "updateJob")
JOB_SUBSCRIPTION = ADCQuery(raw_queries.JOB_SUBSCRIPTION)

# Datafiles
DATAFILE = ADCQuery(raw_queries.DATAFILE)
CREATE_DATAFILE = ADCQuery(raw_queries.CREATE_DATAFILE, "createDatafile")
