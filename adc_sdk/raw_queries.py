CURRENT_USER = """
    query {
        me {
            email
            name
            globusUsername
            organization
            created
            updated
            id
        }
    }
"""

STUDIES = """
    query {
        studies {
            edges {
                node {
                    id
                    name
                    description
                    keywords
                    startDate
                    status
                    created
                    updated
                    permissions { edges { node { user { id name email } level } } }
                    investigations { edges { node { id name description type keywords startDatetime endDatetime created updated } } }
                    samples { edges { node { id name url keywords created updated } } }
                }
            }
        }
    }
"""

STUDY = """
    query ($id: ID!) {
        study(id: $id) {
            id
            name
            description
            keywords
            startDate
            status
            created
            updated
            permissions { edges { node { user { id name email } level } } }
            investigations { edges { node { id name description type keywords startDatetime endDatetime created updated } } }
            samples { edges { node { id name url keywords created updated } } }
        }
    }
"""

CREATE_STUDY = """
    mutation ($description: String, $keywords: [String], $name: String) {
        createStudy(description: $description, keywords: $keywords, name: $name) {
            success
            study {
                id
                name
                description
                keywords
                startDate
                status
                created
                updated
            }
        }
    }
"""

CREATE_SAMPLE = """
    mutation ($file: Upload!, $keywords: [String], $name: String!, $parentId: ID, $source: String, $studyId: ID!) {
        createSample(file: $file, keywords: $keywords, name: $name, parentId: $parentId, source: $source, studyId: $studyId) {
            success
            sample {
                id
                name
                user { id name email }
                keywords
                parent { id }
                created
                updated
                url
            }
        }
    }
"""

STUDY_SUBSCRIPTION = """
    subscription ($studyId: ID!) {
        study(studyId: $studyId) {
            study {
                id
                name
                description
                keywords
                startDate
                status
                permissions { edges { node { user { id name email } level } } }
                investigations { edges { node { id name description user { id name email }type keywords startDatetime endDatetime created updated } } }
                samples { edges { node { id name url keywords user { id name email } created } } }
                created
                updated
            }
            investigation { id name description type keywords startDatetime endDatetime created updated }
            sample { id name url user { id name email } keywords created updated }
            source
        }
    }
"""


TOKENS = """
    query {
        tokens{
            id
            name
        }
    }
"""

INVESTIGATION = """
    query ($id: ID!) {
        investigation(id: $id) {
            id
            name
            description
            type
            user { id name email }
            keywords
            study {
                id
                name
                description
                keywords
                startDate
                status
                created
                updated
                permissions { edges { node { user { id name email } level } } }
                investigations { edges { node { id name description type keywords startDatetime endDatetime created updated } } }
                samples { edges { node { id name url keywords created updated } } }
            }
            jobs { edges { node { id startDatetime endDatetime status  } } }
            startDatetime
            endDatetime
            created
            updated
        }
    }
"""

CREATE_INVESTIGATION = """
    mutation ($description: String!, $investigationType: String, $keywords: [String], $name: String!, $studyId: ID!) {
        createInvestigation(description: $description, investigationType: $investigationType, keywords: $keywords, name: $name, studyId: $studyId) {
            success
            investigation {
                id
                name
                description
                type
                user { id name email }
                keywords
                study { id name description keywords startDate status created updated }
                startDatetime
                endDatetime
                created
                updated
            }
        }
    }
"""

DELETE_TOKEN = """
    mutation ($tokenId: ID) {
        deleteToken(tokenId: $tokenId) {
            success
        }
    }
"""

SET_PERMISSIONS = """
    mutation ($permission: String, $studyId: ID, $userId: String) {
        setPermissions(permission: $permission, studyId: $studyId, userId: $userId) {
            success
        }
    }
"""

REMOVE_PERMISSIONS = """
    mutation ($studyId: ID, $userId: ID) {
        removePermissions(studyId: $studyId, userId: $userId) {
            success
        }
    }
"""

CREATE_TOKEN = """
    mutation ($name: String!) {
        createToken(name: $name){
            success
            token
        }
    }
"""

CREATE_JOB = """
    mutation ($investigationId: ID!, $sampleId: ID!, $startDatetime: DateTime!, $endDatetime: DateTime, $status: String, $source: String) {
        createJob(investigationId: $investigationId, sampleId: $sampleId, startDatetime: $startDatetime, endDatetime: $endDatetime, status: $status, source: $source) {
            success
            job {
                id
                endDatetime
                startDatetime
                status
                investigation { id name description type keywords startDatetime endDatetime created updated user { id name email } }
                sample { id name url user { id name email } keywords created updated }
                created
                updated
            }
        }
    }
"""

CREATE_DATAFILE = """
    mutation($name: String!, $jobId: ID!, $description: String, $file: Upload!, $source: String) {
        createDatafile(name: $name, jobId: $jobId, description: $description, file: $file, source: $source) {
            success
            datafile {
              id
              name
              description
              url
              user { id name email }
            }
        }
    }
"""

UPDATE_JOB = """
    mutation ($jobId: ID!, $status: String!, $endDatetime: DateTime, $source: String){
        updateJob(jobId: $jobId, status: $status, endDatetime: $endDatetime, source: $source) {
            success
            job {
                id
                startDatetime,
                endDatetime,
                status
                datafiles { edges { node { id name description url user { id name email } } } }
            }
        }
    }
"""

JOB_SUBSCRIPTION = """
    subscription ($jobId: ID!) {
        job(jobId: $jobId) {
            job {
                id
                endDatetime
                startDatetime
                status
                investigation { id name description type keywords startDatetime endDatetime created updated user { id name email } }
                sample { id name url user { id name email } keywords created updated }
                datafiles { edges { node { id name url user { id name email } created } } }
                created
                updated
            }
            datafile { id name url user { id name email } created }
            source
        }
    }
"""

INVESTIGATION_SUBSCRIPTION = """
    subscription ($investigationId: ID!) {
        investigation(investigationId: $investigationId) {
            job {
                id
                endDatetime
                startDatetime
                status
                sample { id name url user { id name email } keywords created }
                created
                updated
            }
            source
        }
    }
"""

SAMPLE = """
    query ($id: ID!){
        sample(id: $id){
            id
            name
            keywords
            url
            created
            user { id name email }
        }
    }
"""

DATAFILE = """
    query ($id: ID!) {
        datafile (id: $id) {
            id
            name
            description
            url
            user { id name email }
        }
    }
"""

JOB = """
    query ($id: ID!){
        job (id: $id){ 
            id
            startDatetime,
            endDatetime,
            status
            datafiles { edges { node { id name url user { id name email } created } } }
        }
    }
"""