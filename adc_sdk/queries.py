from gql import gql
from adc_sdk import raw_queries


class ADCQuery:

    def __init__(self, query, path=None):
        self.raw_query = query
        self.query = gql(self.raw_query)
        self.path = path


# Queries
CURRENT_USER = ADCQuery(raw_queries.CURRENT_USER)
TOKENS = ADCQuery(raw_queries.TOKENS)
STUDIES = ADCQuery(raw_queries.STUDIES)
STUDY = ADCQuery(raw_queries.STUDY)
SAMPLE = ADCQuery(raw_queries.SAMPLE)
DATAFILE = ADCQuery(raw_queries.DATAFILE)
JOB = ADCQuery(raw_queries.JOB)
INVESTIGATION = ADCQuery(raw_queries.INVESTIGATION)

# Mutations
CREATE_TOKEN = ADCQuery(raw_queries.CREATE_TOKEN, 'createToken')
DELETE_TOKEN = ADCQuery(raw_queries.DELETE_TOKEN, 'deleteToken')
CREATE_STUDY = ADCQuery(raw_queries.CREATE_STUDY, 'createStudy')
CREATE_SAMPLE = ADCQuery(raw_queries.CREATE_SAMPLE, 'createSample')
CREATE_JOB = ADCQuery(raw_queries.CREATE_JOB, 'createJob')
CREATE_DATAFILE = ADCQuery(raw_queries.CREATE_DATAFILE, 'createDatafile')
UPDATE_JOB = ADCQuery(raw_queries.UPDATE_JOB, 'updateJob')
SET_PERMISSIONS = ADCQuery(raw_queries.SET_PERMISSIONS, 'setPermissions')
REMOVE_PERMISSIONS = ADCQuery(raw_queries.REMOVE_PERMISSIONS, 'deletePermissions')
CREATE_INVESTIGATION = ADCQuery(raw_queries.CREATE_INVESTIGATION, 'createInvestigation')

# Subscription
STUDY_SUBSCRIPTION = ADCQuery(raw_queries.STUDY_SUBSCRIPTION)
INVESTIGATION_SUBSCRIPTION = ADCQuery(raw_queries.INVESTIGATION_SUBSCRIPTION)
JOB_SUBSCRIPTION = ADCQuery(raw_queries.JOB_SUBSCRIPTION)
