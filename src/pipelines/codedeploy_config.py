# Esse script cria a configuração do AWS CodeDeploy para gerenciar o deploy das funções Lambda de forma automatizada e segura.


import boto3

def create_codedeploy_config():
    """
    Cria configuração de CodeDeploy para atualizar Lambdas do fluxo de atendimento.
    """
    client = boto3.client("codedeploy")

    response = client.create_deployment_group(
        applicationName="ClinicasLambdaApp",
        deploymentGroupName="ClinicasLambdaDG",
        serviceRoleArn="arn:aws:iam::123456789012:role/CodeDeployRole",
        deploymentConfigName="CodeDeployDefault.LambdaAllAtOnce",
        deploymentGroupName="ClinicasLambdaDG",
        deploymentStyle={
            "deploymentType": "BLUE_GREEN",
            "deploymentOption": "WITH_TRAFFIC_CONTROL"
        },
        blueGreenDeploymentConfiguration={
            "terminateBlueInstancesOnDeploymentSuccess": {
                "action": "TERMINATE",
                "terminationWaitTimeInMinutes": 5
            },
            "deploymentReadyOption": {
                "actionOnTimeout": "CONTINUE_DEPLOYMENT",
                "waitTimeInMinutes": 2
            }
        },
        autoRollbackConfiguration={
            "enabled": True,
            "events": ["DEPLOYMENT_FAILURE"]
        }
    )

    print("✅ Deployment Group criado:", response["deploymentGroupInfo"]["deploymentGroupName"])

if __name__ == "__main__":
    create_codedeploy_config()
