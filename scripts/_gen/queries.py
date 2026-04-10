from gql import gql


QUERY_TITLE = gql("""
query questionTitle($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
    id: questionFrontendId,
    title,
    difficulty,
    }
}
""")

QUERY_TOPICS = gql("""
query singleQuestionTopicTags($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        topicTags {
            name
        }
    }
}
""")
