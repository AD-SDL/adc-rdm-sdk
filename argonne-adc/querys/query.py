user = """query {
    users {
        edges {
            node {
                id
                username
                email
                created
                updated
                investigations { id name keywords }
                samples { name id url keywords }
                studies {
                    id
                    name
                    investigations { id name keywords }
                    keywords
                }
            }
        }
    }
}"""
users = """query {
    users {
        edges {
            node {
                id
                username
                email
                created
                updated
                investigations { id name keywords }
                samples { name id url keywords }
                studies {
                    id
                    name
                    investigations { id name keywords }
                    keywords
                }
            }
        }
    }
}"""
study = """query ($id: ID!){
    study(id: $id){
        id
        name
        description
        created
        updated
        keywords
        investigations {
            id
            name
            samples { id name url }
        }
        user { id username email }
        isOwner
    }
}"""
studies = """query {
    studies {
        edges {
            node {
                id
                name
                description
                created
                updated
                keywords
                investigations {
                    id
                    name
                    samples { id name url }
                }
                user { id username email }
                isOwner
            }
        }
    }
}"""
samples = """query {
    samples {
        edges {
            node {
                id
                name
                url
                keywords
                created
                updated
                user { id username email }
                isOwner
            }
        }
    }
}"""
sample = """query ($id: ID!){
    sample(id: $id){
        id
        name
        keywords
        url
        created
        updated
        user { id username email }
        isOwner
    }
}"""
me = """query {
    me {
        id
        username
        email
        studies { id name description }
        investigations { id name description
            samples {
                name
                url
            }
        }
        samples { id name url }
    }
}"""
keywordsId = """query ($id: ID!) {
        keyword (id: $id) {
            id
        }
    }"""
keywords = """query {
        keywords {
            edges {
                node {
                    id name
                }
            }
        }
    }"""
investigations = """query {
    investigations {
        edges {
            node {
                id
                name
                description
                keywords
                created
                updated
                study { id name description keywords }
                user { id username email }
                samples { id name url }
                isOwner
            }
        }
    }
}"""
investigation = """query ($id: ID!){
    investigation(id: $id){
        id
        name
        description
        keywords
        created
        updated
        study { id name description keywords }
        user { id username email }
        samples { id name url }
        isOwner
    }
}"""
createStudy = """mutation ($name: String!, $description: String!, $keywords: [String]) {
    createStudy(
        name: $name,
        description: $description,
        keywords: $keywords
    ){
        study {
            id
            name
            description
            keywords
            isOwner
            user { id username }
            investigations { id name }
        }
    }
}"""
createInvestigation = """mutation (
    $name: String!, $description: String!, $keywords: [String!],
    $studyGlobalId: ID!, $sampleGlobalIds: [ID!], $investigationType: String
) {
    createInvestigation(
        name: $name, description: $description, keywords: $keywords, studyGlobalId: $studyGlobalId,
        sampleGlobalIds: $sampleGlobalIds, investigationType: $investigationType
    ) {
        investigation {
            id
            name
            description
            isOwner
            keywords
            study { id name }
            samples { id }
            user { id username }
        }
    }
}"""
