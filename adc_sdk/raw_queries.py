CURRENT_USER = """
    query {
        me {
            email
            name
            globusUsername
            organization
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
                    status
                    created
                    updated
                    startDate
                    endDate
                    permissions {
                        edges {
                            node {
                                user {
                                    id
                                    name
                                    email
                                }
                                level
                            }
                        }
                    }
                    investigations {
                        edges {
                            node {
                                id
                                name
                            }
                        }
                    }
                    samples {
                        edges {
                            node {
                                id
                                name
                            }
                        }
                    }
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
            status
            created
            updated
            startDate
            endDate
            permissions {
                edges {
                    node {
                        user {
                            id
                            name
                            email
                        }
                        level
                    }
                }
            }
            investigations {
                edges {
                    node {
                        id
                        name
                    }
                }
            }
            samples {
                edges {
                    node {
                        id
                        name
                    }
                }
            }
        }
    }
"""

CREATE_STUDY = """
    mutation (
        $name: String!,
        $description: String,
        $keywords: [String!],
        $startDate: Date,
        $endDate: Date
    ) {
        createStudy(
            name: $name,
            description: $description,
            keywords: $keywords,
            startDate: $startDate,
            endDate: $endDate
        ){
            study {
                id
                name
                description
                keywords
                startDate
                endDate
                status
                permissions { edges { node { user { id name email } level } } }
            }
        }
    }
"""

CREATE_SAMPLE = """
    mutation (
        $name: String!,
        $studyId: ID!
        $file: Upload,
        $keywords: [String],
        $parentId: ID,
        $source: String
    ) {
        createSample(
            name: $name,
            studyId: $studyId,
            file: $file,
            keywords: $keywords,
            parentId: $parentId,
            source: $source
        ) {
            success
            sample {
                id
                name
                keywords
                parent { id name keywords url }
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
            }
            investigation { id name description investigationType keywords startDate endDate }
            sample { id name url keywords }
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
            investigationType
            user { id name email }
            keywords
            study {
                id
                name
                description
                keywords
                startDate
                status
            }
            jobs { edges { node { id startDatetime endDatetime status  } } }
            startDate
            endDate
        }
    }
"""

CREATE_INVESTIGATION = """
    mutation (
        $studyId: ID!
        $name: String!,
        $description: String,
        $investigationType: String,
        $keywords: [String],
        $startDate: Date,
        $endDate: Date,
        $source: String
    ) {
        createInvestigation(
            studyId: $studyId, 
            name: $name,
            description: $description,
            investigationType: $investigationType,
            keywords: $keywords,
            startDate: $startDate,
            endDate: $endDate,
            source: $source
        ) {
            success
            investigation {
                id
                name
                description
                investigationType
                user { id name email }
                keywords
                study { id name description keywords startDate status }
                startDate
                endDate
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
    mutation (
        $investigationId: ID!,
        $sampleId: ID,
        $startDatetime: DateTime,
        $endDatetime: DateTime,
        $status: String,
        $source: String
    ) {
        createJob(investigationId: $investigationId, sampleId: $sampleId, startDatetime: $startDatetime, endDatetime: $endDatetime, status: $status, source: $source) {
            success
            job {
                id
                endDatetime
                startDatetime
                status
                investigation { id name description investigationType keywords startDate endDate user { id name email } }
                sample { id name url user { id name email } keywords }
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
    mutation (
        $jobId: ID!,
        $status: String,
        $startDatetime: DateTime,
        $endDatetime: DateTime,
        $source: String
    ){
        updateJob(
            jobId: $jobId,
            status: $status,
            startDatetime: $startDatetime,
            endDatetime: $endDatetime,
            source: $source
        ) {
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
                datafiles { 
                    edges { 
                        node {
                            id 
                            name
                            url
                        }
                    } 
                }
            }
            datafile { id name url }
            source
        }
    }
"""

INVESTIGATION_SUBSCRIPTION = """
    subscription ($investigationId: ID!) {
        investigation(investigationId: $investigationId) {
            investigation {
                id
                name
                description
                investigationType
                keywords
                startDate
                endDate
            }
            job {
                id
                endDatetime
                startDatetime
                status
                sample { id name url user { id name email } keywords }
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
            datafiles { 
                edges { 
                    node {
                        id 
                        name
                        url
                    }
                } 
            }
            user {
                id
                email
                name
            }
        }
    }
"""
