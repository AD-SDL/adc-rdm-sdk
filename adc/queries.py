from gql import gql


ME = gql(
    """
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
)

STUDIES = gql(
    """
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
                    permissions { user { id name email } level }
                    investigations { id name description type keywords startDatetime endDatetime created updated }
                    samples { id name url keywords created updated }
                }
            }
        }
    }
    """
)

STUDY = gql(
    """
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
            permissions { user { id name email } level }
            investigations { id name description type keywords startDatetime endDatetime created updated }
            samples { id name url keywords created updated }
        }
    }
    """
)

CREATE_STUDY = gql(
    """
    mutation ($description: String, $keywords: [String], $name: String) {
        createStudy(description: $description, keywords: $keywords, name: $name) {
            success
            error
            study {
                id
                name
                description
                keywords
                startDate
                status
                created
                updated
                permissions { user { id name email } level }
                investigations { id name description type keywords startDatetime endDatetime created updated }
                samples { id name url keywords created updated }
            }
        }
    }
    """
)

CREATE_SAMPLE = """
    mutation createSample($file: Upload!, $keywords: [String], $name: String!, $parentId: ID, $source: String, $studyId: ID!) {
        createSample(file: $file, keywords: $keywords, name: $name, parentId: $parentId, source: $source, studyId: $studyId) {
            success
            error
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

STUDY_SUBSCRIPTION = gql(
    """
    subscription ($studyId: ID!) {
        newSample (studyId: $studyId) {
            study {
                id
                name
                description
                keywords
                startDate
                status
                created
                updated
                permissions { user { id name email } level }
                investigations { id name description type keywords startDatetime endDatetime created updated }
                samples { id name url keywords created updated }
            }
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
            source
        }
    }
    """
)

TOKENS = gql(
    """
    query {
        tokens{
            id
            name
            token
        }
    }
    """
)

INVESTIGATION = gql(
    """
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
                permissions { user { id name email } level }
                investigations { id name description type keywords startDatetime endDatetime created updated }
                samples { id name url keywords created updated }
            }
            startDatetime
            endDatetime
            created
            updated
        }
    }
    """
)

CREATE_INVESTIGATION = gql(
    """
    mutation createInvestigation($description: String!, $investigationType: String, $keywords: [String], $name: String!, $studyId: ID!) {
        createInvestigation(description: $description, investigationType: $investigationType, keywords: $keywords, name: $name, studyId: $studyId) {
            error
            success
            investigation {
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
                    permissions { user { id name email } level }
                    investigations { id name description type keywords startDatetime endDatetime created updated }
                    samples { id name url keywords created updated }
                }
                startDatetime
                endDatetime
                created
                updated
            }
        }
    }
    """
)

CREATE_TOKEN = gql(
    """
    mutation ($name: String!) {
        createToken(name: $name) {
            success
            error
            token { id name token }
        }
    }
    """
)

DELETE_TOKEN = gql(
    """
    mutation ($tokenId: ID) {
        deleteToken(tokenId: $tokenId) {
            success
            error
        }
    }
    """
)

SET_PERMISSIONS = gql(
    """
    mutation ($permission: String, $studyId: ID, $userId: String) {
        setPermissions(permission: $permission, studyId: $studyId, userId: $userId) {
            success
            error
        }
    }
    """
)

REMOVE_PERMISSIONS = gql(
    """
    mutation ($studyId: ID, $userId: ID) {
        removePermissions(studyId: $studyId, userId: $userId) {
            success
            error
        }
    }
    """
)
