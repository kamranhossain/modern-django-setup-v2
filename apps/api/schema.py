import graphene
from graphene_django import DjangoObjectType
from apps.api.models import Api


class ApiType(DjangoObjectType):
    class Meta:
        model = Api


class Query(graphene.ObjectType):
    apis = graphene.List(ApiType)

    def resolve_Apis(self, info):
        return Api.objects.all()


class CreactApi(graphene.Mutation):
    Api = graphene.Field(ApiType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Log in to add a Api")
        Api = Api(title=title, description=description, url=url, created_by=user)
        Api.save()

        return CreactApi(Api=Api)


class Mutation(graphene.ObjectType):
    create_api = CreactApi.Field()
