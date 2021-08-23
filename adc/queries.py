from gql import gql
from adc import raw_queries


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
INVESTIGATION = ADCQuery(raw_queries.INVESTIGATION)

# Mutations
CREATE_TOKEN = ADCQuery(raw_queries.CREATE_TOKEN, 'createToken')
DELETE_TOKEN = ADCQuery(raw_queries.DELETE_TOKEN, 'deleteToken')
CREATE_STUDY = ADCQuery(raw_queries.CREATE_STUDY, 'createStudy')
CREATE_SAMPLE = ADCQuery(raw_queries.CREATE_SAMPLE, 'createSample')
SET_PERMISSIONS = ADCQuery(raw_queries.SET_PERMISSIONS, 'setPermissions')
REMOVE_PERMISSIONS = ADCQuery(raw_queries.REMOVE_PERMISSIONS, 'deletePermissions')
CREATE_INVESTIGATION = ADCQuery(raw_queries.CREATE_INVESTIGATION, 'createInvestigation')

# Subscription
STUDY_SUBSCRIPTION = ADCQuery(raw_queries.STUDY_SUBSCRIPTION)
