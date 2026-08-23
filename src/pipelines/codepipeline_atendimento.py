# O pipeline de CI/CD em Python, sempre com o path completo. 
# Esse arquivo define um AWS CodePipeline que automatiza o deploy das Lambdas, Step Functions e testes.

import boto3

def create_codepipeline():
    """
    Cria um pipeline de CI/CD para o fluxo de atendimento.
    """
    client = boto3.client("codepipeline")

    pipeline_definition = {
        "pipeline": {
            "name": "ClinicasAtendimentoPipeline",
            "roleArn": "arn:aws:iam::123456789012:role/CodePipelineRole",
            "artifactStore": {
                "type": "S3",
                "location": "clinicas-pipeline-artifacts"
            },
            "stages": [
                {
                    "name": "Source",
                    "actions": [
                        {
                            "name": "SourceCode",
                            "actionTypeId": {
                                "category": "Source",
                                "owner": "AWS",
                                "provider": "CodeCommit",
                                "version": "1"
                            },
                            "outputArtifacts": [{"name": "SourceOutput"}],
                            "configuration": {
                                "RepositoryName": "clinicas-devops",
                                "BranchName": "main"
                            }
                        }
                    ]
                },
                {
                    "name": "Build",
                    "actions": [
                        {
                            "name": "BuildLambda",
                            "actionTypeId": {
                                "category": "Build",
                                "owner": "AWS",
                                "provider": "CodeBuild",
                                "version": "1"
                            },
                            "inputArtifacts": [{"name": "SourceOutput"}],
                            "outputArtifacts": [{"name": "BuildOutput"}],
                            "configuration": {
                                "ProjectName": "ClinicasLambdaBuild"
                            }
                        }
                    ]
                },
                {
                    "name": "Test",
                    "actions": [
                        {
                            "name": "RunTests",
                            "actionTypeId": {
                                "category": "Test",
                                "owner": "AWS",
                                "provider": "CodeBuild",
                                "version": "1"
                            },
                            "inputArtifacts": [{"name": "BuildOutput"}],
                            "configuration": {
                                "ProjectName": "ClinicasTests"
                            }
                        }
                    ]
                },
                {
                    "name": "Deploy",
                    "actions": [
                        {
                            "name": "DeployLambda",
                            "actionTypeId": {
                                "category": "Deploy",
                                "owner": "AWS",
                                "provider": "CodeDeploy",
                                "version": "1"
                            },
                            "inputArtifacts": [{"name": "BuildOutput"}],
                            "configuration": {
                                "ApplicationName": "ClinicasLambdaApp",
                                "DeploymentGroupName": "ClinicasLambdaDG"
                            }
                        }
                    ]
                }
            ]
        }
    }

    response = client.create_pipeline(**pipeline_definition)
    print("✅ Pipeline criado:", response["pipeline"]["name"])

if __name__ == "__main__":
    create_codepipeline()
