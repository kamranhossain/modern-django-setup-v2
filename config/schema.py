import graphene
import graphql_jwt
from apps.api import schema as api_schema
from apps.users import schema as user_schema


class Query(user_schema.Query, api_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, api_schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
