import json
import boto3

# 初始化 CodeDeploy 客户端
codedeploy = boto3.client('codedeploy')

def pre_handler(event, context):
    """
    部署前的 hook function。
    它可以在流量切换到新版本的 Lambda 函数之前执行某些操作。
    """
    print("Pre-deployment hook triggered")
    print(f"Event: {json.dumps(event)}")

    # 获取 CodeDeploy 的部署 ID 和生命周期事件 Hook 的执行 ID
    deployment_id = event.get('DeploymentId')
    lifecycle_event_hook_execution_id = event.get('LifecycleEventHookExecutionId')

    try:
        # 检查配置、初始化资源等前置操作可以在这里进行

        # 报告前置操作成功
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=deployment_id,
            lifecycleEventHookExecutionId=lifecycle_event_hook_execution_id,
            status='Succeeded'  # 如果前置操作失败，可以将 'Succeeded' 改为 'Failed'
        )
        print("Pre-deployment checks passed and reported as succeeded")
        return {
            'statusCode': 200,
            'body': json.dumps('Pre-deployment checks passed')
        }

    except Exception as e:
        print(f"Error during pre-deployment hook: {str(e)}")

        # 报告失败状态给 CodeDeploy
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=deployment_id,
            lifecycleEventHookExecutionId=lifecycle_event_hook_execution_id,
            status='Failed'
        )
        raise e


def post_handler(event, context):
    """
    部署后的 hook function。
    它可以在流量切换到新版本的 Lambda 函数之后执行某些操作。
    """
    print("Post-deployment hook triggered")
    print(f"Event: {json.dumps(event)}")

    # 获取 CodeDeploy 的部署 ID 和生命周期事件 Hook 的执行 ID
    deployment_id = event.get('DeploymentId')
    lifecycle_event_hook_execution_id = event.get('LifecycleEventHookExecutionId')

    try:
        # 记录日志、清理资源等后置操作可以在这里进行

        # 报告后置操作成功
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=deployment_id,
            lifecycleEventHookExecutionId=lifecycle_event_hook_execution_id,
            status='Succeeded'
        )
        print("Post-deployment tasks completed and reported as succeeded")
        return {
            'statusCode': 200,
            'body': json.dumps('Post-deployment tasks completed')
        }

    except Exception as e:
        print(f"Error during post-deployment hook: {str(e)}")

        # 报告失败状态给 CodeDeploy
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=deployment_id,
            lifecycleEventHookExecutionId=lifecycle_event_hook_execution_id,
            status='Failed'
        )
        raise e
